from src.database import FakeDatabase

def test_database_connection():
    db = FakeDatabase()

    assert db.connect() is True
    assert db.is_connected() is True
