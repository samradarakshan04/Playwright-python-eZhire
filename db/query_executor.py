import mysql.connector

def fetch_booking_by_id(booking_id):
    connection = mysql.connector.connect(
        host="localhost",
        user="youruser",
        password="yourpassword",
        database="ezhire"
    )
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM bookings WHERE id = %s", (booking_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result
