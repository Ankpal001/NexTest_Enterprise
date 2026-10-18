
import allure

@allure.feature("Framework Setup")
@allure.story("Basic Validation")
@allure.title("Verify that the test framework is working")
def test_framework_setup():
    expected_result = "NexTest Enterprise"
    actual_result = "NexTest Enterprise"

    assert actual_result == expected_result
