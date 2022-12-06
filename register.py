from tkinter import *
import mysql.connector
from tkinter import messagebox, ttk
from PIL import ImageTk, Image


class Register:
    def __init__(self, root):
        self.root = root

        root.geometry("1550x900+0+0")
        root.title("registration form")

        self.var_dept = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_country = StringVar()
        self.var_securityQ = StringVar()
        self.var_pass = StringVar()
        self.var_verifypass = StringVar()

        # frame = Frame(root, background="white")
        # frame.pack(fill=BOTH, expand=True)

        w = Label(root, text='Login page', font=30)
        w.place(relx=0.47, rely=0.05, anchor=CENTER)

        frame = Frame(root, bg='SkyBlue1')
        frame.pack(fill=BOTH, expand=True)

        photo1 = Image.open(r'register.jpg')
        resize_image1 = photo1.resize((1200, 700), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(resize_image1)
        # self.img = ImageTk.PhotoImage(Image.open("register.jpg"))

        b = ttk.Label(frame, image=self.img)
        b.place(relx=0.1, rely=0.04)

        label = Label(b, text="Registration Form", width=15, font=("arial", 17, "bold"), bg='white', fg='oliveDrab4')
        label.place(x=780, y=80)

        lb1 = Label(b, text="Department", width=10, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        lb1.place(x=650, y=150)
        en1 = Entry(b, textvariable=self.var_dept, font=('calibre', 13, 'normal'))
        en1.place(x=830, y=155, width=200, height=30)

        lb2 = Label(b, text="Dept.Head Name", width=15, font=('calibre', 14, 'normal'), bg='white', fg='midnight blue')
        lb2.place(x=645, y=200)
        en2 = Entry(root, textvariable=self.var_name, font=('calibre', 13, 'normal'))
        en2.place(x=985, y=240, width=200, height=30)

        lb3 = Label(b, text="Email", width=10, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        lb3.place(x=650, y=256)
        en3 = Entry(b, textvariable=self.var_email, font=('calibre', 13, 'normal'))
        en3.place(x=830, y=260, width=200, height=30)

        lb4 = Label(b, text="Contact Number", width=13, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        lb4.place(x=650, y=300)
        en4 = Entry(b, textvariable=self.var_contact, font=('calibre', 13, 'normal'))
        en4.place(x=830, y=305, width=200, height=30)

        lb5 = Label(b, text="College code", width=13, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        lb5.place(x=650, y=350)
        en5 = Entry(b, textvariable=self.var_securityQ, font=('calibre', 13, 'normal'))
        en5.place(x=830, y=350, width=200, height=30)

        # lb9 = Label(b, text="Select Country", width=13, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        # lb9.place(x=650, y=400)
        # courses_combo = ttk.Combobox(root, font=('calibre', 15, 'normal'), state="readonly",
        #                              textvariable=self.var_country)
        # courses_combo["values"] = (
        #     'Select Country', 'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Anguilla',
        #     'Antigua And Barbuda',
        #     'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
        #     'Bahrain',
        #     'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda',
        #     'Bhutan', 'Bolivia',
        #     'Bosnia And Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil',
        #     'British Virgin Islands',
        #     'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
        #     'Cape Verde',
        #     'Cayman Islands', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo',
        #     'Cook Islands',
        #     'Costa Rica', 'Croatia', 'Curacao', 'Cyprus', 'Czech Republic',
        #     'Democratic Republic Of The Congo',
        #     'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador',
        #     'Egypt',
        #     'El Salvador', 'Equatorial Guinea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji',
        #     'Finland',
        #     'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia',
        #     'Germany', 'Ghana',
        #     'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala',
        #     'Guernsey',
        #     'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary',
        #     'Iceland',
        #     'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle Of Man', 'Israel', 'Italy',
        #     'Ivory Coast',
        #     'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kosovo', 'Kuwait',
        #     'Kyrgyzstan',
        #     'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Libyan Arab Jamahiriya',
        #     'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macau', 'Macedonia',
        #     'Madagascar', 'Malawi',
        #     'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius',
        #     'Mexico',
        #     'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar',
        #     'Namibia',
        #     'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand',
        #     'Nicaragua',
        #     'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palestine', 'Panama',
        #     'Papua New Guinea',
        #     'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
        #     'Reunion',
        #     'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Kitts And Nevis',
        #     'Saint Lucia', 'Singapore',
        #     'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
        #     'Spain',
        #     'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Taiwan',
        #     'Tajikistan',
        #     'Tanzania', 'Tanzania, United Republic Of', 'Thailand', 'Togo', 'Tonga',
        #     'Trinidad And Tobago',
        #     'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay',
        #     'Uzbekistan',
        #     'Vanuatu', 'Venezuela', 'Vietnam', 'Wallis And Futuna', 'Yemen', 'Zambia',
        #     'Zimbabwe')
        # courses_combo.current(0)
        # courses_combo.place(x=985, y=430, width=200, height=30)

        lb6 = Label(b, text="Enter Password", width=13, font=('calibre', 15, 'normal'), bg='white', fg='midnight blue')
        lb6.place(x=650, y=450)
        en6 = Entry(b, show='*', textvariable=self.var_pass, font=('calibre', 13, 'normal'))
        en6.place(x=830, y=450, width=200, height=30)

        lb7 = Label(b, text="Re-Enter Password", width=15, font=('calibre', 15, 'normal'), bg='white',
                    fg='midnight blue')
        lb7.place(x=650, y=500)
        en7 = Entry(b, show='*', textvariable=self.var_verifypass, font=('calibre', 13, 'normal'))
        en7.place(x=830, y=500, width=200, height=30)

        register = Button(b, text="Register", width=15, command=self.register, bg="oliveDrab4",
                          font=('calibre', 15, 'bold'))
        register.place(x=800, y=560)

    def register(self):

        if self.var_dept.get() == "" or self.var_name.get() == "" or self.var_email.get() == "" or self.var_contact.get() == "" or self.var_pass.get() == "" or self.var_securityQ.get() == "" or self.var_country.get() == "" or self.var_verifypass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)

        elif self.var_pass.get() == self.var_verifypass.get():
            messagebox.showerror("Error", "Password do not match")

        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Donotdisturb14",
                                               database="face_recognition")
                my_cursor = conn.cursor()
                query = "select * from register where email=%s"
                value = self.var_email.get()
                my_cursor.execute(query, (value,))
                row = my_cursor.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "User already exist")
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (
                                      self.var_dept.get(),
                                      self.var_name.get(),
                                      self.var_email.get(),
                                      self.var_contact.get(),
                                      self.var_country.get(),
                                      self.var_securityQ.get(),
                                      self.var_pass.get(),
                                      self.var_verifypass.get(),
                                  ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered", parent=self.root)
            self.close_win()

    def close_win(self):
        root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
