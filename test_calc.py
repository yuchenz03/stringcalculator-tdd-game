from calc import add
import pytest


# Write your tests below.
# Use assert statements to check that calc returns the correct result.
# All test functions must start with test_ to be discovered by pytest or similar frameworks.
# We have included a single starter test.
# Add more test_* functions as you work through each new requirement.
# Example:

def test_example_string_returns_zero():
    assert add("") == 0  # uncomment to test

def test_single_number():
    assert add("1") == 1
    assert add("2") == 2
    assert add("10") == 10

def test_comma_separated_numbers():
    assert add("1,2,3,4") == 10
    assert add("6,7") == 13
    assert add("4,2,3") == 9

def test_new_line_separated_numbers():
    assert add("1\n2\n3\n4") == 10
    assert add("6\n7") == 13
    assert add("4\n2\n3") == 9

def test_custom_delimiters():
    assert add("//;\n1;2") == 3
    assert add("//!\n1!2!3!4") == 10
    assert add("//?\n6?7?8") == 21

def test_negative_numbers():
    with pytest.raises(ValueError, match="negatives not allowed: -1"): 
        add("//;\n-1;2")
    with pytest.raises(ValueError, match="negatives not allowed: -3"): 
        add("//!\n1!2!-3!4")
    with pytest.raises(ValueError, match="negatives not allowed: -8"): 
        add("//?\n6?7?-8")

