from calc import add


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

