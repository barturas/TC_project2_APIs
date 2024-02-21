import pytest
import sys
from project import check_cla
from unittest.mock import patch

def test_check_cla_valid_args():
    test_args = ["project.py", "test@example.com", "news"]
    with patch.object(sys, 'argv', test_args):
        recipient, api = check_cla()
        assert recipient == "test@example.com"
        assert api == "news"

def test_check_cla_invalid_args():
    test_args = ["script.py", "test@example.com", "invalidapi"]
    with patch.object(sys, 'argv', test_args):
        with pytest.raises(SystemExit):
            check_cla()
