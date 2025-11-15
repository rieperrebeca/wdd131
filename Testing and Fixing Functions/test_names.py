from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Alice", "Smith") == "Smith; Alice"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("Smith; Alice") == "Smith"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("Smith; Alice") == "Alice"

#call the main function that is part of pytest so that the
#computer will execute the test functions in this file
pytest.main(["-v", "--tb=line", "-rN", __file__])