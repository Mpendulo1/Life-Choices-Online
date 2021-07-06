import tkinter
from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import mysql.connector

root = Tk()
root.geometry('600x500')
root.title('Login Centre')

class MainScreen:
    def __init__(self):
        self.root = root
        self.input_text = StringVar
        self.header = Label(self.root, text='Enter Your Details', foreground='black', font=('serif', 25))
        self.header.place(x=150, y=10)
        # Username Labels and Entries
        self.username = Label(self.root, text='Username', foreground='black', font=('Arial', 20))
        self.username.place(x=220, y=100)
        self.username_entry = ttk.Entry(self.root, textvariable=self.input_text, justify=CENTER, font=('courier', 20), bd=1)
        self.username_entry.place(x=140, y=150)
        # Password Label and Entries
        self.password = Label(self.root, text='Password', foreground='black', font=('Arial', 20))
        self.password.place(x=220, y=200)
        self.password_entry = ttk.Entry(self.root, textvariable=self.input_text, justify=CENTER, font=('Courier', 20), show="**", bd=1)
        self.password_entry.place(x=140, y=250)
        # Buttons
        self.login_button = tkinter.Button(self.root, text='Login', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', command=self.DatabaseLogin)
        self.login_button.place(x=140, y=350)
        self.register_button = tkinter.Button(self.root, text='Register', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', command=self.register)
        self.register_button.place(x=250, y=350)
        # self.admin_button = tkinter.Button(self.root, text='Admin', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2')
        # self.admin_button.place(x=390, y=350)

    def DatabaseLogin(self):
        global userID
        try:
            connection = mysql.connector.connect(user='sql6423123', password='EYQeBzmlvU', port='3306', host='sql6.freesqldatabase.com', database='sql6423123', auth_plugin='mysql_native_password')
            curs = connection.cursor()
        except:
            print('You are not connected to the server')
        else:
            name = self.username_entry.get()
            password = self.password_entry.get()
            curs = connection.cursor()
            query = ('SELECT Name, Password FROM `Life Choices Online` ')
            for (Name, Password) in curs:
                if name == Name and password == Password:
                    messagebox.showinfo('Welcome' + name, 'Login Successful, Enjoy Your Day')
                    curs.close()
                    connection.close()
                    root.destroy()



        # if self.username_entry.get() == '':
        #     messagebox.showerror('Enter Username', 'Please Enter A Username')
        # elif self.password_entry.get() == '':
        #     messagebox.showerror('Enter Password', 'Please Enter A Valid Password')
        # elif self.password_entry.get() == '' or self.username_entry.get() == '':
        #     messagebox.showerror('Inputs Empty', 'Please Enter Valid Details!')
        # else:
        #     my_database = mysql.connector.connect(user='sql6423123', password='EYQeBzmlvU', port='3306', host='sql6.freesqldatabase.com', database='sql6423123', auth_plugin='mysql_native_password')
        #     mycursor = my_database.cursor()
        #     a = mycursor.execute('SELECT * FROM Life Choices Online')
        #
        #     for i in mycursor:
        #         if i[0] == self.username_entry or i[1] == self.password_entry.get():
        #             messagebox.Message('Login Successfully', 'Enjoy Your Day')
        #             root.destroy()
        #
        #         if i[0] != self.username_entry.get():
        #             messagebox.showerror('Invalid Username', 'Please Enter A Correct Username!')
        #             self.username_entry.delete(0, END)
        #         elif i[1] != self.password_entry.get():
        #             messagebox.showerror('Invalid Password', 'Please Enter A Correct Password')
        #             self.password_entry.delete(0, END)
        #         else:
        #             i[1] != self.name_entry or i[0] != self.password_entry.get()
        #             messagebox.RETRYCANCEL('Invalid Entries', "Click 'RETRY' to Re-Enter '\n' CLick 'CANCEL' to Go And Register")
        #             self.username_entry.delete(0, END)
        #             self.password_entry.delete(0, END)
        #             return

    def register(self):
        root.destroy()
        import register


x = MainScreen()
root.mainloop()
