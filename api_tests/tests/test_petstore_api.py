import pytest
import logging
from api_tests.utils.api_client import PetstoreAPI

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PetstoreTest")

# Initialize API client
petstore_api = PetstoreAPI()

# ✅ Test 1: Create a Pet
def test_create_pet():
    logger.info("Testing: Create Pet")
    pet_data = {
        "id": 123456,
        "category": {"id": 1, "name": "Dog"},
        "name": "Buddy",
        "photoUrls": ["http://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    response = petstore_api.create_pet(pet_data)
    petstore_api.save_test_result("Create Pet", 200, response.status_code)
    assert response.status_code == 200

# ✅ Test 2: Get Pet by ID
def test_get_pet():
    logger.info("Testing: Get Pet")
    pet_id = 123456
    response = petstore_api.get_pet(pet_id)
    petstore_api.save_test_result("Get Pet", 200, response.status_code)
    assert response.status_code == 200


# ❌ Negative Test: Get Pet with Invalid ID (Expecting 404)
def test_get_pet_invalid():
    logger.info("Testing: Get Pet with Invalid ID")
    invalid_pet_id = "m"
    response = petstore_api.get_pet(invalid_pet_id)
    petstore_api.save_test_result("Get Pet (Invalid ID)", 404, response.status_code)
    assert response.status_code == 404

# ✅ Test 3: Update Pet
def test_update_pet():
    logger.info("Testing: Update Pet")
    updated_pet_data = {
        "id": 123456,
        "category": {"id": 1, "name": "Dog"},
        "name": "Max",
        "photoUrls": ["http://example.com/dog.jpg"],
        "tags": [{"id": 1, "name": "friendly"}],
        "status": "available"
    }
    response = petstore_api.update_pet(updated_pet_data)
    petstore_api.save_test_result("Update Pet", 200, response.status_code)
    assert response.status_code == 200

# ✅ Test 4: Delete Pet
def test_delete_pet():
    logger.info("Testing: Delete Pet")
    pet_id = 123456
    response = petstore_api.delete_pet(pet_id)
    petstore_api.save_test_result("Delete Pet", 200, response.status_code)
    assert response.status_code == 200


# ✅ Test 5: Find Pets by Status
@pytest.mark.parametrize("status", ["available", "pending", "sold"])
def test_find_pets_by_status(status):
    logger.info(f"Testing: Find Pets by Status - {status}")
    response = petstore_api.find_pets_by_status(status)
    petstore_api.save_test_result(f"Find Pets by Status - {status}", 200, response.status_code)
    assert response.status_code == 200


@pytest.fixture(scope="session", autouse=True)
def generate_report():
    yield
    petstore_api.generate_excel_report()
