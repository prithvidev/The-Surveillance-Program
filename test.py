from tkinter import messagebox

import cv2
import mysql.connector
from PIL import Image
from future.utils import tobytes

conn= mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
cursor = conn.cursor()

'''
with open('./visitor/qwer.png', "rb") as file:
    binarydata= file.read()
    cursor.execute(
        "insert into visitor(visitor_id,visitor_name,visitor_phone,visitor_email,purpose,whom_to_meet,image)values(%s,%s,%s,%s,%s,%s,%s)",
        ("1","Prithvi", "9891691925", "prithvidevkanojia@gmail.com", "documentation", "Vikram jha", binarydata))
    conn.commit()
    messagebox.showinfo(title="VISITOR DETAIL", message="VISITOR DETAIL ADDED")





write image
'''
sql_fetch_blob_query = "SELECT * from visitor where visitor_id = %s"

cursor.execute(sql_fetch_blob_query, ("1",))
record = cursor.fetchall()
for row in record:
    print("Id = ", row[0], )
    print("Name = ", row[1])
    print("phone = ",row[2])
    print("email = ", row[3])
    print("purpose = ", row[4])
    print("whom to meet = ", row[5])
    image = row[6]
    print("Storing employee image and bio-data on disk \n")
    with open('fetch.png', 'wb') as file:
        file.write(image)
