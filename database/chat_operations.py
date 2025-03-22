import mysql.connector
import json
from config import DB_CONFIG

def get_db_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

def save_conversation(conversation):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = """
        INSERT INTO conversations (id, username, title, date, messages)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE messages = %s
        """
        conv_id = conversation["id"]
        username = conversation["username"]
        title = conversation["title"]
        date = conversation["date"]
        messages = json.dumps(conversation["messages"])  # Serialize to JSON array
        print("DEBUG: Serialized messages ->", messages)  # Debugging line
        cursor.execute(query, (conv_id, username, title, date, messages, messages))
        conn.commit()
        cursor.close()
        conn.close()

def load_conversations(username):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM conversations WHERE username = %s", (username,))
        conversations = cursor.fetchall()
        cursor.close()
        conn.close()

        # Deserialize the messages field from JSON string to list of dictionaries
        for conv in conversations:
            print("DEBUG: Raw messages data from DB ->", conv["messages"])  # Debugging line
            try:
                conv["messages"] = json.loads(conv["messages"])
                print(f"DEBUG: Successfully deserialized messages for conversation {conv['id']}")
            except json.JSONDecodeError as e:
                print(f"DEBUG: JSONDecodeError for conversation {conv['id']}: {e}")
                conv["messages"] = []  # Fallback to an empty list
        return conversations
    return []

def load_conversation_by_id(conversation_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM conversations WHERE id = %s"
        cursor.execute(query, (conversation_id,))
        conversation = cursor.fetchone()
        cursor.close()
        conn.close()

        if conversation:
            try:
                # Deserialize the messages field from JSON string to list of dictionaries
                conversation["messages"] = json.loads(conversation["messages"])
                print("DEBUG: Deserialized messages ->", conversation["messages"])
            except json.JSONDecodeError as e:
                print(f"ERROR: Failed to deserialize messages for conversation {conversation_id}: {e}")
                conversation["messages"] = []  # Fallback to empty list
            return conversation
    return None

def delete_conversation(conversation_id):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "DELETE FROM conversations WHERE id = %s"
        cursor.execute(query, (conversation_id,))
        conn.commit()
        cursor.close()
        conn.close()