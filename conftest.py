import pytest

from main import BooksCollector

@pytest.fixture
def book():
    collector = BooksCollector()
    return collector
