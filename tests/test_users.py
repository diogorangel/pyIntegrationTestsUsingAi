import requests
import logging

BASE_URL = "http://127.0.0.1:8000/users/"

# Create logger
logger = logging.getLogger("integration_tests")
logger.setLevel(logging.INFO)

# Prevent duplicate handlers if pytest reloads module
if not logger.handlers:

    # File handler
    file_handler = logging.FileHandler("integration_test.log")
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def test_users_invalid_password():
    """
    Test 1:
    username=admin & password=qwerty
    Expect HTTP 200
    """
    params = {"username": "admin", "password": "qwerty"}

    logger.info(f"Sending request to {BASE_URL} with params {params}")
    response = requests.get(BASE_URL, params=params)
    logger.info(f"Received response status: {response.status_code}")

    assert response.status_code == 200
    assert response.text == ""


def test_users_valid_password():
    """
    Test 2:
    username=admin & password=admin
    Expect HTTP 401
    """
    params = {"username": "admin", "password": "admin"}

    logger.info(f"Sending request to {BASE_URL} with params {params}")
    response = requests.get(BASE_URL, params=params)
    logger.info(f"Received response status: {response.status_code}")

    assert response.status_code == 401
    assert response.text == ""
