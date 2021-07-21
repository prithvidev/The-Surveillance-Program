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


def att():
    KNOWN_FACES_DIR = 'known'
    TOLERANCE = 0.4
    FRAME_THICKNESS = 3
    FONT_THICKNESS = 2
    MODEL = 'cnn'  # default: 'hog', other one can be 'cnn' - CUDA accelerated (if available) deep-learning pretrained model


    video=cv2.VideoCapture(0)


    print('Loading known faces...')
    known_faces = []
    known_names = []

    # We oranize known faces as subfolders of KNOWN_FACES_DIR
    # Each subfolder's name becomes our label (name)
    for name in os.listdir(KNOWN_FACES_DIR):

        image = face_recognition.load_image_file(f'{KNOWN_FACES_DIR}/{name}')


            # Always returns a list of found faces, for this purpose we take first face only (assuming one face per image as you can't be twice on one image)
        encoding = face_recognition.face_encodings(image)[0]

            # Append encodings and name
        known_faces.append(encoding)
        known_names.append(name.split('.')[0][:-1])


    print('Processing unknown faces...')
    # Now let's loop over a folder of faces we want to label
    match = None
    while True:
        ret, image=video.read()
        locations = face_recognition.face_locations(image)


        # Now since we know loctions, we can pass them to face_encodings as second argument
        # Without that it will search for faces once again slowing down whole process
        encodings = face_recognition.face_encodings(image, locations)

        # We passed our image through face_locations and face_encodings, so we can modify it
        # First we need to convert it from RGB to BGR as we are going to work with cv2


        # But this time we assume that there might be more faces in an image - we can find faces of dirrerent people
        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):


            # We use compare_faces (but might use face_distance as well)
            # Returns array of True/False values in order of passed known_faces
            results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE)
            print(results)
            # Since order is being preserved, we check if any face was found then grab index
            # then label (name) of first matching known face withing a tolerance

            if True in results:  # If at least one is true, get a name of first of found labels
                match=(known_names[results.index(True)])
                print(f' - {match} from {results}')
                print(match)
                #print(face_location,'kkkk')

                # Each location contains positions in order: top, right, bottom, left
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])



                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, (0,255,0), FRAME_THICKNESS)

                # Now we need smaller, filled grame below for a name
                # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, ( 0,255,0), cv2.FILLED)

                # Wite a name
                cv2.putText(image, match, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), FONT_THICKNESS)
            else:
                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), FRAME_THICKNESS)

                # Now we need smaller, filled grame below for a name
                # This time we use bottom in both corners - to start from bottom and move 50 pixels down
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                # Paint frame
                cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), cv2.FILLED)

                # Wite a name
                cv2.putText(image, 'Unknown', (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (200, 200, 200), FONT_THICKNESS)
        # Show image
        cv2.imshow('Camera', image)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    del(video)
    cv2.destroyAllWindows()


    if match==None:
        messagebox.showinfo(title="Surviellance Program", message="UNIDENTIFIED PERSON")
        return
    else:
        detect_mask_video.dm(match)
    '''    
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

    cursor.execute("select * from employee where empid=%s",(x[0],))
    my_result = cursor.fetchall()
    conn.commit()

    #labels
    label_title = Label(window, text="EMPLOYEE DETAILS", fg='black', bg='light blue',
                     font=('Times New Roman', 22,'bold','underline'))
    label_title.place(x=85, y=1)

    '''
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
    #label_image = Label(window, text="Employee Image", fg='black', bg='white',
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

    #date and time stamp
    emp_id=my_result[0][0]
    emp_name=my_result[0][1]

    d= datetime.datetime.now()
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

    #attendance function
    def markyourattendance():
        messagebox.showinfo(title="Surveillance Program", message="PLEASE CONFIRM THAT YOU WEAR A MASK!! THIS IS MANDATORY")
        
        cursor.execute("insert into attendance(empid, empname, Date, Time, On_Time_or_Late)values(%s,%s,%s,%s,%s)",(emp_id,emp_name,date,time,h))
        conn.commit()
        messagebox.showinfo(title="Surviellance System",message="Attendance Marked")

    #button
    mark = Button(window, text='Mark Your Attendance', fg='black', bg='light blue', font=("Times New Roman", 12, 'bold'),
                            relief='raised', justify='center',command=markyourattendance)
    mark.place(x=160, y=360)
    
    window.mainloop()
    '''