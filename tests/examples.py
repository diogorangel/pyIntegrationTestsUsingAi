import random
import psycopg2
import logging

# Configure logger
logger = logging.getLogger("examples")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler("test_execution.log")
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


some_list = ['alpha','beta','gamma','delta']


def find_and_replace(some_list, find, replace):
    logger.info(f"Attempting to replace '{find}' with '{replace}'")
    some_list[some_list.index(find)] = replace
    logger.info(f"Replacement successful")


def get_random_item():
    choice = random.choice(some_list)
    logger.info(f"Random choice selected: {choice}")
    return choice


def gather_input(prompt):
    logger.info(f"Prompting user with: {prompt}")
    return input(prompt)


def get_data_from_file(filename):
    logger.info(f"Reading from file: {filename}")
    contents = ""
    with open(filename) as myfile:
        contents += myfile.readline()
    logger.info(f"Read contents: {contents}")
    return contents


def get_user_id_1():
    logger.info("Connecting to PostgreSQL database")

    conn = psycopg2.connect(
        dbname="mydb",
        user="username",
        password="password",
        host="127.0.0.1",
        port="5432"
    )

    cur = conn.cursor()

    try:
        logger.info("Executing query for user ID 1")
        cur.execute("SELECT * FROM USERS WHERE ID=1")
        user = cur.fetchone()
        conn.commit()
        logger.info(f"User fetched: {user}")
        return user

    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(f"Error fetching user: {error}")
        conn.rollback()

    finally:
        logger.info("Closing cursor and connection")
        cur.close()
        conn.close()
