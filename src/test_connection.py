from src.config.db import get_connection

connection = get_connection()

print("✅ Database Connected Successfully!")

connection.close()