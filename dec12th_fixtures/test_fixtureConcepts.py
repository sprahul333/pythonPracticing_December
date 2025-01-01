import pytest

#Scope of the fixture can be module, class, function, package, session
#Scope defines how do you want to execute the fixture (setup and teardown)
#module: The fixture will be executed only once for the entire module (All the test cases in the module)
#class: The fixture will be executed only once for the entire class (All the test cases in the class)
#function: The fixture will be executed for every test case in the module
#package: The fixture will be executed for the entire package (All the modules in the package)
#session: The fixture will be executed for the entire session (All the packages in the session)
#Default scope is function

# Fixtures are used to setup and teardown the test environment
@pytest.fixture(scope= "module")
def setup(): #Works like before method and after method
    print("Setup fixture")
    yield # This is used to perform the teardown activity after the test is executed
    print("Teardown fixture")

def test_one(setup):
    print("Test fixture")

def test_two(setup):
    print("Test fixture1")

def test_three(setup):
    print("Test fixture2")