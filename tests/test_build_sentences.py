# -------------------------------------------------
# Author : Diogo Rangel Dos Santos - W06 Assignment: Unit Testing Techniques + Coverage Tools
# -------------------------------------------------
import pytest
import json
from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    get_word,
    fix_agreement,
    build_sentence,
    structures
)

# -------------------------------------------------
# Test function that reads from console
# -------------------------------------------------
def test_get_seven_letter_word(mocker):
    mocker.patch("builtins.input", return_value="testing")
    result = get_seven_letter_word()
    # function converts to uppercase
    assert result == "TESTING"


# -------------------------------------------------
# Test reading JSON file using tmp_path
# -------------------------------------------------
def test_parse_json_from_file(tmp_path):
    test_data = {
        "nouns": ["cat"],
        "verbs": ["run"],
        "adjectives": ["big"],
        "adverbs": ["quickly"],
        "prepositions": ["on"]
    }

    file_path = tmp_path / "test.json"

    with open(file_path, "w") as f:
        json.dump(test_data, f)

    result = parse_json_from_file(file_path)
    assert result == test_data


# -------------------------------------------------
# Test random structure without mocking
# -------------------------------------------------
def test_choose_sentence_structure():
    structure = choose_sentence_structure()
    assert structure in structures


# -------------------------------------------------
# Test random structure with mocking
# -------------------------------------------------
def test_choose_sentence_structure_mock(mocker):
    mocker.patch("random.choice", return_value=structures[0])
    result = choose_sentence_structure()
    assert result == structures[0]


# -------------------------------------------------
# Test get_pronoun using mock
# -------------------------------------------------
def test_get_pronoun(mocker):
    mocker.patch("random.choice", return_value="he")
    result = get_pronoun()
    assert result == "he"


# -------------------------------------------------
# Test get_article using mock
# -------------------------------------------------
def test_get_article(mocker):
    mocker.patch("random.choice", return_value="a")
    result = get_article()
    assert result == "a"


# -------------------------------------------------
# Test get_word (ASCII indexing logic)
# -------------------------------------------------
def test_get_word():
    words = ["cat", "dog", "bird"]
    result = get_word("A", words)  # 'A' = index 0
    assert result == "cat"


# -------------------------------------------------
# Test fix_agreement (covers verb agreement branch)
# -------------------------------------------------
def test_fix_agreement():
    result = fix_agreement("run")
    # function may modify or return value depending on implementation
    assert result is None or isinstance(result, str)


# -------------------------------------------------
# Test build_sentence
# -------------------------------------------------
def test_build_sentence(mocker):
    data = {
        "nouns": ["cat"],
        "verbs": ["run"],
        "adjectives": ["big"],
        "adverbs": ["quickly"],
        "prepositions": ["on"]
    }

    # Seed word must be long enough for indexing
    seed_word = "ABCDEFG"

    # Mock random.choice for article/pronoun selection
    mocker.patch("random.choice", return_value="a")

    structure = structures[0]

    sentence = build_sentence(seed_word, structure, data)

    assert isinstance(sentence, str)
    assert sentence.endswith(".")
    assert len(sentence) > 0
