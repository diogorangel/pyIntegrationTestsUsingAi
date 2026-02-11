import pytest
import logging

from examples import (
    find_and_replace,
    get_random_item,
    gather_input,
    get_data_from_file,
    get_user_id_1,
    some_list
)

# Configure logger for tests
logger = logging.getLogger("tests")
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


def test_find_and_replace():
    logger.info("Running test_find_and_replace")
    mylist = ['apples','oranges']
    find_and_replace(mylist, 'apples', 'bananas')
    assert mylist[0] == 'bananas'


def test_find_and_replace_error():
    logger.info("Running test_find_and_replace_error")
    mylist = ['apples','oranges']
    with pytest.raises(ValueError):
        find_and_replace(mylist, 'bananas', 'pears')


def test_get_random_item_no_mock():
    logger.info("Running test_get_random_item_no_mock")
    choice = get_random_item()
    assert choice in some_list


def test_get_random_item(mocker):
    logger.info("Running test_get_random_item with mock")
    mock_choice = mocker.patch("random.choice", return_value="alpha")
    assert get_random_item() == 'alpha'
    mock_choice.assert_called_once()


def test_gather_input(mocker):
    logger.info("Running test_gather_input")
    mock_input = mocker.patch("builtins.input", return_value="Test input")
    result = gather_input("Enter input: ")
    assert result == "Test input"
    mock_input.assert_called_once_with("Enter input: ")


def test_get_data_from_file(tmp_path):
    logger.info("Running test_get_data_from_file with tmp_path")
    test_data = "file contents"
    file_path = tmp_path / "test.txt"
    with open(file_path, "w") as f:
        f.write(test_data)

    result = get_data_from_file(file_path)
    assert result == test_data


def test_get_data_from_file_mock(mocker):
    logger.info("Running test_get_data_from_file with mock")
    mock_open = mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data="file contents")
    )

    result = get_data_from_file("test.txt")
    assert result == "file contents"
    mock_open.assert_called_once_with("test.txt")


@pytest.fixture
def mock_psycopg2_connect(mocker):
    logger.info("Setting up mock for psycopg2.connect")
    return mocker.patch('psycopg2.connect')


def test_get_user_id_1(mock_psycopg2_connect):
    logger.info("Running test_get_user_id_1 with mock")

    mock_connect = mock_psycopg2_connect.return_value
    mock_cursor = mock_connect.cursor.return_value
    mock_cursor.fetchone.return_value = 'test_user'

    user = get_user_id_1()

    assert user == 'test_user'

    mock_psycopg2_connect.assert_called_once_with(
        dbname="mydb",
        user="username",
        password="password",
        host="127.0.0.1",
        port="5432"
    )

    mock_cursor.execute.assert_called_once_with(
        "SELECT * FROM USERS WHERE ID=1"
    )
    mock_cursor.close.assert_called_once()
    mock_connect.commit.assert_called_once()
    mock_connect.close.assert_called_once()


def test_get_user_id_1_nomock():
    logger.info("Skipping real DB test (no test DB configured)")
    pytest.skip("Real database not configured for testing")
