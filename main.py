from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
from time import strftime
import face_recognition
import numpy as np
from datetime import datetime


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Smart Attendance system")

        self.var_course = StringVar()
        self.var_enrollment = StringVar()
        self.var_name = StringVar()
        self.var_sem = StringVar()

        w = Label(root, text='Smart Attendance system', font=30)
        w.place(relx=0.47, rely=0.05, anchor=CENTER)

        frame = Frame(root, bg='white')
        frame.pack(fill=BOTH, expand=True)

        # self.img = ImageTk.PhotoImage(Image.open("background.jpg"))

        s = ttk.Label(frame)
        s.pack(fill=BOTH, expand=True)

        # Label Widget
        b = Label(root, bg="#f5f5f5", bd=2, relief=RAISED, background="SkyBlue1")
        b.place(relx=0.03, rely=0.05, relheight=0.8, relwidth=0.4)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(b, fg='black', background="SkyBlue1", font=('DS - Digital', 15, 'normal'))
        lbl.place(relx=0.4, rely=0.9, width=120, height=50)
        time()

        label = Label(b, text="For Registered Students", font=('calibre', 20, 'normal'), fg="black",
                      background="SkyBlue1")
        label.place(rely=0.02, relx=0.28)

        text1 = Button(b, text="Take Attendance", command=self.face_recognizer, fg="black",
                       background="yellow",
                       width=30, font=('calibre', 20, 'normal'))
        text1.pack(expand=False, padx=90, pady=80)

        text2 = Label(b, text="Attendance sheet", fg="black", font=('calibre', 20, 'normal'),
                      background="SkyBlue1")
        text2.place(relx=0.5, rely=0.28, anchor=CENTER)

        tableFrame = Frame(b, bd=3, relief=RIDGE)
        tableFrame.place(x=5, y=210, width=595, height=250)

        scroll_x = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.studentTable = ttk.Treeview(tableFrame, columns=("Course", "Sem", "Names", "Enrollment"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)

        self.studentTable.heading("Course", text="Course")
        self.studentTable.heading("Sem", text="Sem")
        self.studentTable.heading("Names", text="Names")
        self.studentTable.heading("Enrollment", text="Enrollment")
        # self.studentTable.heading("Attendance", text="Attendance")

        self.studentTable["show"] = "headings"

        self.studentTable.column('Course', width=100, anchor=CENTER)
        self.studentTable.column('Sem', width=100, anchor=CENTER)
        self.studentTable.column('Names', width=100, anchor=CENTER)
        self.studentTable.column('Enrollment', width=100, anchor=CENTER)
        # self.studentTable.column('Attendance', width=100, anchor=CENTER)

        self.studentTable.pack(expand=1, fill=BOTH, anchor=CENTER)
        self.fetch_data()

        Quit = Button(b, text="Exit", command=self.close_win, font=('calibre', 17, 'normal'), fg="black", background="yellow")
        Quit.place(rely=0.83, relx=0.5, relwidth=0.15, anchor=CENTER)

        # Separator object
        separator = ttk.Separator(root, orient='vertical')
        separator.place(relx=0.47, relheight=1)

        # Label Widget
        a = Label(root, bg="#f5f5f5", bd=2, relief=RAISED, background="SkyBlue1")
        a.place(relx=0.51, rely=0.05, relheight=0.8, relwidth=0.4)

        label = Label(a, text="For New Registrations", bd=2, font=('calibre', 20, 'normal'), fg="black",
                      background="SkyBlue1")
        label.place(rely=0.02, relx=0.3)

        # Course
        enterCourse = Label(a, text="Course", font=30, fg="black", background="SkyBlue1")
        enterCourse.place(anchor="n", relx=0.24, rely=0.13)

        courses_combo = ttk.Combobox(a, font=('calibre', 13, 'normal'), state="readonly", textvariable=self.var_course)
        courses_combo["values"] = ("Select Course", "DDMCA", "BCA", "MCA")
        courses_combo.current(0)
        courses_combo.place(anchor="e", relx=0.43, rely=0.2, relheight=0.05, relwidth=0.4)

        # Semester
        enterSem = Label(a, text="Semester", font=30, fg="black", background="SkyBlue1")
        enterSem.place(anchor="w", relx=0.64, rely=0.15)

        sem_combo = ttk.Combobox(a, font=('calibre', 13, 'normal'), state="readonly", textvariable=self.var_sem)
        sem_combo["values"] = ("Select Sem", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
        sem_combo.current(0)
        sem_combo.place(anchor="w", relx=0.53, rely=0.2, relheight=0.05, relwidth=0.4)

        # Name
        enterName = Label(a, text="Enter Name", font=30, fg="black", background="SkyBlue1")
        enterName.place(anchor="e", relx=0.34, rely=0.3)

        text4 = Label(a, background="yellow", font=20)
        text4 = Entry(a, textvariable=self.var_name, font=('calibre', 15, 'normal'))
        text4.place(relx=0.43, rely=0.35, anchor="e", relheight=0.05, relwidth=0.4)

        # Id
        enterId = Label(a, text="Enter Enrollment", font=30, fg="black", background="SkyBlue1")
        enterId.place(anchor="w", relx=0.58, rely=0.3)

        text3 = Label(a, background="yellow", font=20)
        text3 = Entry(a, textvariable=self.var_enrollment, font=('calibre', 15, 'normal'))
        text3.place(relx=0.53, rely=0.35, anchor="w", relheight=0.05, relwidth=0.4)

        takeImage = Label(a, text="Take Image", font=30, fg="black", background="SkyBlue1")
        takeImage.place(anchor=CENTER, relx=0.5, rely=0.45)

        photo = Image.open(r'photo.png')
        resize_image = photo.resize((200, 200), Image.Resampling.LANCZOS)
        self.my_image = ImageTk.PhotoImage(resize_image)

        photo = Button(a, width=50, image=self.my_image, command=self.upload_img, compound=CENTER,
                       background='tan')
        photo.place(relx=0.5, rely=0.5, anchor="n", relheight=0.3, relwidth=0.3)

        profile = Button(a, text="Save Profile", command=self.add_Data, fg="black", background="yellow",
                         font=('calibre', 17, 'normal'))
        profile.place(relx=0.5, rely=0.85, anchor="n", relheight=0.08, relwidth=0.5)

    # ===================== database connecting function => adding data in table ===============================================================

    def add_Data(self):
        if self.var_course.get() == "Select Course" or self.var_sem.get() == "Select Sem" or self.var_name.get() == "" or self.var_enrollment.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                if self.var_course.get() == "DDMCA":
                    my_cursor.execute("insert into ddmca values(%s,%s,%s,%s)", (
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_enrollment.get()
                    ))
                elif self.var_course.get() == "BCA":
                    my_cursor.execute("insert into bca values(%s,%s,%s,%s)", (
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_enrollment.get()
                    ))
                else:
                    my_cursor.execute("insert into mca values(%s,%s,%s,%s)", (
                        self.var_course.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_enrollment.get()
                    ))
                conn.commit()
                # self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Profile Saved", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                       database="face_recognition")
        my_cursor = conn.cursor()

        if self.var_course.get() == "DDMCA":
            query = "select * from ddmca"
            # my_cursor.execute("select * from ddmca")
        elif self.var_course.get() == "BCA":
            query = "select * from bca"
            # my_cursor.execute("select * from bca")
        else:
            query = "select * from mca"
            # my_cursor.execute("select * from mca")

        my_cursor.execute(query)
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.studentTable.delete(*self.studentTable.get_children())
            for i in data:
                self.studentTable.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ====================marking the attendance==============================================================================

    def markAttendance(self, name):
        with open('Attendances.csv', 'r+') as f:
            my_data = f.readline()
            name_lst = []
            for line in my_data:
                entry = line.split(',')
                name_lst.append(entry[0])
            if name not in name_lst:
                now = datetime.now()
                dString = now.strftime('%H:%M:%S')
                dt = now.strftime('%d:%m:%Y')
                f.writelines(f'\n{name},{dt},{dString},Present')
            else:
                messagebox.showinfo("Success", "Marked already")

    # def load_file(self):
    #     csv_list = []
    #     # filename = "Attendances.csv"
    #     with open('Attendances.csv') as Attendances:
    #         reader = csv.reader(Attendances, delimiter=',')
    #         next(reader)
    #         for i in reader:
    #             csv_list.append(i)
    #         return csv_list

    # new_list = load_file('Attendances.csv')

    # ========================face detection function =================================================================

    def face_recognizer(self):
        path = 'images'
        studentImg = []
        studentName = []
        myList = os.listdir(path)
        for cl in myList:
            curimg = cv2.imread(f'{path}/{cl}')
            studentImg.append(curimg)
            studentName.append(os.path.splitext(cl)[0])
        print(studentName)

        def findEncoding(images):
            encodeList = []
            for img in images:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                encoded_face = face_recognition.face_encodings(img)[0]
                encodeList.append(encoded_face)
            return encodeList

        EncodeList = findEncoding(studentImg)
        print('all encodings done')

        vid = cv2.VideoCapture(0)

        while True:
            success, frame = vid.read()
            Smaller_frames = cv2.resize(frame, (0, 0), None, 0.25, 0.25)

            facesInFrame = face_recognition.face_locations(Smaller_frames)
            encodeFacesInFrame = face_recognition.face_encodings(Smaller_frames, facesInFrame)

            for encodeFace, faceloc in zip(encodeFacesInFrame, facesInFrame):
                matches = face_recognition.compare_faces(EncodeList, encodeFace)
                facedis = face_recognition.face_distance(EncodeList, encodeFace)
                # print(facedis)
                matchIndex = np.argmin(facedis)

                if matches[matchIndex]:
                    name = studentName[matchIndex].upper()
                    y1, x2, y2, x1 = faceloc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
                    cv2.rectangle(frame, (x1, y2 - 25), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 3)
                    self.markAttendance(name)
            cv2.imshow('video', frame)
            if cv2.waitKey(1) == 13:
                break
        vid.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Attendance marked")

    # ===========training data function ================================================================================

    def upload_img(self):

        video = cv2.VideoCapture(0)
        a = 1
        while True:
            try:
                a = a + 1
                ret, frame = video.read()
                cv2.imshow("Camera", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                if self.var_name.get() == "" and self.var_course.get() == "Select Course":
                    messagebox.showerror("Error", "All fields are required")
                    break
                else:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                                   database="face_recognition")
                    my_cursor = conn.cursor()
                    if self.var_course.get() == "DDMCA":
                        sql = "SELECT Name FROM ddmca "
                    elif self.var_course.get() == "BCA":
                        sql = "SELECT Name FROM bca"
                    else:
                        sql = "SELECT Name FROM mca"

                    my_cursor.execute(sql)
                    mit = my_cursor.fetchone()
                    # mit = mit.replace('(', '').replace(')', '')
                    mit = "".join(mit)
                    file_name_path = f"images/{mit}" + ".jpg"

                    cv2.imwrite(file_name_path, frame)
            except KeyboardInterrupt:
                continue

        video.release()
        cv2.destroyAllWindows()

    def close_win(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
