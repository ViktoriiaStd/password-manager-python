import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from validation import validate_password


def test_valid_password():
    errors = validate_password("Aa123456!")
    assert errors == []

def test_password_too_short():
    errors = validate_password("Aa!")
    assert any("8 characters" in error for error in errors)

def test_no_uppercase():
    errors = validate_password("aa123456!")
    assert any("uppercase" in error for error in errors)

def test_no_special_char():
    errors = validate_password("Aa1234567")
    assert any("special character" in error for error in errors)

def test_empty_password():
    errors = validate_password("")
    assert any("8 characters" in error for error in errors)
    assert any("lowercase" in error for error in errors)
    assert any("uppercase" in error for error in errors)
    assert any("digit" in error for error in errors)
    assert any("special character" in error for error in errors)

def test_no_lowercase():
    errors = validate_password("AA123456!")
    assert any("lowercase" in error for error in errors)

def test_no_digit():
    errors = validate_password("Aabbccdd!")
    assert any("digit" in error for error in errors)

 