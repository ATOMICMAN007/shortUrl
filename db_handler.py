import sqlite3

conn = sqlite3.connect('shortUrl.db')

script = """CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    original_url TEXT NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0
);"""

conn.executescript(script)
conn.commit()
conn.close()

