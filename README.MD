

# Directory Data Service – Integration Tests
Author : Diogo Rangel Dos Santos (diogorangel)
CSE270 class BYU

# 📌 Overview

This assignment focuses on writing unit tests for the build_sentences.py module using pytest and coverage.py.

The goal is to test all functions in the module except:

The main() function

The call to main()

Your final coverage report should show that all lines are covered except lines 106–110 and line 113.

# 🧪 What Is Being Tested

The following functions from build_sentences.py are tested:

get_seven_letter_word()

parse_json_from_file()

choose_sentence_structure()

get_pronoun()

get_article()

get_word()

fix_agreement()

build_sentence()

The main() function is intentionally NOT tested.

🛠 Testing Techniques Used

This assignment applies multiple pytest testing concepts:

# ✅ 1. Testing Functions That Read From Console

We mock the input() function:

mocker.patch("builtins.input", return_value="testing")


This allows automatic testing without manual user input.

# ✅ 2. Testing File Reading

We use the built-in tmp_path fixture:

def test_parse_json_from_file(tmp_path):


This safely creates a temporary JSON file during the test.

# ✅ 3. Testing Random Outcomes

Two approaches are used:

✔ Testing that result is within expected range
✔ Mocking random.choice() for predictable behavior

Example:

mocker.patch("random.choice", return_value=structures[0])

# ✅ 4. Testing ASCII-Based Word Selection

The get_word() function uses ASCII indexing:

result = get_word("A", words)


This verifies that the ordinal logic works correctly.

# ✅ 5. Testing Agreement Logic

The fix_agreement() function is tested to ensure it handles verb agreement logic properly.

# ✅ 6. Testing Sentence Construction

The build_sentence() function is tested using:

A full valid data dictionary

A valid seed word

Mocked random selections

We verify:

The result is a string

The sentence ends with a period

The sentence is not empty

# 📦 Requirements

Install required packages:

Windows
pip install pytest pytest-mock coverage

Mac/Linux
pip3 install pytest pytest-mock coverage

▶ Running the Tests

From the project root:

pytest -v

# 📊 Running Coverage

Navigate to the tests directory:

cd tests


Run coverage:

coverage run -m pytest test_build_sentences.py
coverage report -m

# ✅ Expected Coverage Output

Your report should show something similar to:

Name                  Stmts   Miss  Cover  Missing
---------------------------------------------------
build_sentences.py     XXX     6     95%   106-110,113


Only these lines should be missing:

Lines 106–110 → main() function

Line 113 → call to main()

All other lines must be covered.

# 🎯 Assignment Compliance

This project satisfies the assignment requirements:

✔ All functions tested except main()
✔ Mocking used where required
✔ File reading tested using tmp_path
✔ Random behavior tested properly
✔ All code paths covered
✔ Coverage report demonstrates correct exclusions

# 📚 Concepts Demonstrated

Unit testing with pytest

Mocking with pytest-mock

Testing side effects

Testing raised exceptions

Testing console input

Testing file I/O

Testing random outcomes

Code coverage analysis

# 🚀 Final Result

All required functions are fully tested and verified.

Coverage confirms that every executable line is tested except the intentionally excluded main() function and its invocation.

This project contains integration tests for the /users endpoint of the Directory Data Service.

The tests verify the service's behavior for different username and password combinations, validating the returned HTTP codes.

# 📌 Tested Endpoint
GET http://127.0.0.1:8000/users/

# Query Parameters
Parameter Type Description
username string Username
password string User password
🧪 Implemented Tests
✅ Test 1 – Invalid Password

# Request:

/users/?username=admin&password=qwerty

Validation:

Expects HTTP 200

Empty response

# ✅ Test 2 – Incorrect Password Expected as Unauthorized

Request:

/users/?username=admin&password=admin

# Validation:

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

# 📝 Logging

The tests generate logs in two locations:

# 1️⃣ Console

Displayed during the execution of pytest.

# 2️⃣ File
integration_test.log

Example of generated log:

2026-02-11 11:02:12,321 - INFO - Sending request to http://127.0.0.1:8000/users/ with params {'username': 'admin', 'password': 'qwerty'}
2026-02-11 11:02:12,328 - INFO - Received response status: 200

This allows you to:

Confirm that the service was called

Verify the returned status

Audit test executions

# 🔎 How to Verify if the Service Was Called

After running the tests:

Check the terminal where the service is running

You should see two GET requests to /users

This confirms that the tests actually executed real calls to the service.

# 🚀 Applied Best Practices

Use of real integration tests (not mocks)

Explicit HTTP status validation

Structured logging

Prevention of duplicate log handlers

CI/CD compatible

# 📌 Note

These tests are integration tests, therefore:

They depend on the service being active

They do not use mocks

They test real endpoint behavior