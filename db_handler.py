import psycopg2
from datetime import datetime

DB_NAME = "agent_db"
DB_USER = "agent_user"
DB_PASS = "agent_pass"
DB_HOST = "localhost"
DB_PORT = "5432"

def save_summary(user_query, ai_response):
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO summaries (user_query, ai_response, created_at) VALUES (%s, %s, %s)",
            (user_query, ai_response, datetime.now())
        )
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Saved to DB")
    except Exception as e:
        print("❌ Error saving to DB:", e)


def get_all_summaries():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM summaries ORDER BY created_at DESC;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows
    except Exception as e:
        print("❌ Error fetching from DB:", e)
        return []
