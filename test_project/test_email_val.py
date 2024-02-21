import pytest
from project import check_email
from email_validator import EmailNotValidError

def test_check_email_valid():
    assert check_email("test@example.com") == "test@example.com"

def test_check_email_invalid():
    with pytest.raises(SystemExit) as e:
        check_email("invalidemail")
    assert "The email address is not valid" in str(e.value)