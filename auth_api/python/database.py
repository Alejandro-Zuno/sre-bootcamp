from re import X
import mysql.connector
import os

mydb = mysql.connector.connect(
    host = os.environ['DB_HOST'],
    user = os.environ['DB_USER'],
    passwd = os.environ['DB_PASS'],
    database = os.environ['DB_NAME']
)