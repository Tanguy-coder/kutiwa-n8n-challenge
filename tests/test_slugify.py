import pytest
from utils.slugify import slugify

@pytest.mark.parametrize("input_text,expected", [
    ("Hello World!", "hello-world"),
    ("  Multiple   spaces  ", "multiple-spaces"),
    ("Café-au-lait", "cafe-au-lait"),
    ("Python_3.8+", "python-3-8"),
    ("--Already--slug--", "already-slug"),
])
def test_slugify(input_text, expected):
    assert slugify(input_text) == expected
