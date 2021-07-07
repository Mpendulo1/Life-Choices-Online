from tkinter import *
import tkinter.messagebox
from tkinter import Scrollbar, Listbox
win = Tk()
win.geometry('1335x580')
win.title('Database Management')

class Administration:
    def __init__(self):

        users = StringVar()
        FirstName = StringVar()
        Surname = StringVar()
        Password = StringVar()
        Identity = StringVar()
        PhoneNumber = StringVar()
        NextOfKin_name = StringVar()
        NextOfKin_number = StringVar()

        # ================================ Frame =========================
        mainframe = Frame(win, bg='cadet blue')
        mainframe.grid()
        titframe = Frame(mainframe, bd=2, padx=52, pady=8, bg='SkyBlue', relief=RIDGE)
        titframe.pack(side=TOP)

        self.lbltit = Label(titframe, font=('Arial', 30, 'bold'), text='Database Management', bg='SkyBlue')
        self.lbltit.grid()

        buttonfrme = Frame(mainframe, bd=2, width=1350, height=70, padx=18, pady=10, bg='SkyBlue', relief=RIDGE)
        buttonfrme.pack(side=BOTTOM)

        dataframe = Frame(mainframe, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg='white')
        dataframe.pack(side=BOTTOM)

        dataframe_left = LabelFrame(dataframe, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg='skyblue', font=('Arial', 20, 'bold'), text='User Info\n')
        dataframe_left.pack(side=LEFT)

        dataframe_right = LabelFrame(dataframe, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg='skyblue', font=('arial', 20, 'bold'), text='User Details\n')
        dataframe_right.pack(side=RIGHT)

        # ================================ Labels =========================
        self.lblID = Label(dataframe_left, font=('Arial', 20, 'bold'), text='User ID', bg='skyblue', padx=2, pady=2)
        self.lblID.grid(row=0, column=0, sticky=W)
        self.txtID = Entry(dataframe_left, font=('Courier', 20), textvariable=users, justify=CENTER, width=39)
        self.txtID.grid(row=0, column=1)

        self.lbl_firstname = Label(dataframe_left, font=('Arial', 20, 'bold'), text='First Name', bg='skyblue', padx=2, pady=2)
        self.lbl_firstname.grid(row=1, column=0, sticky=W)
        self.txt_firstname_entry = Entry(dataframe_left, font=('Courier', 20), textvariable=FirstName, justify=CENTER, width=39)
        self.txt_firstname_entry.grid(row=1, column=1)

        self.lbl_surname = Label(dataframe_left, font=('Arial', 20, 'bold'), text='Surname', bg='skyblue', padx=2, pady=2)
        self.lbl_surname.grid(row=2, column=0, sticky=W)
        self.txt_surname_entry = Entry(dataframe_left, font=('Courier', 20), textvariable=Surname, justify=CENTER, width=39)
        self.txt_surname_entry.grid(row=2, column=1)

        self.lbl_Identity = Label(dataframe_left, font=('Arial', 20, 'bold'), text='Identity', bg='skyblue', padx=2, pady=2)
        self.lbl_Identity.grid(row=3, column=0, sticky=W)
        self.txtID_entry = Entry(dataframe_left, font=('Courier', 20), textvariable=Identity, justify=CENTER, width=39)
        self.txtID_entry.grid(row=3, column=1)

        self.lbl_phone_number = Label(dataframe_left, font=('Arial', 20, 'bold'), text='Kin Name', bg='skyblue', padx=2, pady=2)
        self.lbl_phone_number.grid(row=4, column=0, sticky=W)
        self.txt_number_entry = Entry(dataframe_left, font=('Courier', 20), textvariable=NextOfKin_name, justify=CENTER, width=39)
        self.txt_number_entry.grid(row=4, column=1)

        self.lbl_kin_Name = Label(dataframe_left, font=('Arial', 20, 'bold'), text='Kin Number', bg='skyblue', padx=2, pady=2)
        self.lbl_kin_Name.grid(row=5, column=0, sticky=W)
        self.txt_kin_number = Entry(dataframe_left, font=('Courier', 20), textvariable=NextOfKin_number, justify=CENTER, width=39)
        self.txt_kin_number.grid(row=5, column=1)

        #================================================ List and Scrollbar Widget =======================
        scrollbar = Scrollbar(dataframe_right)
        scrollbar.grid(row=0, column=1, sticky='ns')
        user_list = Listbox(dataframe_right, width=41, height=16, font=('Arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        user_list.grid(row=0, column=0, padx=8)
        scrollbar.config(command=user_list.yview)

        # ================================ Buttons =========================
        self.Add_button = Button(buttonfrme, text='Add User', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Add_button.grid(row=0, column=0)

        self.Display_button = Button(buttonfrme, text='Update', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Display_button.grid(row=0, column=1)

        self.clear_button = Button(buttonfrme, text='Search', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.clear_button.grid(row=0, column=2)

        self.Delete_button = Button(buttonfrme, text='Display', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Delete_button.grid(row=0, column=3)

        self.Search_button = Button(buttonfrme, text='Delete', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Search_button.grid(row=0, column=4)

        self.Update_button = Button(buttonfrme, text='Clear', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Update_button.grid(row=0, column=5)

        self.Exit_button = Button(buttonfrme, text='Exit', relief=GROOVE, activebackground="#33B5E5", bg='gray80', fg='gray12', font=('Georgia', 15, 'bold'), cursor='hand2', height=1, width=10, bd=3)
        self.Exit_button.grid(row=0, column=6)



x = Administration()
win.mainloop()
