import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import mysql.connector
master = Tk()
master.geometry('700x700')
master.title('Register Username')

class Registration:
    def __init__(self):
        self.input_text = StringVar
        self.master = master
        self.header = Label(master, text='Register User Here', foreground='black', font=('serif', 25))
        self.header.place(x=180, y=10)

        self.Name = Label(master, text='Name', foreground='black', font=('Arial', 20))
        self.Name.place(x=20, y=100)
        self.name_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.name_entry.place(x=250, y=100)

        self.Surname = Label(master, text='Surname', foreground='black', font=('Arial', 20))
        self.Surname.place(x=20, y=170)
        self.surname_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.surname_entry.place(x=250, y=170)

        self.Password = Label(master, text='Password', foreground='black', font=('Arial', 20))
        self.Password.place(x=20, y=240)
        self.Password_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.Password_entry.place(x=250, y=240)

        self.ID_number = Label(master, text='ID Number', foreground='black', font=('Arial', 20))
        self.ID_number.place(x=20, y=310)
        self.ID_number_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.ID_number_entry.place(x=250, y=310)

        self.Phone_number = Label(master, text='Phone Number', foreground='black', font=('Arial', 20))
        self.Phone_number.place(x=20, y=380)
        self.Phone_number_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.Phone_number_entry.place(x=250, y=380)

        self.kin_name = Label(master, text="Next of kin's Name", foreground='black', font=('Arial', 20))
        self.kin_name.place(x=20, y=450)
        self.kin_name_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.kin_name_entry.place(x=250, y=450)

        self.kin_number = Label(master, text="Next of kin's Cell", foreground='black', font=('Arial', 20))
        self.kin_number.place(x=20, y=520)
        self.kin_number_entry = ttk.Entry(master, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.kin_number_entry.place(x=250, y=520)

        self.register_btn = tkinter.Button(master, text='Register', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=self.database_register)
        self.register_btn.place(x=150, y=600)

        self.register_btn = tkinter.Button(master, text='Login', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 20, 'bold'), cursor='hand2', command=self.BacktoExit)
        self.register_btn.place(x=350, y=600)

    def BacktoExit(self):
        master.destroy()
        import main

    def database_register(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        password = self.Password_entry.get()
        identity = self.ID_number_entry.get()
        phone_number = self.Phone_number_entry.get()
        kin_name = self.kin_name_entry.get()
        kin_cell = self.kin_number_entry.get()

        if self.name_entry.get() == '' or self.ID_number_entry.get() == '' or self.surname_entry.get() == '' or self.Phone_number_entry.get() == '' or self.Password_entry.get() == '':
            messagebox.showerror('STATUS', "PLEASE Enter Valid Details")
        else:
            con = mysql.connector.connect(user='sql6423123', password='EYQeBzmlvU', port='3306', host='sql6.freesqldatabase.com', database='sql6423123', auth_plugin='mysql_native_password')
            cursor = con.cursor()
            cursor.execute("INSERT INTO `Life Choices Online` VALUES('" + name + "','" + surname + "', '" + password + "', '" + identity + "', '" + phone_number + "', '" + kin_name + "', '" + kin_cell + "' )")
            cursor.execute('commit')
            messagebox.showinfo("PERMISSION", "YOU HAVE REGISTERED SUCCESSFULLY")
            self.name_entry.delete(0, END)
            self.surname_entry.delete(0, END)
            self.Password_entry.delete(0, END)
            self.ID_number_entry.delete(0, END)
            self.Phone_number_entry.delete(0, END)
            self.kin_name_entry.delete(0, END)
            self.kin_number_entry.delete(0, END)
            con.close();
            master.destroy()
            import main



a = Registration()
master.mainloop()
