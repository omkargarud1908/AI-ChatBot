from database.db_connection import get_db_connection
from utils.password_utils import hash_password, generate_salt

def register_user(username, password):
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
            conn.commit()
            return True
        except mysql.connector.IntegrityError:
            return False  # Username already exists
        finally:
            cursor.close()
            conn.close()
    return False

def authenticate(username, password):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT password, salt FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if user_data and user_data["password"] == hash_password(password, user_data["salt"]):
            return True
    return False