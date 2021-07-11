from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector

class SignUp:
    def __init__(self, root):
        self.window = root
        self.window.title("Sign Up")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg = "white")

        self.bg_img = ImageTk.PhotoImage(file="../../PycharmProjects/MySQL with Python/Images/photo1.jpeg")
        background = Label(self.window, image=self.bg_img).place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.window, bg="white")
        frame.place(x=300, y=100, width=700, height=600)

        title1 = Label(frame, text="Sign Up", font=("times new roman", 25, "bold"), bg="white").place(x=20, y=10)
        title2 = Label(frame, text="Enter User Details", font=("times new roman", 13), bg="white", fg="gray").place(x=20, y=50)

        f_name = Label(frame, text="First name", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=100)
        l_name = Label(frame, text="Last name", font=("helvetica", 15, "bold"), bg="white").place(x=240, y=100)

        l_Identity = Label(frame, text="Identity", font=("helvetica", 15, "bold"), bg="white").place(x=490, y=100)
        l_Phone = Label(frame, text="Phone", font=("helvetica", 15, "bold"), bg="white").place(x=490, y=180)

        l_kinname = Label(frame, text="Kin Name", font=("helvetica",15,"bold"),bg="white").place(x=490, y=260)

        l_kinname = Label(frame, text="Kin Number", font=("helvetica", 15, "bold"), bg="white").place(x=490, y=340)

        self.fname_txt = Entry(frame, font=("arial"))
        self.fname_txt.place(x=20, y=130, width=200)

        self.lname_txt = Entry(frame, font=("arial"))
        self.lname_txt.place(x=240, y=130, width=200)
        self.Identity_txt = Entry(frame, font=("arial"))
        self.Identity_txt.place(x=480, y=130, width=200)

        self.Phone_txt = Entry(frame, font=("arial"))
        self.Phone_txt.place(x=480, y=210, width=200)

        self.kin_name_txt = Entry(frame, font=("arial"))
        self.kin_name_txt.place(x=480, y=290, width=200)

        self.kin_number_txt = Entry(frame, font=("arial"))
        self.kin_number_txt.place(x=480, y=370, width=200)

        email = Label(frame, text="Email", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=180)

        self.email_txt = Entry(frame, font=("arial"))
        self.email_txt.place(x=20, y=210, width=420)

        sec_question = Label(frame, text="Security questions", font=("helvetica", 15, "bold"), bg="white").place(x=20, y=260)
        answer = Label(frame, text="Answer", font=("helvetica", 15, "bold"), bg="white").place(x=240, y=260)

        self.questions = ttk.Combobox(frame,font=("helvetica",13),state='readonly',justify=CENTER)
        self.questions['values'] = ("Select","What's your pet name?","Your first teacher name","Your birthplace", "Your favorite movie")
        self.questions.place(x=20,y=290,width=200)
        self.questions.current(0)

        self.answer_txt = Entry(frame,font=("arial"))
        self.answer_txt.place(x=240, y=290, width=200)

        password =  Label(frame, text="New password", font=("helvetica",15,"bold"),bg="white").place(x=20, y=340)

        self.password_txt = Entry(frame,font=("arial"))
        self.password_txt.place(x=20, y=370, width=420)

        self.terms = IntVar ()
        terms_and_con = Checkbutton(frame, text="I Agree The Terms & Conditions", variable=self.terms, onvalue=1,
                                     offvalue=0, bg="white", font=("times new roman", 12)).place(x=210, y=420)

        self.signup = Button(frame, text="Sign Up", command=self.signup_func, font=("times new roman", 18, "bold"), bd=0, cursor="hand2", bg="green2", fg="white").place(x=210, y=470, width=250)

    def signup_func(self):
        if (format(self.fname_txt.get())) == "" or format(self.lname_txt.get())=="" or format(self.email_txt.get()) == "" or format(self.questions.get()) == "Select" or format(self.answer_txt.get()) == "" or format(self.password_txt.get()) == "" or format(self.Phone_txt.get()) == '' or format(self.Identity_txt.get()) == '' or format(self.kin_name_txt.get()) == '' or format(self.kin_number_txt.get()) == '':
            messagebox.showerror("Error!", "Sorry!, All fields are required",parent=self.window)

        elif self.terms.get() == 0:
            messagebox.showerror("Error!", "Please Agree with our Terms & Conditions", parent=self.window)

        else:
            try:
                connection = mysql.connector.connect(host="127.0.0.1", user="lifechoices", password="@Lifechoices1234", database="LifeChoicesOnline", auth_plugin='mysql_native_password')
                cur = connection.cursor()
                cur.execute("select * from Userdetails where EmailID=%s", self.email_txt.get())
                row = cur.fetchone()

                #Check if entered email id is already exists or not.
                if row != None:
                    messagebox.showerror("Error!", "The email id is already exists, please try again with another email id", parent=self.window)
                else:
                    cur.execute("INSERT INTO Userdetails (Name,Surname,IdentityNumber,PhoneN,KinName,KinNumber,EmailID,securityQ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                    (self.fname_txt.get(),
                                     self.lname_txt.get(),
                                     self.Identity_txt.get(),
                                     self.Phone_txt.get(),
                                     self.password_txt.get()),
                                     self.email_txt.get(),
                                     self.kin_name_txt.get(),
                                     self.kin_number_txt.get())
                    connection.commit()
                    connection.close()
                    messagebox.showinfo("Congratulations!", "Register Successful", parent=self.window)
                    self.reset_fields()
                    import login_page
            except Exception as e:
                messagebox.showerror("Error!", f"Error due to {str(e)}", parent=self.window)

    def reset_fields(self):
        self.fname_txt.delete(0, END)
        self.lname_txt.delete(0, END)
        self.email_txt.delete(0, END)
        self.questions.current(0)
        self.answer_txt.delete(0, END)
        self.password_txt.delete(0, END)
        self.Identity_txt.delete(0, END)
        self.Phone_txt.delete(0, END)
        self.kin_name_txt.delete(0, END)
        self.kin_number_txt.delete(0, END)


root = Tk()
obj = SignUp(root)
root.mainloop()
