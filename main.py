from tkinter import *
from tkinter import messagebox
#from detect_mask_video import dm
import cv2

from frame2 import f2
#import detect_mask_video
import mysql.connector

window = Tk()
window.geometry("420x400")
window.title("")
window.resizable(0, 0)
window.config(bg='light blue')

username = StringVar()
password = StringVar()


#database connection
conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost', auth_plugin='mysql_native_password',
                             database='surveillance')
cursor = conn.cursor()

#logo
label_image = PhotoImage(file="E:\\Netbeans project new\\Email\\src\\email\\1111.png")
label1 = Label(window, bg='light blue',image=label_image, justify='center',
               font=('arial', 16, "bold"), height=60, width=150).place(x=140, y=5)

#label_image1 = PhotoImage(file="C:\\Users\\Pragya.DESKTOP-3UL0L63\\Downloads\\cctv(3).png")
#label2 = Label(window, bg='light blue', image=label_image1, justify='center',
              #     font=('arial', 16, "bold"), height=80, width=120).place(x=300, y=5)
#labels
labelUser = Label(window, text="Username", fg='black', bg='light blue',
                  font=('Times New Roman', 12)).place(x=130, y=75)
labelPass = Label(window, text="Password", fg='black', bg='light blue',
                  font=('Times New Roman', 12)).place(x=130, y=125)
#Entry Boxes
entryUser = Entry(window, fg='black', bg='light blue',
                  font=('Times New Roman', 12, 'bold'), relief='sunken', textvariable= username).place(x=130, y=100)
entryPass = Entry(window, fg='black', bg='light blue', show="x",
                  font=('Times New Roman', 12, 'bold'), relief='sunken',textvariable= password).place(x=130, y=150)


#function for the login button
def alert() :
    w = username.get()
    b = password.get()
    saveQuery = 'select username, password from admin'
    cursor.execute(saveQuery)
    print(cursor)
    for (email,pas) in cursor:
        if w==email and b==pas:
            cursor.execute('select name from admin where username=%s',(w,))
            my_result = cursor.fetchall()
            conn.commit()
            i=my_result[0][0]
            window.destroy()
            f2(i)
        else:
            messagebox.showwarning(message='Incorrect Details')
    conn.commit()
    print("Query Executed successfully")
    return

buttonLogin = Button(window, text='     Login     ', justify='center', fg='black', bg='light blue',
                     font=('Times New Roman', 12, 'bold'), relief='raised', command=alert).place(x=160, y=195)

labelForgot = Label(window, text='Problem in signing in?', fg='black', bg='light blue',
                    font=("Times New Roman", 10)).place(x=93, y=260)

buttonForgot = Button(window, text='Forgot Password', fg='red', bg='light blue',
                      font=('Times New Roman', 8)).place(x=220, y=258)


window.mainloop()