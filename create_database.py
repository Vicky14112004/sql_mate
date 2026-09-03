import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD")
)

cursor = conn.cursor()

cursor.execute("""
    CREATE DATABASE IF NOT EXISTS IPL_ANALYTICS
""")

print("✅ IPL_ANALYTICS database created successfully!")

cursor.close()
conn.close()