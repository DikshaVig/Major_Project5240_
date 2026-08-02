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

conn = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    port=int(os.getenv("MYSQLPORT", "3306")),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQLDATABASE")
)


# --------------------------------------------
# Save Prediction History
# --------------------------------------------

def save_prediction(gender, age, income, spending, cluster):

    connection = create_connection()
    cursor = connection.cursor()

    query = """
    INSERT INTO prediction_history
    (
        Gender,
        Age,
        AnnualIncome,
        SpendingScore,
        PredictedCluster
    )
    VALUES
    (%s, %s, %s, %s, %s)
    """

    values = (
        gender,
        age,
        income,
        spending,
        cluster
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()


# --------------------------------------------
# Get Cluster Information
# --------------------------------------------

def get_cluster_details(cluster_id):

    connection = create_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM clusters
    WHERE ClusterID = %s
    """

    cursor.execute(
        query,
        (cluster_id,)
    )

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result


# --------------------------------------------
# Get Prediction History
# --------------------------------------------

def get_history():

    connection = create_connection()

    cursor = connection.cursor()

    query = """
    SELECT *
    FROM prediction_history
    ORDER BY PredictionID DESC
    """

    cursor.execute(query)

    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data
