import pytest
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType
@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    if hasattr(request.node, "rep_call"):
        if request.node.rep_call.failed:
            screenshot = browser.get_screenshot_as_png()

            allure.attach(
                screenshot,
                name=f"{request.node.name}_failure",
                attachment_type=AttachmentType.PNG
            )

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        setattr(item, "rep_call", report)



from config.config import TEST_EMAIL, TEST_PASSWORD

@pytest.fixture
def test_credentials():
    if not TEST_EMAIL or not TEST_PASSWORD:
        pytest.fail(
            "TEST_EMAIL and TEST_PASSWORD must be configured "
            "in environment variables"
        )

    return {
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD
    }

