import sqlite3

from config import DATABASE
from db.queries import CREATE_USERS_TABLE

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute(CREATE_USERS_TABLE)
    conn.commit()
    conn.close()