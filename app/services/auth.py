import mysql.connector

def login_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_mysql_password",
        database="course_db"
    )
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    conn.close()
    return user
