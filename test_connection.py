from database import create_connection


connection = create_connection()


if connection:
    print("MYSQL CONNECTED SUCCESSFULLY")
    connection.close()

else:
    print("CONNECTION FAILED")