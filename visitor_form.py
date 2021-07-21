from tkinter import *
from tkinter import messagebox
import mysql.connector
import cv2
import re
#from frame2 import f2

def visitor():
    window = Tk()
    window.geometry("500x430")
    window.title("SURVEILLANCE PROGRAM")
    window.resizable(0, 0)
    window.config(bg='light blue')
    global entryid, entryName, entryPhone, entryEmail, entryPurpose, entryWhometomeet

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

        elif len(entryPurpose.get()) == 0:
            messagebox.showwarning(message="Enter Correct Purpose")
            return False

        elif len(entryWhomtomeet.get()) == 0:
            messagebox.showwarning(message="Choose Correct Name of the Person")
            return False
        else:
            return True

    # database connection
    conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
    cursor = conn.cursor()
    #labels
    label_title = Label(window, text="Visitor Details", fg='black', bg='light blue',
                     font=('Times New Roman', 20,'bold','underline')).place(x=80, y=1)
    label_id = Label(window, text="Visitor ID", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=60)
    label_name = Label(window, text="Visitor Name", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=100)
    label_phone = Label(window, text="Visitor Phone", fg='black', bg='light blue',
                  font=('Times New Roman', 14)).place(x=60, y=140)
    label_email = Label(window, text="Visitor Email", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=180)
    label_purpose = Label(window, text="Purpose", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=220)
    label_whomtomeet = Label(window, text="Whom To Meet", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=260)
    label_image = Label(window, text="Visitor Image", fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=60, y=300)
    #entries
    #entryid = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    #entryid.place(x=260, y=60)
    cursor.execute("select * from visitor")
    cursor.fetchall()
    conn.commit()
    a = cursor.rowcount
    a = 100+a
    labelid = Label(window, text=a, fg='black', bg='light blue',
                        font=('Times New Roman', 14)).place(x=260, y=60)
    #Name entry
    entryName = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryName.place(x=260, y=100)
    valid_name = window.register(validateName)
    entryName.config(validate="key", validatecommand=(valid_name, '%P'))
    #phone entry
    entryPhone = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryPhone.place(x=260, y=140)
    valid_phoneno = window.register(phonevalidate)
    entryPhone.config(validate="key", validatecommand=(valid_phoneno, '%P'))
    #email entry
    entryEmail = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryEmail.place(x=260, y=180)
    #purpose entry
    entryPurpose = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryPurpose.place(x=260, y=220)
    #whom to meet entry
    entryWhomtomeet = Entry(window, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entryWhomtomeet.place(x=260, y=260)

    #camera function
    def click():
        global x,y
        d = 0
        x = str(a)
        y = entryName.get()
        #camera = cv2.VideoCapture(0)

        camera = cv2.VideoCapture(0)
        return_value, image = camera.read()
        cv2.imwrite('./visitor/' +y + '.png', image)
        del (camera)
        messagebox.showinfo(message="PHOTO CLICKED!")
    #uploading data in database
    def upload():
        if validateAllfeilds() :
            global a1, a2, a3, a4, a5, a6
            a2 = entryName.get()
            a3 = entryPhone.get()
            a4 = entryEmail.get()
            a5 = entryPurpose.get()
            a6 = entryWhomtomeet.get()
            cursor.execute("insert into visitor(visitor_id,visitor_name,visitor_phone,visitor_email,purpose,whom_to_meet)values(%s,%s,%s,%s,%s,%s)",
                (a, a2, a3, a4, a5, a6))
            conn.commit()
            messagebox.showinfo(title="VISITOR DETAIL", message="VISITOR DETAIL ADDED")
            window.destroy()

    #button
    buttonCamera = Button(window, text='Open Camera', justify='center', fg='black', bg='light blue',
                         font=('Times New Roman', 12, 'italic'), relief='raised', command=click).place(x=260, y=300)
    buttonSubmit = Button(window, text='  SUBMIT  ', justify='center', fg='black', bg='light blue',
                          font=('Times New Roman', 14, 'bold'), relief='raised', command=upload).place(x=200, y=360)
    window.mainloop()

#extras
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
        if z==True and x==True and y==True and len(entryPhone.get())==10 and entryEmail.get()!="" and entryWhomtomeet.get()!="" and entryPurpose.get()!="":
            return True
        else:
            return False
        '''
#entryWhomtomeet = Combobox(window, width=24,font=('Times New Roman', 12, 'bold'))
    #entryWhomtomeet['values'] = ('Software Developer', 'Team Leader', 'Manager', 'Graphic Designer', 'Sweeper', 'Assisstant'
     #                             ,'Director', 'CEO', 'Floor Manager')