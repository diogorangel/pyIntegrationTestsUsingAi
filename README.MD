

# Directory Data Service – Integration Tests
Author : Diogo Rangel Dos Santos (diogorangel)
CSE270 class BYU

This project contains integration tests for the /users endpoint of the Directory Data Service.

The tests verify the service's behavior for different username and password combinations, validating the returned HTTP codes.

📌 Tested Endpoint
GET http://127.0.0.1:8000/users/

Query Parameters
Parameter Type Description
username string Username
password string User password
🧪 Implemented Tests
✅ Test 1 – Invalid Password

Request:

/users/?username=admin&password=qwerty

Validation:

Expects HTTP 200

Empty response

✅ Test 2 – Incorrect Password Expected as Unauthorized

Request:

/users/?username=admin&password=admin

Validation:

Expects HTTP 401

Empty response

📂 Project Structure
project-root/
│
├── tests/
│ └── test_users_integration.py
│
├── integration_test.log
└── README.md

⚙️ Requirements

Python 3.8+

pytest

requests

Install the dependencies:

pip install pytest requests

▶ How to Run the Tests

Make sure the Directory Data Service is running at:

http://127.0.0.1:8000

Then run:

pytest -v -s

Parameters used:

-v → verbose (shows test details)

-s → displays logs in the console

📝 Logging

The tests generate logs in two locations:

1️⃣ Console

Displayed during the execution of pytest.

2️⃣ File
integration_test.log

Example of generated log:

2026-02-11 11:02:12,321 - INFO - Sending request to http://127.0.0.1:8000/users/ with params {'username': 'admin', 'password': 'qwerty'}
2026-02-11 11:02:12,328 - INFO - Received response status: 200

This allows you to:

Confirm that the service was called

Verify the returned status

Audit test executions

🔎 How to Verify if the Service Was Called

After running the tests:

Check the terminal where the service is running

You should see two GET requests to /users

This confirms that the tests actually executed real calls to the service.

🚀 Applied Best Practices

Use of real integration tests (not mocks)

Explicit HTTP status validation

Structured logging

Prevention of duplicate log handlers

CI/CD compatible

📌 Note

These tests are integration tests, therefore:

They depend on the service being active

They do not use mocks

They test real endpoint behavior