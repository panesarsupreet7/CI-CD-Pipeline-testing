# CI/CD Deployment – Flask Student Registration Application

## Step 1 – Clone the Application Repository

The Flask Student Registration application source code was cloned from the GitHub repository to begin the deployment and CI/CD implementation.

**Evidence – `1.) Git Clone.png`**

![Git Clone](./screenshots/1.%29%20Git%20Clone.png)

---

## Step 2 – Install Python Dependencies

The application's required Python packages were installed from the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

This ensured that all dependencies required by the Flask application were available before testing and containerization.

**Evidence – `2.) Requirements downloaded.png`**

![Requirements downloaded](./screenshots/2.%29%20Requirements%20downloaded.png)

---

## Step 3 – Create the MongoDB Cluster

A MongoDB cluster was created to provide the database backend required by the Flask Student Registration application.

**Evidence – `3.)Cluster created.png`**

![Cluster created](./screenshots/3.%29Cluster%20created.png)

---

## Step 4 – Run the Application

The Flask Student Registration application was started and verified to ensure that the application was functioning before containerization.

**Evidence – `4.)Application running.png`**

![Application running](./screenshots/4.%29Application%20running.png)

---

## Step 5 – Verify Data Storage in MongoDB

Application data was submitted through the Student Registration application and verified in MongoDB.

This confirmed that the Flask application was successfully communicating with the MongoDB database and storing application data.

**Evidence – `5.) Values stored in MongoDB.png`**

![Values stored in MongoDB](./screenshots/5.%29%20Values%20stored%20in%20MongoDB.png)

---

## Step 6 – Verify MongoDB Cluster Health

The MongoDB cluster health and available nodes were checked to confirm that the database infrastructure was operational.

**Evidence – `6.) Health nodes.png`**

![Health nodes](./screenshots/6.%29%20Health%20nodes.png)

---

## Step 7 – Run the Application Test Suite

The application test suite was executed using `pytest`.

```bash
pytest
```

The tests completed successfully.

Testing was also incorporated into the CI/CD pipeline as a mandatory gate. If the test stage fails, the pipeline stops and does not continue to the Docker build, ECR push, or EC2 deployment stages.

**Evidence – `7.)Test Passed.png`**

![Test Passed](./screenshots/7.%29Test%20Passed.png)

---

## Step 8 – Create the Docker Ignore Configuration

A `.dockerignore` file was created to prevent unnecessary files and directories from being included in the Docker build context.

**Evidence – `8.)Created Docker ignore file.png`**

![Created Docker ignore file](./screenshots/8.%29Created%20Docker%20ignore%20file.png)

---

## Step 9 – Create the Dockerfile

A Dockerfile was created to containerize the Flask application.

The Dockerfile defines the application environment, dependencies, application files, exposed application port, and command used to start the Flask application.

**Evidence – `9.)Dockerfile created.png`**

![Dockerfile created](./screenshots/9.%29Dockerfile%20created.png)

---

## Step 10 – Build the Docker Image

The Flask application was successfully packaged into a Docker image.

The Docker image was built locally before integrating the Docker build process into GitHub Actions.

**Evidence – `10.)Docker image created.png`**

![Docker image created](./screenshots/10.%29Docker%20image%20created.png)

---

## Step 11 – Verify the Docker Container

The Docker image was used to start a container locally.

The container was checked to confirm that the Flask application was running correctly inside Docker.

**Evidence – `11.)Checking docker container working.png`**

![Checking docker container working](./screenshots/11.%29Checking%20docker%20container%20working.png)

---

## Step 12 – Push the Application Source Code to GitHub

The application source code, Dockerfile, `.dockerignore`, test files, and related configuration were committed and pushed to the GitHub repository.

GitHub was established as the source repository for the CI/CD pipeline.

**Evidence – `12.)Push to Github.png`**

![Push to Github](./screenshots/12.%29Push%20to%20Github.png)

---

## Step 13 – Create the GitHub Actions Workflow

A GitHub Actions workflow was created to automate the application build and deployment process.

The workflow was designed to execute the required stages in sequence:

```text
Checkout
    ↓
Install Dependencies
    ↓
Test
    ↓
Docker Build
    ↓
Push to Amazon ECR
    ↓
Deploy to EC2
    ↓
Application Verification
    ↓
Email Notification
```

**Evidence – `13.)Create workflow.png`**

![Create workflow](./screenshots/13.%29Create%20workflow.png)

---

## Step 14 – Configure GitHub Repository Secrets

Sensitive configuration values required by the CI/CD pipeline were stored as GitHub repository secrets instead of being hardcoded in the workflow.

The secrets configuration covers AWS authentication, deployment access, and SMTP email notification.

**Evidence – `14.)Secrets created.png`**

![Secrets created](./screenshots/14.%29Secrets%20created.png)

---

## Step 15 – Configure Docker for GitHub Actions

Docker was configured and verified on the GitHub Actions runner.

This allows the CI/CD workflow to automatically build Docker images during pipeline execution.

**Evidence – `15.)Docker working on GitHub actions.png`**

![Docker working on GitHub actions](./screenshots/15.%29Docker%20working%20on%20GitHub%20actions.png)

---

## Step 16 – Create the Amazon ECR Repository

An Amazon Elastic Container Registry repository was created to store the Docker images produced by GitHub Actions.

```text
Repository: cicd-git-repo
Region: us-east-1
```

Amazon ECR acts as the image registry between the GitHub Actions pipeline and the EC2 deployment environment.

**Evidence – `16.)ECR repo created.png`**

![ECR repo created](./screenshots/16.%29ECR%20repo%20created.png)

---

## Step 17 – Configure AWS Credentials in GitHub

AWS credentials required by GitHub Actions were configured as GitHub repository secrets.

The credentials allow the workflow to authenticate with AWS and perform the required ECR and EC2 deployment operations.

AWS credentials were not hardcoded in the workflow file.

**Evidence – `17.)AWS secret access key created in Github.png`**

![AWS secret access key created in Github](./screenshots/17.%29AWS%20secret%20access%20key%20created%20in%20Github.png)

---

## Step 18 – Build and Push the Docker Image to ECR

The GitHub Actions pipeline was executed successfully.

The pipeline built the Docker image and pushed it to the Amazon ECR repository.

The image was tagged using the Git commit SHA so that every image can be traced back to the exact source-code commit that produced it.

Example:

```text
df9fd9efff7372c08abe4275cb4bb87cdec0c68a
```

This avoids relying only on the `latest` tag and provides deployment traceability.

**Evidence – `18.)Successful pipeline for docker image push to ECR.png`**

![Successful pipeline for docker image push to ECR](./screenshots/18.%29Successful%20pipeline%20for%20docker%20image%20push%20to%20ECR.png)

---

## Step 19 – Verify the Docker Image in ECR

The Docker image pushed by GitHub Actions was verified in Amazon ECR.

The image was available in the `cicd-git-repo` repository using the Git commit SHA as its image tag.

Example image format:

```text
444068947659.dkr.ecr.us-east-1.amazonaws.com/cicd-git-repo:<commit-sha>
```

**Evidence – `19.)Image on ECR using GitHub actions.png`**

![Image on ECR using GitHub actions](./screenshots/19.%29Image%20on%20ECR%20using%20GitHub%20actions.png)

---

## Step 20 – Create the EC2 Deployment Instance

An EC2 instance was created to host the Dockerized Flask Student Registration application.

The EC2 instance acts as the deployment target for the CI/CD pipeline.

**Evidence – `20.)EC2 Created.png`**

![EC2 Created](./screenshots/20.%29EC2%20Created.png)

---

## Step 21 – Install and Enable Docker on EC2

Docker was successfully installed and enabled on the EC2 instance.

Docker is required on EC2 to pull the application image from Amazon ECR and run the application container.

**Evidence – `21.)Docker successfully installed and enabled.png`**

![Docker successfully installed and enabled](./screenshots/21.%29Docker%20successfully%20installed%20and%20enabled.png)

---

## Step 22 – Configure IAM Permissions for Deployment

The required IAM permissions were configured for the deployment process.

The permissions allow the deployment identity to perform the required AWS operations, including communicating with the EC2 instance through AWS Systems Manager and interacting with Amazon ECR.

This configuration supports the automated EC2 deployment performed by GitHub Actions.

**Evidence – `22.)Role added to iam user.png`**

![Role added to iam user](./screenshots/22.%29Role%20added%20to%20iam%20user.png)

---

## Step 23 – Authenticate EC2 with Amazon ECR

The EC2 instance was authenticated with the Amazon ECR registry so that Docker could pull the private application image.

The ECR authentication was successfully completed.

The authentication command used the AWS ECR login password rather than storing an ECR password manually.

**Evidence – `23.)Login success.png`**

![Login success](./screenshots/23.%29Login%20success.png)

---

## Step 24 – Pull the Docker Image from ECR onto EC2

The Docker image produced by the GitHub Actions pipeline was pulled from Amazon ECR onto the EC2 instance.

The deployment uses the commit-specific image tag rather than an untraceable image version.

Example:

```text
444068947659.dkr.ecr.us-east-1.amazonaws.com/cicd-git-repo:df9fd9efff7372c08abe4275cb4bb87cdec0c68a
```

**Evidence – `24.)Docker image pull on EC2.png`**

![Docker image pull on EC2](./screenshots/24.%29Docker%20image%20pull%20on%20EC2.png)

---

## Step 25 – Verify the Application Health

After starting the application container, the application was verified using `curl`.

The application was checked from the EC2 instance to confirm that the application itself was responding.

Example:

```bash
curl http://localhost:5000/
```

Where the application exposes a `/health` endpoint, the deployment verification can be performed using:

```bash
curl http://localhost:5000/health
```

This verification acts as the deployment verification gate. A container that starts but crashes immediately or fails to respond is treated as a failed deployment.

**Evidence – `25.)Health Curl status.png`**

![Health Curl status](./screenshots/25.%29Health%20Curl%20status.png)

---

## Step 26 – Perform Application Testing After Deployment

The deployed application was tested after the EC2 deployment to confirm that the Flask application was accessible and functioning correctly.

This provided functional verification after the Docker deployment.

**Evidence – `26.)Sucessful application testing.png`**

![Sucessful application testing](./screenshots/26.%29Sucessful%20application%20testing.png)

---

## Step 27 – Run the Flask Application on EC2

The Flask Student Registration application was successfully deployed and was running inside a Docker container on EC2.

The application port was mapped using:

```bash
-p 5000:5000
```

The mapping connects the EC2 host port to the Docker container port:

```text
EC2 Port 5000
      ↓
Container Port 5000
      ↓
Flask Application
```

The application can therefore be accessed using:

```text
http://<EC2-Public-IP>:5000
```

**Evidence – `27.)Application successfully running on EC2.png`**

![Application successfully running on EC2](./screenshots/27.%29Application%20successfully%20running%20on%20EC2.png)

---

## Step 28 – Configure Deployment Email Notification

Email notification was implemented as the final stage of the CI/CD workflow.

SMTP configuration was stored securely using GitHub Secrets.

The following variables were configured:

```text
MAIL_SERVER
MAIL_PORT
MAIL_USERNAME
MAIL_PASSWORD
MAIL_TO
```

For Gmail SMTP authentication, an application-specific App Password was used instead of the normal Gmail account password.

The notification was configured to report the deployment outcome.

### Success Notification

The successful deployment email includes:

- Success status
- Git commit SHA
- Branch
- Docker image tag
- EC2 deployment target
- Pipeline run information

### Failure Notification

The failure notification includes:

- Failure status
- Failed deployment stage
- Git commit SHA
- Branch
- Pipeline/log information for troubleshooting

Email credentials are not hardcoded in the workflow.

**Evidence – `28.)Sucessful email notification.png`**

![Sucessful email notification](./screenshots/28.%29Sucessful%20email%20notification.png)

---

## Step 29 – Configure Automatic Deployment Trigger

The GitHub Actions workflow was configured to automatically start whenever changes are pushed to the `main` branch.

The workflow trigger is configured as:

```yaml
on:
  push:
    branches:
      - main
```

This means that after the initial infrastructure configuration, the Docker image does not need to be manually built and pushed to ECR for every code change.

The pipeline automatically performs the build and deployment process.

---

## Step 30 – Implement the Complete CI/CD Deployment Flow

The completed GitHub Actions pipeline performs the deployment stages in the required order.

```text
Git Push to main
        ↓
Checkout
        ↓
Install Dependencies
        ↓
Pytest
        ↓
Docker Build
        ↓
Tag Image with Git Commit SHA
        ↓
Authenticate with Amazon ECR
        ↓
Push Image to ECR
        ↓
Deploy to EC2 using SSM
        ↓
Pull New Image from ECR
        ↓
Stop Existing Container
        ↓
Remove Existing Container
        ↓
Run New Container
        ↓
Map Application Port
        ↓
Application Health Check
        ↓
Email Notification
```

The test stage acts as a deployment gate:

```text
Pytest
  |
  ├── FAIL → Pipeline stops
  |
  └── PASS → Docker Build → ECR Push → EC2 Deployment
```

The Docker image is tagged using the Git commit SHA, allowing the deployed image to be traced back to its source-code version.

---

## Step 31 – Final Deployment and Testing Result

The complete CI/CD deployment was successfully implemented and verified.

### Final Deployment Flow

```text
GitHub Repository
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
Amazon ECR
        ↓
EC2
        ↓
Docker Container
        ↓
Flask Application
        ↓
Health Check
        ↓
Email Notification
```

### Final Testing Results

| Validation | Result |
|---|---|
| Application setup | Passed |
| MongoDB cluster creation | Passed |
| MongoDB connectivity | Passed |
| Application data storage | Passed |
| MongoDB health verification | Passed |
| Pytest suite | Passed |
| Docker image build | Passed |
| Local Docker container test | Passed |
| GitHub repository push | Passed |
| GitHub Actions workflow | Passed |
| Amazon ECR repository | Created |
| Docker image pushed to ECR | Passed |
| EC2 instance creation | Completed |
| Docker installation on EC2 | Passed |
| IAM configuration | Completed |
| ECR authentication from EC2 | Passed |
| Docker image pull on EC2 | Passed |
| Application health check | Passed |
| Post-deployment application testing | Passed |
| Application running on EC2 | Passed |
| Email notification | Passed |

### Final Outcome

The Flask Student Registration application was successfully containerized, stored in Amazon ECR, deployed to EC2, verified after deployment, and integrated with automated email notification.

The final CI/CD implementation removes the need to manually repeat the Docker build, ECR push, EC2 image pull, and container restart process for every code change.

A push to the `main` branch now initiates the automated deployment workflow.