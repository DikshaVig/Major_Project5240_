# ============================================
# DATABASE CONNECTION FILE
# Customer Segmentation Project
# ============================================

import mysql.connector


# --------------------------------------------
# Create Database Connection
# --------------------------------------------

import os
import mysql.connector

connection = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE"),
    port=int(os.getenv("MYSQLPORT"))
)

except mysql.connector.Error as error:
print("Database connection error:")
print(error)
return None
