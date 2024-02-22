import pytest
import requests
import sys
@pytest.fixture
def base_url():
    return "https://petstore.swagger.io/"

def validate_url(base_url):
    try:
        response = requests.head(base_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        print(f"URL '{base_url}' is valid.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error validating URL '{base_url}': {e}")
        sys.exit()


FILE_ORDER = {
    "tests.test_pet.py": 2,
    "tests.test_store.py": 3,
    "tests.test_user.py": 1,
}



