import pytest
from app import app, mongo
from bson.objectid import ObjectId


TEST_DB = "test_student_db"


@pytest.fixture
def client():
    app.config["TESTING"] = True

    client = app.test_client()

    # Use a separate test database on MongoDB Atlas
    test_db = mongo.cx[TEST_DB]

    # Clean the test collection before each test
    test_db.students.delete_many({})

    # Insert test student
    test_db.students.insert_one({
        "_id": ObjectId("66fddff25f4b5f6a0a123456"),
        "name": "Test Student",
        "email": "test@student.com",
        "course": "Flask"
    })

    yield client

    # Clean up test documents after each test
    test_db.students.delete_many({})


def test_home_page(client):
    """Test if home page loads correctly."""
    response = client.get("/")

    assert response.status_code == 200
    assert b"Test Student" in response.data


def test_add_student(client):
    """Test adding a new student."""
    data = {
        "name": "New User",
        "email": "new@user.com",
        "course": "Python"
    }

    response = client.post(
        "/add",
        data=data,
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"New User" in response.data


def test_update_student(client):
    """Test updating a student."""
    student_id = "66fddff25f4b5f6a0a123456"

    data = {
        "name": "Updated Name",
        "email": "updated@student.com",
        "course": "Updated Course"
    }

    response = client.post(
        f"/update/{student_id}",
        data=data,
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Updated Name" in response.data


def test_delete_student(client):
    """Test deleting a student."""

    test_db = mongo.cx[TEST_DB]

    student_id = test_db.students.insert_one({
        "name": "Temp User",
        "email": "temp@user.com",
        "course": "Temp Course"
    }).inserted_id

    response = client.get(
        f"/delete/{student_id}",
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Temp User" not in response.data

def test_health():

    """Test health endpoint."""
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
    assert response.json["database"] == "connected"
