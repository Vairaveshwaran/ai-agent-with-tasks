import psycopg2
from datetime import datetime

# Database connection settings
DB_NAME = "agent_db"
DB_USER = "agent_user"
DB_PASS = "agent_pass"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()
    print("✅ Connected to PostgreSQL")

    # Insert a test row
    cur.execute(
        "INSERT INTO summaries (user_query, ai_response, created_at) VALUES (%s, %s, %s)",
        ("Hello AI!", "This is a test response from Python.", datetime.now())
    )
    conn.commit()

    # Fetch rows
    cur.execute("SELECT * FROM summaries;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
