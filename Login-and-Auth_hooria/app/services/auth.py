import mysql.connector

def authenticate(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="course_management"
    )
    cursor = conn.cursor()
    query = "SELECT role FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None
