import sqlite3

conn = sqlite3.connect("localmind.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS transcripts (
  id INTEGER PRIMARY KEY,
  timestamp TEXT,
  text TEXT
)
""")
conn.commit()
