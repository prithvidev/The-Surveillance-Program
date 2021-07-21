import time
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

import mysql.connector
import cv2
import re
#from frame2 import f2

def addEmp():
    window = Tk()
    window.geometry("500x430")
    window.title("SURVEILLANCE PROGRAM")
    window.resizable(0, 0)
    window.config(bg='light blue')
    global entryid, entryName, entryPhone, entryEmail, entryaddress, entryDesignation

    def phonevalidate(user_phoneno):
        if user_phoneno.isdigit():
            return True
        elif user_phoneno == "":
            return True
        else:
            return False


    def isValidEmail(user_email):
        if len(user_email) > 7:
            if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', user_email)):
                return True
            return False
        else:
            return False


    def validateName(user_name):
        if user_name.isalpha():
            return True
        elif user_name == "":
            return True
        else:
            return False

    def validateAllfeilds():
        '''
        elif entryEmail.get() != "":
            status = isValidEmail(entryEmail.get())
            if status == True:
                labelpng = PhotoImage(file="C:\\Users\\Pragya.DESKTOP-3UL0L63\\PycharmProjects\\pythonProject\\Yes.png")
                label1 = Label(window, image=labelpng, justify='center',
                               height=30, width=30)
                label1.place(x=450, y=140)
            else:
                messagebox.showinfo(message="Enter Correct Email Address")

        x = isValidEmail(entryEmail.get())
        y = phonevalidate(entryPhone.get())
        z = validateName(entryName.get())
        if z==True and x==True and y==True and len(entryPhone.get())==10 and entryEmail.get()!="" and entryDesignation.get()!="" and entryaddress.get()!="":
            return True
        else:
            return False
        '''
        status = isValidEmail(entryEmail.get())
        if entryName.get() == "":
            messagebox.showwarning(message="Enter Correct Name")
            return False

        elif len(entryPhone.get()) != 10:
            messagebox.showinfo(message="Enter Correct Number!")
            return False

        elif status == False:
            messagebox.showinfo(message="Enter Correct Email!")
            return False

        elif len(entryaddress.get()) == 0:
            messagebox.showwarning(message="Enter Correct Address")
            return False

        elif len(entryDesignation.get()) == 0:
            messagebox.showwarning(message="Choose Correct Designation")
            return False
        else:
            return True

    # database connection
    conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
    cursor = conn.cursor()
    #labels
    label_title = Label(window, text="NEW EMPLOYEE DETAILS", fg='black', bg='light blue',
                     font=('Times New Roman', 20,'bold','underline')).place(x=80, y=1)
    label_id = Label(window, text="Employee ID", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=60)
    label_name = Label(window, text="Employee Name", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=100)
    label_phone = Label(window, text="Employee Phone", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=140)
    label_email = Label(window, text="Employee Email", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=180)

    label_Address = Label(window, text="Employee Address", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=220)
    label_designation = Label(window, text="Employee Designation", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=260)
    label_image = Label(window, text="Employee Image", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=300)
    #entries
    #entryid = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    #entryid.place(x=260, y=60)
    cursor.execute("select * from employee")
    cursor.fetchall()
    conn.commit()
    a = cursor.rowcount
    a = 100+a
    labelid = Label(window, text=a, fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=260, y=60)
    entryName = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryName.place(x=260, y=100)
    valid_name = window.register(validateName)
    entryName.config(validate="key", validatecommand=(valid_name, '%P'))

    entryPhone = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryPhone.place(x=260, y=140)
    valid_phoneno = window.register(phonevalidate)
    entryPhone.config(validate="key", validatecommand=(valid_phoneno, '%P'))

    entryEmail = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryEmail.place(x=260, y=180)

    entryaddress = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryaddress.place(x=260, y=220)
    #entryDesignation = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')

    entryDesignation = Combobox(window, width=24,font=('Times New Roman', 12, 'bold'))
    entryDesignation['values'] = ('Software Developer', 'Team Leader', 'Manager', 'Graphic Designer', 'Sweeper', 'Assisstant'
                                  ,'Director', 'CEO', 'Floor Manager')
    entryDesignation.place(x=260, y=260)

    #camera function
    def click():
        global x,y
        d = 0
        x = str(a)
        y = entryName.get()
        #camera = cv2.VideoCapture(0)
        for i in range(8):
            camera = cv2.VideoCapture(0)
            return_value, image = camera.read()
            cv2.imwrite('./known/' +x+" "+y+str(i) + '.png', image)
            del (camera)
        messagebox.showinfo(message="PHOTOS CLICKED")


    def upload():
        if validateAllfeilds() :
            global a1, a2, a3, a4, a5, a6
            a2 = entryName.get()
            a3 = entryPhone.get()
            a4 = entryEmail.get()
            a5 = entryaddress.get()
            a6 = entryDesignation.get()
            print(len(a6), len(a5))
            cursor.execute("insert into employee(empid,empname,phone,email,address,designation)values(%s,%s,%s,%s,%s,%s)",
                (a, a2, a3, a4, a5, a6))
            conn.commit()
            messagebox.showinfo(title="ADD NEW EMPLOYEE", message="EMPLOYEE ADDED")
            window.destroy()

    #button
    buttonCamera = Button(window, text='Open Camera', justify='center', fg='black', bg='light blue',
                         font=('Times New Roman', 12, 'italic'), relief='raised', command=click).place(x=260, y=300)
    buttonSubmit = Button(window, text='  SUBMIT  ', justify='center', fg='black', bg='light blue',
                          font=('Times New Roman', 14, 'bold'), relief='raised', command=upload).place(x=200, y=360)
    window.mainloop()
