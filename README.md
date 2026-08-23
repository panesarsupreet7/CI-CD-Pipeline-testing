1. Project Overview

This project implements an end-to-end CI/CD pipeline for a Flask-based Student Registration Application.

The pipeline automates the process of taking application changes from GitHub, testing and containerizing the application, pushing the Docker image to Amazon ECR, deploying it to an Amazon EC2 instance, verifying the deployment, and sending an email notification.

CI/CD Flow
Developer Pushes Code
        ↓
GitHub Repository
        ↓
GitHub Actions
        ↓
Checkout
        ↓
Install Dependencies
        ↓
Run Tests
        ↓
Build Docker Image
        ↓
Push Image to Amazon ECR
        ↓
Deploy Image to EC2
        ↓
Run Docker Container
        ↓
Application Health Verification
        ↓
Email Notification
2. Application Setup
2.1 Clone the Application Repository

The application source code was cloned from GitHub.

The repository contains the Flask application, Python dependencies, tests, and application configuration.

What was done:

Cloned the GitHub repository.
Reviewed the application structure.
Prepared the application for containerization.

Screenshot: Git Clone

![alt text](<1.) Git Clone.png>)

2.2 Install Application Requirements

The Python dependencies required by the Flask application were downloaded using requirements.txt.

What was done:

Installed the required Python packages.
Verified that the application dependencies were available.
The same requirements.txt is later used by the CI/CD pipeline.

Screenshot: Requirements downloaded

2.3 Create MongoDB Cluster

MongoDB was configured as the database backend for the Student Registration Application.

What was done:

Created the MongoDB cluster.
Configured the database environment.
Prepared the MongoDB connection for the Flask application.

Screenshot: Cluster created

2.4 Configure and Run the Application

The Flask application was configured to communicate with MongoDB and then started.

What was changed:

Updated the application configuration to use the MongoDB connection.
Configured the required application environment values.
Started the Flask application.

Screenshot: Application running

2.5 Verify Data Storage in MongoDB

The application was tested by submitting data and verifying that the values were stored in MongoDB.

What was verified:

Flask successfully connected to MongoDB.
Application data was successfully inserted.
MongoDB was confirmed as the application's backend database.

Screenshot: Values stored in MongoDB

2.6 Verify MongoDB Health

The MongoDB cluster and its nodes were checked to verify that the database infrastructure was available.

Screenshot: Health nodes

2.7 Run Application Tests

The application test suite was executed before containerization.

What was done:

Executed the pytest test suite.
Verified that the tests passed successfully.
Confirmed that the application was ready for Dockerization.

Screenshot: Test Passed

3. Dockerization
3.1 Create .dockerignore

A .dockerignore file was created to prevent unnecessary files from being included in the Docker build context.

What was changed:

Created the .dockerignore file.
Excluded unnecessary files/directories from the Docker build.

Screenshot: Created Docker ignore file

3.2 Create Dockerfile

A Dockerfile was created to define how the Flask application would be packaged into a Docker image.

What was created:

Defined the Python base image.
Added application files.
Installed Python dependencies.
Defined the application startup command.

Screenshot: Dockerfile created

3.3 Build Docker Image

The Docker image was built from the Dockerfile.

What was done:

Built the Flask application into a Docker image.
Verified successful image creation.
Prepared the image for container testing and ECR deployment.

Screenshot: Docker image created

3.4 Test Docker Container

The Docker image was run as a container to verify that the application worked correctly inside Docker.

What was verified:

Docker container started successfully.
Flask application started successfully.
Application was accessible through the configured port.

Screenshot: Checking docker container working

4. Push Application to GitHub

The application and Docker configuration were pushed to GitHub.

What was updated:

Application source code.
Dockerfile.
.dockerignore.
Tests.
Supporting configuration.

Screenshot: Push to Github

5. Create GitHub Actions Workflow

A GitHub Actions workflow was created to automate the CI/CD process.

What was created/updated:

Created the CI/CD workflow YAML file.
Added the required pipeline stages.
Configured the workflow to trigger automatically when code is pushed to the main branch.

The workflow follows this order:

Checkout
   ↓
Install Dependencies
   ↓
Test
   ↓
Build
   ↓
Push to ECR
   ↓
Deploy to EC2
   ↓
Verify Deployment
   ↓
Notify

Screenshot: Create workflow

6. Configure GitHub Secrets

Sensitive values required by the pipeline were stored using GitHub Secrets.

What was configured:

AWS credentials.
SMTP credentials.
Required deployment credentials/configuration.

Sensitive credentials were not hardcoded in the workflow file.

Screenshot: Secrets created

7. Configure Docker in GitHub Actions

Docker functionality was configured in GitHub Actions.

What was done:

Enabled Docker operations in the workflow.
Verified Docker was available on the GitHub Actions runner.
Prepared the workflow to build Docker images.

Screenshot: Docker working on GitHub actions

8. Create Amazon ECR Repository

An Amazon Elastic Container Registry repository was created to store Docker images.

Repository:

cicd-git-repo

Region:

us-east-1

Screenshot: ECR repo created

9. Configure AWS Authentication

AWS credentials were configured so that GitHub Actions could communicate with AWS.

What was configured:

AWS access credentials were added to GitHub Secrets.
GitHub Actions was granted the required AWS permissions.
ECR operations were enabled from the pipeline.

Screenshot: AWS secret access key created in Github

10. Build Docker Image with Git Commit SHA

The workflow was updated so that Docker images are tagged using the Git commit SHA.

Instead of deploying only an ambiguous latest tag, each image receives a unique tag corresponding to the source-code commit.

Example:

df9fd9efff7372c08abe4275cb4bb87cdec0c68a

This provides traceability between:

Git Commit
    ↓
Docker Image
    ↓
ECR Image
    ↓
EC2 Deployment

What was changed:

Updated the Docker build stage.
Added Git commit SHA as the Docker image tag.
Updated the ECR push stage to use the same tag.

Screenshot: Successful pipeline for docker image push to ECR

11. Verify Docker Image in ECR

The Docker image pushed by GitHub Actions was verified in Amazon ECR.

What was verified:

Image exists in the cicd-git-repo repository.
Commit SHA tag is present.
Image is available for deployment.

Screenshot: Image on ECR using GitHub actions

12. Create EC2 Deployment Target

An EC2 instance was created to host the Dockerized Flask application.

The EC2 instance acts as the deployment target for the CI/CD pipeline.

Screenshot: EC2 Created

13. Install Docker on EC2

Docker was installed and enabled on the EC2 instance.

What was configured:

Installed Docker.
Enabled Docker service.
Verified that Docker was available to run containers.

Screenshot: Docker successfully installed and enabled

14. Configure IAM Permissions

IAM permissions were configured for the deployment process.

What was changed:

Added the required permissions.
Allowed the deployment process to interact with AWS services.
Enabled required ECR/SSM operations.

Screenshot: Role added to iam user

15. Deploy Docker Image to EC2
15.1 Pull Image from ECR

The Docker image generated by GitHub Actions was pulled onto EC2.

What was done:

Connected to the EC2 instance.
Authenticated Docker with Amazon ECR.
Pulled the commit-specific Docker image.
Verified that the image was available on EC2.

Screenshot: Docker image pull on EC2

15.2 Configure .env File

The application environment variables were provided through a .env file on EC2.

The .env file contains the application's required configuration, such as:

MONGO_URI
SECRET_KEY

The .env file is kept on the EC2 instance and is not hardcoded into the Docker image.

The container is started using:

--env-file .env

This allows the same Docker image to be deployed without embedding environment-specific secrets inside the image.

15.3 Authenticate Docker with ECR

Docker on EC2 was authenticated against the ECR registry.

The ECR login command was used to obtain temporary authentication for the registry.

What was verified:

ECR authentication succeeded.
EC2 could access the private ECR repository.

Screenshot: Login success

15.4 Run the Docker Container

The Docker container was started using the commit-specific image pulled from ECR.

Example deployment command:

sudo docker run -d \
  --name flask-student-container \
  -p 5000:5000 \
  --env-file .env \
  444068947659.dkr.ecr.us-east-1.amazonaws.com/cicd-git-repo:<commit-sha>
Port Mapping

The following mapping was used:

-p 5000:5000

This means:

EC2 Port 5000
      ↓
Container Port 5000
      ↓
Flask Application Port 5000

What was done:

Started the Docker container.
Passed the .env configuration.
Mapped port 5000.
Started the Flask application inside the container.
16. Verify Deployment
16.1 Verify Docker Container

The running container was checked using:

sudo docker ps

The output confirmed that the container was running and that port 5000 was mapped.

Screenshot: Docker container running on EC2

16.2 Verify Application Health

The deployed application was verified using a curl request.

The health/application endpoint was accessed from the EC2 instance to ensure that the application was actually responding.

What was verified:

Container is running.
Flask process is running.
Application responds to HTTP requests.
Deployment is operational.

Screenshot: Health Curl status

This is important because a Docker container can technically start and then immediately crash. Therefore, checking the actual application response provides a proper deployment verification gate.

16.3 Access Application from Browser

After verifying the container and application response, the application was accessed using the EC2 public IP and port 5000.

Example:

http://<EC2-Public-IP>:5000

The Student Registration System was successfully displayed.

Screenshot: Application successfully running on EC2

17. Email Notification
17.1 Configure SMTP

SMTP settings were stored in GitHub Secrets rather than being hardcoded into the workflow.

The configured values were:

MAIL_SERVER
MAIL_PORT
MAIL_USERNAME
MAIL_PASSWORD
MAIL_TO

For Gmail, an App Password was used instead of the normal Gmail password.

17.2 Update Email Notification Code

The GitHub Actions workflow was updated to send an email after the pipeline execution.

What was changed:

Added the email notification action.
Connected SMTP credentials through GitHub Secrets.
Added customized success and failure messages.
Included actual build/deployment information in the notification.

The success email confirms that the deployment completed successfully.

Screenshot: Successful email notification

18. Final CI/CD Pipeline

The final GitHub Actions pipeline implements the required stages in order.

18.1 Checkout

Pulls the latest source code from the main branch.

18.2 Install Dependencies

Installs Python dependencies from:

requirements.txt
18.3 Test

Runs the pytest test suite.

If a test fails, the pipeline stops and does not continue to Docker build or deployment.

18.4 Build

Builds the Docker image and tags it using the Git commit SHA.

18.5 Push to ECR

Authenticates with Amazon ECR and pushes the commit-specific image.

18.6 Deploy to EC2

The deployment process:

Connects to EC2.
Authenticates with ECR.
Pulls the new image.
Stops the existing container.
Removes the existing container.
Starts the new container.
Uses the .env configuration.
Maps port 5000.
18.7 Deployment Verification

The application is checked after deployment using the application/health endpoint.

The deployment is considered successful only when the application actually responds successfully.

18.8 Notify

An email is sent containing the deployment result and relevant build details.

19. Automatic Deployment Trigger

The workflow is configured to automatically execute whenever code is pushed to the main branch.

The final automated flow is:

Git Push
   ↓
GitHub
   ↓
GitHub Actions
   ↓
Checkout
   ↓
Install Dependencies
   ↓
Pytest
   ↓
Docker Build
   ↓
ECR Push
   ↓
EC2 Deployment
   ↓
Container Restart
   ↓
Health Check
   ↓
Email Notification

Therefore, after the initial infrastructure configuration, the Docker image does not need to be manually built, pushed to ECR, pulled on EC2, and started for every code change.

The GitHub Actions pipeline automates that entire process.

20. Deployment Architecture
                  ┌─────────────────────┐
                  │   GitHub Repository  │
                  └──────────┬──────────┘
                             │
                         git push
                             │
                             ▼
                  ┌─────────────────────┐
                  │   GitHub Actions    │
                  │                     │
                  │ Checkout            │
                  │ Install Dependencies│
                  │ Test                │
                  │ Docker Build        │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │    Amazon ECR       │
                  │                     │
                  │ cicd-git-repo       │
                  │                     │
                  │ <commit-sha>        │
                  └──────────┬──────────┘
                             │
                       Pull Image
                             │
                             ▼
                  ┌─────────────────────┐
                  │      EC2            │
                  │                     │
                  │ Docker Container    │
                  │ Flask Application   │
                  │ Port 5000           │
                  └──────────┬──────────┘
                             │
                         Health Check
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Email Notification  │
                  └─────────────────────┘

This completes the end-to-end GitHub → GitHub Actions → ECR → EC2 → Docker → Application → Verification → Email deployment workflow.