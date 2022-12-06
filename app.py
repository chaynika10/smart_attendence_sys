from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
from main import Attendance
from register import Register
from forget_pass import forget_pass


def main():
    win = Tk()
    app = login(win)
    win.mainloop()


class login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x900+0+0")
        self.root.title("Smart Attendance system")

        w = Label(root, text='Login page', font=30)
        w.place(relx=0.47, rely=0.05, anchor=CENTER)

        frame = Frame(root, bg='SkyBlue1')
        frame.pack(fill=BOTH, expand=True)

        photo1 = Image.open(r'ba.png')
        resize_image1 = photo1.resize((1200, 700), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resize_image1)
        # self.img = ImageTk.PhotoImage(Image.open("ba.png"))

        b = ttk.Label(frame, image=self.img)
        b.place(relx=0.1, rely=0.04)

        # self.image = ImageTk.PhotoImage(Image.open("login_icon.png"))

        a = Label(b, bd=4, relief=RAISED, background="SkyBlue1")
        a.place(x=545, y=60, height=600, width=500)

        c = ttk.Label(a, text='Smart Attendance system', borderwidth=3, font=('calibre', 30, 'normal'),
                      background="SkyBlue1", foreground="black")
        c.place(relx=0.04, rely=0.05)

        # photo1 = Image.open(r'login_icon.png')
        # resize_image1 = photo1.resize((130, 110), Image.Resampling.LANCZOS)
        # self.login_i = ImageTk.PhotoImage(resize_image1)
        #
        # label1 = Label(image=self.login_i)
        # label1.place(x=710, y=150, height=90, width=100)

        login = tk.Label(a, text="WELCOME!", bg="SkyBlue1", fg="Yellow", bd=3, font=('calibre', 25, 'bold'),
                         background="SkyBlue1")
        login.place(relx=0.25, rely=0.2, relheight=0.05, relwidth=0.5)

        Username = tk.Label(a, text="Email -", bg="SkyBlue1", fg="black", font=('calibre', 17, 'normal'))
        Username.place(rely=0.32, relwidth=0.4, relheight=0.1)

        self.txtuser = tk.Entry(a, width=35, bg="white", fg="black", font=('calibre', 15, 'normal'))
        self.txtuser.place(relx=0.13, rely=0.42, relwidth=0.75, relheight=0.06)

        Password = tk.Label(a, text="Password -", bg="SkyBlue1", fg="black", font=('calibre', 17, 'normal'))
        Password.place(relx=0, rely=0.52, relwidth=0.4, relheight=0.1)

        self.txtpass = tk.Entry(a, width=35, bg="white", fg="black", font=('calibre', 15, 'normal'), show="*")
        self.txtpass.place(relx=0.13, rely=0.62, relwidth=0.75, relheight=0.06)

        forget_password = tk.Button(a, text="Forget Password?", command=self.forget_pass, bg="SkyBlue1", borderwidth=0,
                                    fg="black",
                                    font=('calibre', 12, 'normal'), activebackground="DodgerBlue4")
        forget_password.place(relx=0.04, rely=0.72, relwidth=0.3, relheight=0.05)

        new_reg = tk.Button(a, text="Register new Account?", command=self.register_window, bg="SkyBlue1", borderwidth=0,
                            fg="black", font=('calibre', 12, 'normal'), activebackground="SkyBlue1")
        new_reg.place(relx=0.64, rely=0.72, relwidth=0.33, relheight=0.05)

        submitbtn = tk.Button(a, text="Login", command=self.logintodb, bg="yellow", fg="black",
                              font=('calibre', 20, 'normal'))
        submitbtn.place(relx=0.35, rely=0.8, relwidth=0.27, relheight=0.09)

    def logintodb(self):
        if self.txtuser.get() == "" and self.txtpass.get() == "":
            messagebox.showerror("Error", 'All field required')

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                           database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s",
                              (
                                  self.txtuser.get(),
                                  self.txtpass.get()
                              ))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                open_main = messagebox.askyesno("YesNo", "Authorised person")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Attendance(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            # self.clear()
            conn.close()

    def forget_pass(self):
        self.new_window = Toplevel()
        self.app = forget_pass(self.new_window)

    def register_window(self):
        self.new_window = Toplevel()
        self.app = Register(self.new_window)


if __name__ == "__main__":
    main()
