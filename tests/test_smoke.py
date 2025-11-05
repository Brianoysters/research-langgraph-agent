import re
from utils import safe_filename


def test_safe_filename_returns_string_and_safe_chars():
    name = safe_filename(prefix="test/session")
    # safe_filename should return a string and contain only allowed characters
    assert isinstance(name, str)
    assert re.match(r"^[A-Za-z0-9_-]+$", name)
