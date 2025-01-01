import pytest

@pytest.mark.parametrize("input1, input2, output", [(2, 3, 5), (3, 7, 10), (5, 6, 10)])
def test_parmeterizing_data(input1, input2, output):

    assert input1 + input2 == output
    print("Test Passed")
