import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "localmind.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS transcripts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TEXT NOT NULL,
  text TEXT NOT NULL
)
""")

conn.commit()
