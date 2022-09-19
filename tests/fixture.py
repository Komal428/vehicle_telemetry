import pytest
from app import app

"""Initialize the testing environment

Creates an app for testing that has the configuration flag ``TESTING`` set to
``True``.

"""

@pytest.fixture
def client():
    client = app.test_client()

    yield client