import pytest

from starlette.testclient import TestClient

from app.main import app
from app.tests.factories import PhotoFactory, WorkFactory


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def mock_photo(test_client):
    print(test_client)
    return PhotoFactory.create_batch(10)


@pytest.fixture
def mock_work(test_client):
    return WorkFactory.create_batch(10)
