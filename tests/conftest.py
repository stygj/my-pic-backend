import pytest
from dataclasses  import asdict
from config import DBConfig
from connector_test import DBConnector

@pytest.fixture
def get_session():
    conn = DBConnector(**asdict(DBConfig()))
    return conn


