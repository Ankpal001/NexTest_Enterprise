import os

BASE_URL = os.getenv("BASE_URL","https://naveenautomationlabs.com/opencart" )
LOGIN_URL = f"{BASE_URL}/index.php?route=account/login"

EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", "10"))
TEST_EMAIL = os.getenv("TEST_EMAIL", "")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "")
