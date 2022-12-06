from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk
import tkinter as tk


class forget_pass:
    def __init__(self, window):
        self.window = window
        # window.geometry("800x700+350+300")
        self.window.title('Reset password')

        w = Label(window, text='Smart Attendance system', font=30)
        w.place(relx=0.47, rely=0.05, anchor=CENTER)

        frame = Frame(window)
        frame.pack(fill=BOTH, expand=True)

        self.img = ImageTk.PhotoImage(Image.open("og_bg.jpg"))

        s = ttk.Label(frame, image=self.img)
        s.pack(fill=BOTH, expand=True)

        label = tk.Label(window, text="Reset Password", bg="white", fg="black", font=('calibre', 17, 'bold'))
        label.place(x=600, y=80)

        Username = tk.Label(window, text="Username/email", bg="white", fg="black", font=('calibre', 15, 'normal'))
        Username.place(x=510, y=140)

        self.txtuser = tk.Entry(window, width=30, fg="black", font=('calibre', 12, 'normal'), bd=0)
        self.txtuser.place(x=530, y=180, height=32)
        Frame(window, width=300, height=2, bg='orchid1').place(x=530, y=205)

        Password = tk.Label(window, text="New Password", bg="white", fg="black", font=('calibre', 15, 'normal'))
        Password.place(x=510, y=240)

        self.txtpass = tk.Entry(window, width=25, fg="black", font=('calibre', 12, 'normal'), show="*", bd=0)
        self.txtpass.place(x=530, y=280, height=32)
        Frame(window, width=300, height=2, bg='orchid1').place(x=530, y=305)

        con_Password = tk.Label(window, text="Confirm Password", bg="white", fg="black", font=('calibre', 15, 'normal'))
        con_Password.place(x=510, y=340)

        self.txtcon_pass = tk.Entry(window, width=34, bd=0, fg="black", font=('calibre', 12, 'normal'), show="*")
        self.txtcon_pass.place(x=530, y=380, height=32)
        Frame(window, width=300, height=2, bg='orchid1').place(x=530, y=405)

        reset = Button(window, text="Reset", width=10, bg="pink", font=('calibre', 15, 'normal'),
                       command=self.change_password)
        reset.place(x=620, y=450, height=30)

    def change_password(self):
        if self.txtuser.get() == '' or self.txtpass.get() == '' or self.txtcon_pass.get() == '':
            messagebox.showerror("Error", 'All field required')
        elif self.txtpass.get() != self.txtcon_pass.get():
            messagebox.showerror("Error", 'Password do not match')
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = self.txtuser.get()
                my_cursor.execute(query, (value,))
                row = my_cursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid username or password", parent=window)
                else:
                    my_cursor.execute('update register set pass=%s,verifypass=%s where email=%s', (
                        self.txtpass.get(),
                        self.txtcon_pass.get(),
                        self.txtuser.get()
                    ))

                conn.commit()
                conn.close()
                messagebox.showinfo('Success', 'Password is reset, login with new password', parent=self.window)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.window)

    def close_win(self):
        window.destroy()

if __name__ == "__main__":
    window = Tk()
    obj = forget_pass(window)
    window.mainloop()
