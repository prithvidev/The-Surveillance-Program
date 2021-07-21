from tkinter import *
from tkinter import messagebox
import mysql.connector
from addnew import addEmp
from motion import motionD
from attendance import att
from visitor_form import visitor
from detect_mask_visitor import dm1
#main window

def f2(i):
    window = Tk()
    window.geometry("500x400")
    window.title("SURVEILLANCE PROGRAM")
    window.resizable(0, 0)
    window.config(bg='light blue')
    p=i
    print(p)
    label_name= Label(window,text=p,fg='black', bg='light blue', justify='center',
                  font=('Times new roman', 16, "bold"))
    label_name.place(x=36, y=10)

    buttonMonitoring = Button(window, text='     MONITORING     ', justify='center', fg='black', bg='light blue',
                        font=('Times New Roman', 17, 'bold'), relief='ridge', command=motionD).place(x=123, y=80)

    buttonAttendance = Button(window, text='     ATTENDANCE     ', justify='center', fg='black', bg='light blue',
                              font=('Times New Roman', 17, 'bold'), relief='ridge', command= att).place(x=123, y=166)

    buttonADD = Button(window, text='ADD NEW EMPLOYEE', justify='center', fg='black', bg='light blue',
                        font=('Times New Roman', 16, 'bold'), relief='ridge', command=addEmp).place(x=120, y=252)

    buttonADD = Button(window, text='       VISITOR FORM       ', justify='center', fg='black', bg='light blue',
                       font=('Times New Roman', 16, 'bold'), relief='ridge', command=visitor).place(x=120, y=340)

    window.mainloop()

#extras
#label_image = PhotoImage(file="C:\\Users\\Pragya.DESKTOP-3UL0L63\\Downloads\\cctv(2).png")
    #label1 = Label(window, bg='light blue', image=label_image, justify='center',
     #              font=('arial', 16, "bold"), height=130, width=150).place(x=360, y=5)