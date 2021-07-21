from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
import cv2
import time
import face_recognition
import os
import datetime
import detect_mask_video
from attendance import att

def matt(match):
    window = Tk()
    window.geometry("500x490")
    window.title("SURVEILLANCE PROGRAM")
    window.resizable(0, 0)
    window.config(bg='light blue')
    global entryid, entryName, entryPhone, entryEmail, entryaddress, entryDesignation

    # database connection
    conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
    cursor = conn.cursor()

    x = match.split(" ")
    print(x)

    cursor.execute("select * from employee where empid=%s", (x[0],))
    my_result = cursor.fetchall()
    conn.commit()

    # labels
    label_title = Label(window, text="EMPLOYEE DETAILS", fg='black', bg='light blue',
                       font=('Times New Roman', 22, 'bold', 'underline'))
    label_title.place(x=85, y=1)

    '''
a = "C:\\Users\\Pragya.DESKTOP-3UL0L63\\PycharmProjects\\pythonProject\\known\\"+match+"0.png"
global im
im = Image.open(a)

resized_im = im.resize((round(im.size[0] * 0.27), round(im.size[1] * 0.27)))
b= match+".png"
resized_im.save(b)
c="C:\\Users\\Pragya.DESKTOP-3UL0L63\\PycharmProjects\\pythonProject\\"+b
label_image = PhotoImage(file=c)

label1 = Label(window, bg='white', image=label_image, height=160, width=150)
label1.place(x=160, y=40)
'''

    label_id = Label(window, text="Employee ID                - ", fg='black', bg='light blue',
                     font=('Times New Roman', 14))
    label_id.place(x=60, y=100)
    label_name = Label(window, text="Employee Name           - ", fg='black', bg='light blue',
                       font=('Times New Roman', 14))
    label_name.place(x=60, y=140)
    label_phone = Label(window, text="Employee Phone          - ", fg='black', bg='light blue',
                        font=('Times New Roman', 14))
    label_phone.place(x=60, y=180)
    label_email = Label(window, text="Employee Email           - ", fg='black', bg='light blue',
                        font=('Times New Roman', 14))
    label_email.place(x=60, y=220)
    label_Address = Label(window, text="Employee Address       - ", fg='black', bg='light blue',
                          font=('Times New Roman', 14))
    label_Address.place(x=60, y=260)
    label_designation = Label(window, text="Employee Designation  - ", fg='black', bg='light blue',
                              font=('Times New Roman', 14))
    label_designation.place(x=60, y=300)
    # label_image = Label(window, text="Employee Image", fg='black', bg='white',
    #                   font=('Times New Roman', 14)).place(x=60, y=300)

    label_id1 = Label(window, text=my_result[0][0], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id1.place(x=260, y=100)
    label_id2 = Label(window, text=my_result[0][1], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id2.place(x=260, y=140)
    label_id3 = Label(window, text=my_result[0][2], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id3.place(x=260, y=180)
    label_id4 = Label(window, text=my_result[0][3], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id4.place(x=260, y=220)
    label_id5 = Label(window, text=my_result[0][4], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id5.place(x=260, y=260)
    label_id6 = Label(window, text=my_result[0][5], fg='black', bg='light blue',
                      font=('Times New Roman', 14))
    label_id6.place(x=260, y=300)

    # date and time stamp
    emp_id = my_result[0][0]
    emp_name = my_result[0][1]

    d = datetime.datetime.now()
    date = d.strftime("%x")
    time = d.strftime("%X")
    f = d.hour
    g = d.minute
    if (f < 10):
        h = "on time"
    elif (f == 10 and g <= 30):
        h = "on time"
    else:
        h = "Late"

    # attendance function
    def markyourattendance():
        messagebox.showinfo(title="Surveillance Program", message="PLEASE CONFIRM THAT YOU WEAR A MASK!! THIS IS MANDATORY")
        cursor.execute("insert into attendance(empid, empname, Date, Time, On_Time_or_Late)values(%s,%s,%s,%s,%s)",
                       (emp_id, emp_name, date, time, h))
        conn.commit()
        messagebox.showinfo(title="Surviellance System", message="Attendance Marked")

    # button
    mark = Button(window, text='Mark Your Attendance', fg='black', bg='light blue', font=("Times New Roman", 12, 'bold'),
                  relief='raised', justify='center', command=markyourattendance)
    mark.place(x=160, y=360)


    window.mainloop()