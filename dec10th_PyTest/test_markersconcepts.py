import pytest

#@pytest.mark.smoke --> Marking the test case as smoke
#@pytest.mark.regression --> Marking the test case as regression
#@pytest.mark.sanity --> Marking the test case as sanity
#To run the test cases based on the markers, we use the following command:
#pytest -m smoke -v test_markersconcepts.py

@pytest.mark.smoke
def test_first():
    print("This is my first test")

@pytest.mark.regression
def test_second():
    print("This is my second test")

@pytest.mark.sanity
def test_third():
    print("This is my third test")

@pytest.mark.smoke
def test_fourth():
    print("This is my fourth test")

@pytest.mark.regression
@pytest.mark.sanity
def test_fifth():
    print("This is my fifth test")

#mark.skip is used to skip the test case

@pytest.mark.skip
@pytest.mark.regression
def test_sixth():
    print("This is my sixth test")

@pytest.mark.regression
@pytest.mark.xfail #mark.xfail is used to mark the test case as expected to fail
def test_seventh():
    print("This is my seventh test")

#if the test case is passed then it will be marked as xpass if the test cases is failed then it will be marked as xfail