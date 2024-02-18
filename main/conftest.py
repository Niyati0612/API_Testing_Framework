import pytest
import requests, sys

@pytest.mark.optionalhook
def pytest_html_report_title(report):
    report.title = "Your Custom Title"


def validate_url(base_url):
    try:
        response = requests.head(base_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print(f"\nURL '{base_url}' is valid.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error validating URL '{base_url}': {e}")
        pytest.fail(f"Error validating URL '{base_url}': {e}")


@pytest.fixture
def base_url():
    base_url = "https://petstore.swagger.io/"
    if not validate_url(base_url):
        sys.exit(1)
    return base_url


FILE_ORDER = {
    "tests.test_pet.py": 2,
    "tests.test_store.py": 3,
    "tests.test_user.py": 1,
}



