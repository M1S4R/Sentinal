import sqlite3
import os

db_path = os.path.join(
    os.path.dirname(__file__),
    "threat_intel.db"
)

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    ip TEXT,
    risk_score INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database initialized successfully")