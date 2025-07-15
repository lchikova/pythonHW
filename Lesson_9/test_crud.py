import pytest
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select, delete, update

DB_URL = "postgresql://postgres:1315@localhost:5432/QA"
engine = create_engine(DB_URL)
metadata = MetaData()

users = Table(
    'users', metadata,
    Column('user_id', Integer),
    Column('user_email', String, nullable=False),
    Column('subject_id', Integer)
)


@pytest.fixture
def db_connection():
    connection = engine.connect()
    yield connection
    connection.close()


def test_add_user(db_connection):
    test_user = {
        'user_id': 999,
        'user_email': 'test@example.com',
        'subject_id': 1
    }

    insert_stmt = users.insert().values(test_user)
    db_connection.execute(insert_stmt)

    select_stmt = select(users).where(users.c.user_id == 999)
    result = db_connection.execute(select_stmt).fetchone()

    assert result is not None
    assert result.user_email == 'test@example.com'

    delete_stmt = delete(users).where(users.c.user_id == 999)
    db_connection.execute(delete_stmt)


def test_update_user(db_connection):
    test_user = {
        'user_id': 999,
        'user_email': 'test@example.com',
        'subject_id': 1
    }
    insert_stmt = users.insert().values(test_user)
    db_connection.execute(insert_stmt)

    update_stmt = (
        update(users)
        .where(users.c.user_id == 999)
        .values(user_email='updated@example.com')
    )
    db_connection.execute(update_stmt)

    select_stmt = select(users).where(users.c.user_id == 999)
    result = db_connection.execute(select_stmt).fetchone()

    assert result.user_email == 'updated@example.com'

    delete_stmt = delete(users).where(users.c.user_id == 999)
    db_connection.execute(delete_stmt)


def test_delete_user(db_connection):
    test_user = {
        'user_id': 999,
        'user_email': 'test@example.com',
        'subject_id': 1
    }
    insert_stmt = users.insert().values(test_user)
    db_connection.execute(insert_stmt)

    delete_stmt = delete(users).where(users.c.user_id == 999)
    db_connection.execute(delete_stmt)

    select_stmt = select(users).where(users.c.user_id == 999)
    result = db_connection.execute(select_stmt).fetchone()

    assert result is None
