from tkinter import *
from tkinter import messagebox
import mysql.connector
import time

def forgot():
    fwin = Tk()
    fwin.geometry("300x200")
    fwin.title("Forgot Password")
    fwin.resizable(0,0)
    # database connection
    conn = mysql.connector.connect(user='root', password='{NewPassword}', host='localhost',
                                   auth_plugin='mysql_native_password',
                                   database='surveillance')
    cursor = conn.cursor()

    label_background = Label(fwin, bg="light blue", justify='center',
                   font=('arial', 16, "bold"), height=60, width=150).pack()
    label_phone = Label(fwin, text="Phone No.", fg="black", bg="light blue",
                      font=("Times New Roman", 12)).place(x=75, y=30)
    entry_phone = Entry(fwin, fg='black', bg='light blue',font=('Times New Roman', 12, 'bold'), relief='sunken')
    entry_phone.place(x=75, y=55)
    def display():
        p = entry_phone.get()
        print(p)
        cursor.execute("Select password from admin where phone=%s", (p,))
        my_result = cursor.fetchall()
        if my_result != []:
            fwin.destroy()
            messagebox.showinfo(title="FORGOT PASSWORD",message="YOUR PASSWORD IS : "+my_result[0][0])
        else:
            fwin.destroy()
            messagebox.showinfo(title="FORGOT PASSWORD",message="USER NOT FOUND")

    button_Clickme = Button(fwin, text='Click Me!', fg='black', bg='light blue', font=("Times New Roman", 12, 'bold'),
                            relief='raised', justify='center', command=display).place(x=115, y=100)
    fwin.mainloop()
    return
