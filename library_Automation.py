from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime

class LibraryAutomation:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Automation")
        self.root.geometry("1920x1080+0+0")

        # Variable
        self.member_var=StringVar()
        self.universityid_var=StringVar()
        self.fname_var=StringVar()
        self.lname_var=StringVar()
        self.sem_var=StringVar()
        self.branch_var=StringVar()
        self.cllg_var=StringVar()
        self.mnumber_var=StringVar()
        self.session_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.aname_var=StringVar()
        self.dborrowed_var=StringVar()
        self.ddue_var=StringVar()
        self.dobook_var=StringVar()
        self.lrfine_var=StringVar()
        self.dodue_var=StringVar()
        self.aprice_var=StringVar()

        # Title label
        labeltitle = Label(self.root, text="Library Automation", bg="powder blue", fg="green", bd=20, relief=RIDGE, font=("Times New Roman", 50, "bold"), padx=2, pady=6)
        labeltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # Data frame left
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("Times New Roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=365)

        lblmember = Label(DataFrameLeft, bg="powder blue", text="Member Type :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,textvariable=self.member_var, font=("arial", 13, "bold"), width=28, state="readonly")
        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)

        lblUID = Label(DataFrameLeft, bg="powder blue", text="University ID :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblUID.grid(row=1, column=0, sticky=W)
        txtUID = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.universityid_var,width=28)
        txtUID.grid(row=1, column=1, padx=2, pady=6)

        lblf_name = Label(DataFrameLeft, bg="powder blue", text="First Name :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblf_name.grid(row=2, column=0, sticky=W)  
        txtf_name = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.fname_var, width=28)
        txtf_name.grid(row=2, column=1, padx=2, pady=6)  

        lbll_name = Label(DataFrameLeft, bg="powder blue", text="Last Name :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbll_name.grid(row=3, column=0, sticky=W)  
        txtl_name = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.lname_var,width=28)
        txtl_name.grid(row=3, column=1, padx=2, pady=6)

        lblsem = Label(DataFrameLeft, bg="powder blue", text="Semester :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblsem.grid(row=4, column=0, sticky=W)  
        txtsem = Entry(DataFrameLeft, font=("arial", 13, "bold"), textvariable=self.sem_var,width=28)
        txtsem.grid(row=4, column=1, padx=2, pady=6)

        lblb_name = Label(DataFrameLeft, bg="powder blue", text="Branch :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblb_name.grid(row=5, column=0, sticky=W)  
        txtb_name = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.branch_var, width=28)
        txtb_name.grid(row=5, column=1, padx=2, pady=6)

        lblcllg = Label(DataFrameLeft, bg="powder blue", text="College :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblcllg.grid(row=6, column=0, sticky=W)  
        lblcllg = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.cllg_var, width=28)
        lblcllg.grid(row=6, column=1, padx=2, pady=6)

        lblm_number = Label(DataFrameLeft, bg="powder blue", text="Mobile No. :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblm_number.grid(row=7, column=0, sticky=W)  
        lblm_number = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.mnumber_var, width=28)
        lblm_number.grid(row=7, column=1, padx=2, pady=6)

        lblsession = Label(DataFrameLeft, bg="powder blue", text="Session :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblsession.grid(row=8, column=0, sticky=W)  
        lblsession = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.session_var, width=28)
        lblsession.grid(row=8, column=1, padx=2, pady=6)

        lblb_id = Label(DataFrameLeft, bg="powder blue", text="Book ID :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblb_id.grid(row=0, column=2, sticky=W)
        txtb_id = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.bookid_var, width=28)
        txtb_id.grid(row=0, column=3, padx=2, pady=6)

        lblb_title = Label(DataFrameLeft, bg="powder blue", text="Book Title :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblb_title.grid(row=1, column=2, sticky=W)  
        txtb_title = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.booktitle_var,width=28)
        txtb_title.grid(row=1, column=3, padx=2, pady=6)  

        lbla_name = Label(DataFrameLeft, bg="powder blue", text="Author Name :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbla_name.grid(row=2, column=2, sticky=W)  
        txta_name = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.aname_var, width=28)
        txta_name.grid(row=2, column=3, padx=2, pady=6)

        lblborrow = Label(DataFrameLeft, bg="powder blue", text="Date Borrowed :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblborrow.grid(row=3, column=2, sticky=W)  
        txtborrow = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dborrowed_var, width=28)
        txtborrow.grid(row=3, column=3, padx=2, pady=6)

        lbldue = Label(DataFrameLeft, bg="powder blue", text="Date Due :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbldue.grid(row=4, column=2, sticky=W)  
        txtdue = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.ddue_var, width=28)
        txtdue.grid(row=4, column=3, padx=2, pady=6)

        lbldays = Label(DataFrameLeft, bg="powder blue", text="Days On Book :", font=("arial", 13, "bold"), padx=2, pady=6)
        lbldays.grid(row=5, column=2, sticky=W)  
        lbldays = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dobook_var, width=28)
        lbldays.grid(row=5, column=3, padx=2, pady=6)

        lblfine = Label(DataFrameLeft, bg="powder blue", text="Late Return Fine :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblfine.grid(row=6, column=2, sticky=W)  
        lblfine = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.lrfine_var, width=28)
        lblfine.grid(row=6, column=3, padx=2, pady=6)

        lblover = Label(DataFrameLeft, bg="powder blue", text="Date Over Due :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblover.grid(row=7, column=2, sticky=W)  
        lblover = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.dodue_var, width=28)
        lblover.grid(row=7, column=3, padx=2, pady=6)

        lblprice = Label(DataFrameLeft, bg="powder blue", text="Actual Price :", font=("arial", 13, "bold"), padx=2, pady=6)
        lblprice.grid(row=8, column=2, sticky=W)  
        lblprice = Entry(DataFrameLeft, font=("arial", 13, "bold"),textvariable=self.aprice_var, width=28)
        lblprice.grid(row=8, column=3, padx=2, pady=6)
        # Data frame right
        # Frame for Book Details
        DataFrameRight = LabelFrame(frame, bd=12, padx=20, relief=RIDGE, bg="powder blue", fg="green", 
                            font=("Times New Roman", 12, "bold"), text="Book Details")
        DataFrameRight.place(x=870, y=5, width=580, height=365)

# Scrollbar for ListBox
        ListScrollbar = Scrollbar(DataFrameRight, orient="vertical")
        ListScrollbar.grid(row=0, column=1, sticky="ns")

# ListBox
        ListBox = Listbox(DataFrameRight, font=("Times New Roman", 12, "bold"), width=30, height=16, 
                  yscrollcommand=ListScrollbar.set)
        ListBox.grid(row=0, column=0, padx=4, pady=6)
        ListScrollbar.config(command=ListBox.yview)

# Scrollbar for Text box
        TextScrollbar = Scrollbar(DataFrameRight, orient="vertical")
        TextScrollbar.grid(row=0, column=3, sticky="ns")

# Text box
        self.txtbox = Text(DataFrameRight, font=("Times New Roman", 12, "bold"), width=32, height=16, 
                   padx=2, pady=6, yscrollcommand=TextScrollbar.set)
        self.txtbox.grid(row=0, column=2, padx=4, pady=6)
        TextScrollbar.config(command=self.txtbox.yview)


        Listbook=["Python for Data Analysis",
"Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow",
"Deep Learning with Python",
"Data Science from Scratch: First Principles with Python",
"Python Machine Learning",
"Python Data Science Handbook",
"Introduction to Machine Learning with Python",
"Data Engineering with Python",
"Machine Learning Engineering",
"Designing Data-Intensive Applications",
"The Data Warehouse Toolkit",
"Feature Engineering for Machine Learning",
"Data Pipelines with Apache Airflow",
"Building Machine Learning Powered Applications",
"Data Science for Business",
"Practical Statistics for Data Scientists",
"Natural Language Processing with Python",
"Mining of Massive Datasets",
"Python Cookbook",
"The Hundred-Page Machine Learning Book",
"Storytelling with Data",
"Data Wrangling with Python",
"The Art of Data Science",
"Pattern Recognition and Machine Learning",
"Applied Predictive Modeling",
"Bayesian Data Analysis",
"Naked Statistics",
"Big Data: Principles and Best Practices of Scalable Real-Time Data Systems",
"Introduction to Statistical Learning (ISLR)",
"The Visual Display of Quantitative Information",
"Data Visualization: A Practical Introduction"
]
        for item in Listbook:
            ListBox.insert(END,item)

        def SelectBook(event):
            try:
                value = str(ListBox.get(ListBox.curselection()))
                if value == "Python for Data Analysis":
                    self.bookid_var.set("BKID 7856")
                    self.booktitle_var.set("Data manual")
                    self.aname_var.set("Wes McKinney")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.788")

                elif value == "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow":
                    self.bookid_var.set("BKID 7857")
                    self.booktitle_var.set("Machine Learning")
                    self.aname_var.set("Aurélien Géron")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.999")
                
                elif value == "Deep Learning with Python":
                    self.bookid_var.set("BKID 7858")
                    self.booktitle_var.set("Deep Learning")
                    self.aname_var.set("Franois Chollet")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.959")

                elif value == "Data Science from Scratch: First Principles with Python":
                    self.bookid_var.set("BKID 7859")
                    self.booktitle_var.set("Data Science for Beginner")
                    self.aname_var.set("Joel Grus")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.499")

                elif value == "Python Machine Learning":
                    self.bookid_var.set("BKID 7860")
                    self.booktitle_var.set("ML with python")
                    self.aname_var.set("Wei-Meng Lee")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.789")

                elif value == "Python Data Science Handbook":
                    self.bookid_var.set("BKID 7861")
                    self.booktitle_var.set("DS Handbook")
                    self.aname_var.set("Jake VanderPlas")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.899")

                elif value == "Introduction to Machine Learning with Python":
                    self.bookid_var.set("BKID 7862")
                    self.booktitle_var.set("Machine Learning")
                    self.aname_var.set("Andreas C. Muller")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.799")

                elif value == "Data Engineering with Python":
                    self.bookid_var.set("BKID 7863")
                    self.booktitle_var.set("Data Science")
                    self.aname_var.set("Paul Crickard")
                    
                    d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                    d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                    self.dborrowed_var.set(d1)
                    self.ddue_var.set(d2)
                    self.dobook_var.set(15)
                    self.lrfine_var.set("Rs.50")
                    self.dodue_var.set("No")
                    self.aprice_var.set("Rs.659")

                elif value == "Designing Data-Intensive Applications":
                  self.bookid_var.set("BKID 7864")
                  self.booktitle_var.set("Data Systems")
                  self.aname_var.set("Martin Kleppmann")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.879")

                elif value == "Machine Learning Engineering":
                  self.bookid_var.set("BKID 6586")
                  self.booktitle_var.set("Machine Learning")
                  self.aname_var.set("Martin Kleppmann")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.809")

                elif value == "The Data Warehouse Toolkit":
                  self.booktitle_var.set("Data Warehouse")
                  self.bookid_var.set("BKID 7865")
                  self.aname_var.set("Ralph Kimball")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.899")

                elif value == "Feature Engineering for Machine Learning":
                  self.bookid_var.set("BKID 7866")
                  self.booktitle_var.set("Feature Engineering")
                  self.aname_var.set("Alice Zheng")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.699")

                elif value == "Data Pipelines with Apache Airflow":
                  self.bookid_var.set("BKID 7867")
                  self.booktitle_var.set("Data Pipelines")
                  self.aname_var.set("Bas P. Harenslak")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.779")

                elif value == "Building Machine Learning Powered Applications":
                  self.bookid_var.set("BKID 7868")
                  self.booktitle_var.set("ML Applications")
                  self.aname_var.set("Emmanuel Ameisen")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.839")

                elif value == "Data Science for Business":
                  self.bookid_var.set("BKID 7869")
                  self.booktitle_var.set("DS for Business")
                  self.aname_var.set("Foster Provost")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.749")

                elif value == "Practical Statistics for Data Scientists":
                  self.bookid_var.set("BKID 7870")
                  self.booktitle_var.set("Practical Statistics")
                  self.aname_var.set("Peter Bruce")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.649")

                elif value == "Natural Language Processing with Python":
                  self.bookid_var.set("BKID 7871")
                  self.booktitle_var.set("NLP with Python")
                  self.aname_var.set("Steven Bird")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.849")

                elif value == "Mining of Massive Datasets":
                  self.bookid_var.set("BKID 7872")
                  self.booktitle_var.set("Massive Datasets")
                  self.aname_var.set("Jure Leskovec")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.799")

                elif value == "Python Cookbook":
                  self.bookid_var.set("BKID 7873")
                  self.booktitle_var.set("Python Recipes")
                  self.aname_var.set("David Beazley")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.899")

                elif value == "The Hundred-Page Machine Learning Book":
                  self.bookid_var.set("BKID 7874")
                  self.booktitle_var.set("ML Book")
                  self.aname_var.set("Andriy Burkov")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.599")

                elif value == "Storytelling with Data":
                  self.bookid_var.set("BKID 7875")
                  self.booktitle_var.set("Data Storytelling")
                  self.aname_var.set("Cole Nussbaumer Knaflic")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.899")

                elif value == "Data Wrangling with Python":
                  self.bookid_var.set("BKID 7876")
                  self.booktitle_var.set("Data Wrangling")
                  self.aname_var.set("Jacqueline Kazil")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.789")

                elif value == "The Art of Data Science":
                  self.bookid_var.set("BKID 7877")
                  self.booktitle_var.set("Data Science Art")
                  self.aname_var.set("Roger D. Peng")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.559")

                elif value == "Pattern Recognition and Machine Learning":
                  self.bookid_var.set("BKID 7878")
                  self.booktitle_var.set("Pattern Recognition")
                  self.aname_var.set("Christopher Bishop")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.949")

                elif value == "Applied Predictive Modeling":
                  self.bookid_var.set("BKID 7879")
                  self.booktitle_var.set("Predictive Modeling")
                  self.aname_var.set("Max Kuhn")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.869")

                elif value == "Bayesian Data Analysis":
                  self.bookid_var.set("BKID 7880")
                  self.booktitle_var.set("Bayesian Analysis")
                  self.aname_var.set("Andrew Gelman")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.969")

                elif value == "Naked Statistics":
                  self.bookid_var.set("BKID 7881")
                  self.booktitle_var.set("Statistics Simplified")
                  self.aname_var.set("Charles Wheelan")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.549")

                elif value == "Big Data: Principles and Best Practices of Scalable Real-Time Data Systems":
                  self.bookid_var.set("BKID 7882")
                  self.booktitle_var.set("Big Data Systems")
                  self.aname_var.set("Nathan Marz")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.789")

                elif value == "Introduction to Statistical Learning (ISLR)":
                  self.bookid_var.set("BKID 7883")
                  self.booktitle_var.set("Statistical Learning")
                  self.aname_var.set("Gareth James")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.659")

                elif value == "The Visual Display of Quantitative Information":
                  self.bookid_var.set("BKID 7884")
                  self.booktitle_var.set("Quantitative Display")
                  self.aname_var.set("Edward Tufte")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.899")

                elif value == "Data Visualization: A Practical Introduction":
                  self.bookid_var.set("BKID 7885")
                  self.booktitle_var.set("Data Visualization")
                  self.aname_var.set("Kieran Healy")
                  d1 = datetime.datetime.today().strftime("%d-%m-%Y")
                  d2 = (datetime.datetime.today() + datetime.timedelta(days=15)).strftime("%d-%m-%Y")
                  self.dborrowed_var.set(d1)
                  self.ddue_var.set(d2)
                  self.dobook_var.set(15)
                  self.lrfine_var.set("Rs.50")
                  self.dodue_var.set("No")
                  self.aprice_var.set("Rs.759")

            except:
                messagebox.showerror("Error", "Please select a book from the list.")


        ListBox.bind("<<ListboxSelect>>", SelectBook)

        # Buttons frame
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Framebutton.place(x=0, y=530, width=1530, height=70)

        btnadddata=Button(Framebutton,command=self.add_data,text="Add Data",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=0)

        btnadddata=Button(Framebutton,command=self.show_data,text="Show Data",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=1)

        btnadddata=Button(Framebutton,command=self.update,text="Update",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=2)

        btnadddata=Button(Framebutton,command=self.delete,text="Delete",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=3)

        btnadddata=Button(Framebutton,command=self.reset,text="Reset",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=4)

        btnadddata=Button(Framebutton,command=self.iExit,text="Exit",font=("Times New Roman", 12, "bold"),width=26,bg="blue",fg="white")
        btnadddata.grid(row=0,column=5)

        # Information frame
        Frameinfo = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        Frameinfo.place(x=0, y=600, width=1530, height=210)

        # Data Table
        Table_frame = Frame(Frameinfo, bd=6, relief="ridge", bg="powder blue")
        Table_frame.place(x=0, y=2, width=1460, height=180)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","universityid","fname","lname","sem","branch","cllg","mnumber","session","bookid","booktitle","aname","dborrowed","ddue","dobook","lrfine","dodue","aprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("universityid",text="University ID")
        self.library_table.heading("fname",text="First Name")
        self.library_table.heading("lname",text="Last Name")
        self.library_table.heading("sem",text="Semester")
        self.library_table.heading("branch",text="Branch")
        self.library_table.heading("cllg",text="College")
        self.library_table.heading("mnumber",text="Mobile Number")
        self.library_table.heading("session",text="Session")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("aname",text="Author Name")
        self.library_table.heading("dborrowed",text="Date Borrowed")
        self.library_table.heading("ddue",text="Date Due")
        self.library_table.heading("dobook",text="Days On Book")
        self.library_table.heading("lrfine",text="Late Return Fine")
        self.library_table.heading("dodue",text="Date Over Due")
        self.library_table.heading("aprice",text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("universityid",width=100)
        self.library_table.column("fname",width=100)
        self.library_table.column("lname",width=100)
        self.library_table.column("sem",width=100)
        self.library_table.column("branch",width=100)
        self.library_table.column("cllg",width=100)
        self.library_table.column("mnumber",width=100)
        self.library_table.column("session",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("aname",width=100)
        self.library_table.column("dborrowed",width=100)
        self.library_table.column("ddue",width=100)
        self.library_table.column("dobook",width=100)
        self.library_table.column("lrfine",width=100)
        self.library_table.column("dodue",width=100)
        self.library_table.column("aprice",width=100)

        self.fetch_data()

    def add_data(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vishal@123",
                database="vishal",
            )
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO library_automation VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    self.member_var.get(),
                    self.universityid_var.get(),
                    self.fname_var.get(),
                    self.lname_var.get(),
                    self.sem_var.get(),
                    self.branch_var.get(),
                    self.cllg_var.get(),
                    self.mnumber_var.get(),
                    self.session_var.get(),
                    self.bookid_var.get(),
                    self.booktitle_var.get(),
                    self.aname_var.get(),
                    self.dborrowed_var.get(),
                    self.ddue_var.get(),
                    self.dobook_var.get(),
                    self.lrfine_var.get(),
                    self.dodue_var.get(),
                    self.aprice_var.get(),
                ),
            )

            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Member has been inserted successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}")


    def update(self):
      try:
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="Vishal@123",
            database="vishal"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("""
            UPDATE library_automation 
            SET 
                `Member Type` = %s,
                `First Name` = %s,
                `Last Name` = %s,
                `Branch` = %s,
                `Semester` = %s,
                `College` = %s,
                `Mobile No.` = %s,
                `Session` = %s,
                `Book ID` = %s,
                `Book Title` = %s,
                `Author Name` = %s,
                `Date Borrowed` = %s,
                `Date Due` = %s,
                `Days On Book` = %s,
                `Late Return Fine` = %s,
                `Date Over Due` = %s,
                `Actual Price` = %s
            WHERE `University Id` = %s
        """, (
            self.member_var.get(),
            self.fname_var.get(),
            self.lname_var.get(),
            self.branch_var.get(),
            self.sem_var.get(),
            self.cllg_var.get(),
            self.mnumber_var.get(),
            self.session_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.aname_var.get(),
            self.dborrowed_var.get(),
            self.ddue_var.get(),
            self.dobook_var.get(),
            self.lrfine_var.get(),
            self.dodue_var.get(),
            self.aprice_var.get(),
            self.universityid_var.get(),
        ))
        
        conn.commit()
        self.fetch_data()
        self.reset()
        
        messagebox.showinfo("Success", "Member has been updated")
    
      except mysql.connector.Error as err:
        messagebox.showerror("Database Error", "Error: " + str(err))
      except Exception as e:
        messagebox.showerror("Error", "An unexpected error occurred: " + str(e))
      finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()



    def fetch_data(self):
      self.library_table.bind("<ButtonRelease-1>",self.get_cursor)
      # try:
      conn = mysql.connector.connect(
          host="localhost",
          username="root",
          password="Vishal@123",
          database="vishal",
        )
      my_cursor = conn.cursor()
      my_cursor.execute("select * from library_automation")
      rows=my_cursor.fetchall()
      if len(rows)!=0:
              self.library_table.delete(*self.library_table.get_children())
              for i in rows:
                self.library_table.insert("",END,values=i)
              conn.commit()
      conn.close()

    def get_cursor(self,event):
      cursor_row=self.library_table.focus()
      content=self.library_table.item(cursor_row)
      row=content["values"]

      self.member_var.set(row[0]),
      self.universityid_var.set(row[1]),
      self.fname_var.set(row[2]),
      self.lname_var.set(row[3]),
      self.branch_var.set(row[4]),
      self.sem_var.set(row[5]),
      self.cllg_var.set(row[6]),
      self.mnumber_var.set(row[7]),
      self.session_var.set(row[8]),
      self.bookid_var.set(row[9]),
      self.booktitle_var.set(row[10]),
      self.aname_var.set(row[11]),
      self.dborrowed_var.set(row[12]),
      self.ddue_var.set(row[13]),
      self.dobook_var.set(row[14]),
      self.lrfine_var.set(row[15]),
      self.dodue_var.set(row[16]),
      self.aprice_var.set(row[17])

    def show_data(self):
      self.txtbox.insert(END,"Member Type :\t\t"+self.member_var.get() +"\n")
      self.txtbox.insert(END,"University ID :\t\t"+self.universityid_var.get() +"\n")
      self.txtbox.insert(END,"First Name :\t\t"+self.fname_var.get() +"\n")
      self.txtbox.insert(END,"Last Name :\t\t"+self.lname_var.get() +"\n")
      self.txtbox.insert(END,"Semester :\t\t"+self.branch_var.get() +"\n")
      self.txtbox.insert(END,"Branch :\t\t"+self.sem_var.get() +"\n")
      self.txtbox.insert(END,"College :\t\t"+self.cllg_var.get() +"\n")
      self.txtbox.insert(END,"Mobile No. :\t\t"+self.mnumber_var.get() +"\n")
      self.txtbox.insert(END,"Session :\t\t"+self.session_var.get() +"\n")
      self.txtbox.insert(END,"Book ID :\t\t"+self.bookid_var.get() +"\n")
      self.txtbox.insert(END,"Book Title :\t\t"+self.booktitle_var.get() +"\n")
      self.txtbox.insert(END,"Author Name :\t\t"+self.aname_var.get() +"\n")
      self.txtbox.insert(END,"Date Borrowed :\t\t"+self.dborrowed_var.get() +"\n")
      self.txtbox.insert(END,"Date Due :\t\t"+self.ddue_var.get() +"\n")
      self.txtbox.insert(END,"Days On Book :\t\t"+self.dobook_var.get() +"\n")
      self.txtbox.insert(END,"Late Return Fine :\t\t"+self.lrfine_var.get() +"\n")
      self.txtbox.insert(END,"Date Over Due :\t\t"+self.dodue_var.get() +"\n")
      self.txtbox.insert(END,"Actual Price :\t\t"+self.aprice_var.get() +"\n")


    def reset(self):
      self.member_var.set(""),
      self.universityid_var.set(""),
      self.fname_var.set(""),
      self.lname_var.set(""),
      self.branch_var.set(""),
      self.sem_var.set(""),
      self.cllg_var.set(""),
      self.mnumber_var.set(""),
      self.session_var.set(""),
      self.bookid_var.set(""),
      self.booktitle_var.set(""),
      self.aname_var.set(""),
      self.dborrowed_var.set(""),
      self.ddue_var.set(""),
      self.dobook_var.set(""),
      self.lrfine_var.set(""),
      self.dodue_var.set(""),
      self.aprice_var.set("")
      self.txtbox.delete("1.0",END)
    
    def iExit(self):
      iExit=tkinter.messagebox.askyesno("Library Automation","Do you really want to exit ?")
      if iExit>0:
        self.root.destroy()
        return

    def delete(self):
      if self.universityid_var.get() == "" or self.bookid_var.get() == "":
        messagebox.showerror("Error", "First select the Member for delete")
      else:
        try:
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="Vishal@123",
                database="vishal",
            )
            my_cursor = conn.cursor()
            query = "DELETE FROM library_automation WHERE `University ID` = %s"
            value = (self.universityid_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            
            messagebox.showinfo("Success", "Member has been deleted")
        
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", "Error: " + str(err))
        except Exception as e:
            messagebox.showerror("Error", "An unexpected error occurred: " + str(e))
        
        finally:
            if 'conn' in locals() and conn.is_connected():
                conn.close()

      
if __name__ == "__main__":
    root = Tk()
    obj = LibraryAutomation(root)
    root.mainloop()
