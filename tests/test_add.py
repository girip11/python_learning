from tryouts.add import add


# Test methods should be prefixed with "test_"
# to be discovered and run by the test explorer
def test_add():
    assert add(1, 2) == 3
