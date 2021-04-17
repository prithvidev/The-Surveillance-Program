from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk, Image
import datetime
import cv2
'''
def showEmp():
    window = Tk()
    window.geometry("500x490")
    window.title("SURVEILLANCE PROGRAM")
    window.resizable(0, 0)
    window.config(bg='white')
    global entryid, entryName, entryPhone, entryEmail, entryaddress, entryDesignation

    # database connection
    conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
    cursor = conn.cursor()
    cursor.execute("select * from employee where empid=%s",("001",))
    my_result = cursor.fetchall()
    print(my_result)

    conn.commit()
    #labels
    label_title = Label(window, text="NEW EMPLOYEE DETAILS", fg='black', bg='white',
                     font=('Times New Roman', 20,'bold','underline')).place(x=75, y=1)
    img = ImageTk.PhotoImage(Image.open('').resize(120, 150))  # the one-liner I used in my app
    label = Label(window, image=img)
    label.image = img  # this feels redundant but the image didn't show up without it in my app
    label.pack()

    #label_image = PhotoImage(file="C:\\Users\\Pragya.DESKTOP-3UL0L63\\PycharmProjects\\pythonProject\\known\\001 Prithvi1.png")
    #label1 = Label(window, text="WELCOME TO TKINTER", bg='white', image=label_image, justify='center',
                  # font=('arial', 16, "bold"), height=120, width=150).place(x=140, y=10)

    label_id = Label(window, text="Employee ID                - ", fg='black', bg='white',
                  font=('Times New Roman', 14)).place(x=60, y=200)
    label_name = Label(window, text="Employee Name           - ", fg='black', bg='white',
                  font=('Times New Roman', 14)).place(x=60, y=240)
    label_phone = Label(window, text="Employee Phone          - ", fg='black', bg='white',
                  font=('Times New Roman', 14)).place(x=60, y=280)
    label_email = Label(window, text="Employee Email           - ", fg='black', bg='white',
                        font=('Times New Roman', 14)).place(x=60, y=320)
    label_Address = Label(window, text="Employee Address       - ", fg='black', bg='white',
                        font=('Times New Roman', 14)).place(x=60, y=360)
    label_designation = Label(window, text="Employee Designation  - ", fg='black', bg='white',
                        font=('Times New Roman', 14)).place(x=60, y=400)
    #label_image = Label(window, text="Employee Image", fg='black', bg='white',
     #                   font=('Times New Roman', 14)).place(x=60, y=300)

    label_id = Label(window, text=my_result[0][0], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=200)
    label_id = Label(window, text=my_result[0][1], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=240)
    label_id = Label(window, text=my_result[0][2], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=280)
    label_id = Label(window, text=my_result[0][3], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=320)
    label_id = Label(window, text=my_result[0][4], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=360)
    label_id = Label(window, text=my_result[0][5], fg='black', bg='white',
                     font=('Times New Roman', 14)).place(x=260, y=400)

    #button
    #buttonCamera = Button(window, text='Open Camera', justify='center', fg='black', bg='white',
                        # font=('Times New Roman', 12, 'italic'), relief='raised', command=click).place(x=260, y=300)
    #buttonSubmit = Button(window, text='  SUBMIT  ', justify='center', fg='black', bg='white',
     #                     font=('Times New Roman', 14, 'bold'), relief='raised', command=upload).place(x=200, y=360)
    #if 0xFF == ord('q'):
     #   window.destroy()
    window.mainloop()
'''
'''
d = datetime.datetime.now()
date = d.strftime("%x")
time = d.strftime("%X")
f = d.hour
g = d.minute
if(f<10):
    h = "on time"
elif(f==10 and g<=30):
    h = "on time"
else:
    h = "Late"
print(h)
# database connection
conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                               auth_plugin='mysql_native_password',database='surveillance')
cursor = conn.cursor()
cursor.execute("Select * from employee")
my_re = cursor.fetchall()
conn.commit()
a = cursor.rowcount

a = 100 + a
a = "ASG" + str(a)
print(a)
'''
window = Tk()
window.geometry("500x430")
window.title("SURVEILLANCE PROGRAM")
window.resizable(0, 0)
window.config(bg='white')

def phonevalidate(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno == "":
        return True
    else:
        return False

def isValidEmail(user_email):
    if len(user_email)>7:
        if (re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',user_email)):
            return True
        messagebox.showinfo(message='Enter Correct email')
        return False
    else:
        messagebox.showinfo(message='Enter Correct email')
        return False

def validateAllfeilds():
    if len(entryPhone.get()) != 10:
        messagebox.showinfo(message="Entry Correct Number")
    elif entryEmail.get() != "" :
        status = isValidEmail(entryEmail.get())
        if status == True:
            labelpng = PhotoImage(file="C:\\Users\\Pragya.DESKTOP-3UL0L63\\PycharmProjects\\pythonProject\\Yes.png")
            label1 = Label(window, image=labelpng, justify='center',
                           height=30, width=30)
            label1.place(x=450, y=140)
        else:
            messagebox.showinfo(message="Correct")


label_phone = Label(window, text="Employee Phone", fg='black', bg='white',
                  font=('Times New Roman', 14)).place(x=60, y=140)
label_email = Label(window, text="Employee Email", fg='black', bg='white',
                    font=('Times New Roman', 14)).place(x=60, y=180)
entryPhone = Entry(window, fg='black', bg='white',font=('Times New Roman', 12, 'bold'), relief='sunken')
entryPhone.place(x=260, y=140)
valid_phoneno = window.register(phonevalidate)
entryPhone.config(validate="key", validatecommand=(valid_phoneno, '%P'))



entryEmail = Entry(window, fg='black', bg='white',font=('Times New Roman', 12, 'bold'), relief='sunken')
entryEmail.place(x=260, y=180)

button_p = Button(window, text='Click', command=validateAllfeilds)
button_p.place(x = 300, y = 250)
window.mainloop()
