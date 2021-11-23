from tkinter import *
from tkinter import ttk
import pymysql
import datetime
import webbrowser







conn=pymysql.connect(host="localhost",
                    user="root",
                    password="")
curr=conn.cursor()
curr.execute("CREATE DATABASE IF NOT EXISTS Database23Nov")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.customerdata\
    (MobileNo BIGINT,\
    FName VARCHAR(20),\
    MName VARCHAR(40),\
    LName VARCHAR(20),\
    City VARCHAR(20),\
    Balance INT,\
    PRIMARY KEY (MobileNo))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.productdata\
    (PID INT,\
    PName VARCHAR(20),\
    TechName VARCHAR(40),\
    Company VARCHAR(40),\
    BatchNo VARCHAR(20),\
    NetContent INT,\
    PrintPrice INT,\
    SellPrice INT,\
    BuyPrice INT,\
    PRIMARY KEY (PID))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.allbills\
    (BillDate VARCHAR(20),\
    BillNo BIGINT,\
    MobileNo BIGINT,\
    Name VARCHAR(100),\
    City VARCHAR(20),\
    CashDebit VARCHAR(10),\
    BillAmount INT,\
    PRIMARY KEY (BillNo))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.subbilldetails\
    (BillDate VARCHAR(20),\
    MobileNo BIGINT,\
    BillNo BIGINT,\
    PID INT,\
    Description VARCHAR(100),\
    Company VARCHAR(40),\
    BatchNo VARCHAR(20),\
    SellPrice INT,\
    Qty INT,\
    Amount INT,\
    PRIMARY KEY (BillNo, PID))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.tempsubbill\
    (BillDate VARCHAR(20),\
    MobileNo BIGINT,\
    BillNo BIGINT,\
    PID INT,\
    Description VARCHAR(100),\
    Company VARCHAR(40),\
    BatchNo VARCHAR(20),\
    SellPrice INT,\
    Qty INT,\
    Amount INT,\
    PRIMARY KEY (BillNo, PID))")
conn.commit()
conn.close()




# Color Variables --------------------------
colbg="#B8D4BD"
colbtn="#3C4ACA"
colhead="#0F9D58"
col1="#DE3163"




root=Tk()
root.title("શ્રી હરી એગ્રો સેન્ટર - Billing Software")
root.geometry("1360x730+0+0")
root.configure(background=colbg)




# Treeview colors & Some Extra Variables-------------------------
style=ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background=colbg, 
            fieldbackground=colbg, foreground="black")

imgGod=PhotoImage(file="img/ganesha.png")
imgheart=PhotoImage(file="img/heart.png")



# Method -------------------------------------------------------
def callfooter(url):
    webbrowser.open_new(url)








Fheading=Frame(root, bg=colbg)
Fheading.place(x=0, y=0, relwidth=1)
Label(Fheading, text="|| શ્રી શ્રીનાથજી કૃપા ||", bg=colbg, fg=col1).grid(row=0, column=0, padx=10)
Label(Fheading, text="|| શ્રી ગણેશાય નમઃ ||", bg=colbg, fg=col1, width=160).grid(row=0, column=1)
Label(Fheading, text="|| શ્રી બહુચર કૃપા ||", bg=colbg, fg=col1).grid(row=0, column=2)
Label(Fheading, text="શ્રી હરી એગ્રો સેન્ટર", font=("", 30, "bold"), bg=colbg, fg=colhead, pady=15).grid(row=1, column=1)
Label(Fheading, image=imgGod, bd=0).place(x=1280, y=25)

FFoot=Frame(root, bg=colbg)
FFoot.place(x=0, y=705, relwidth=1)
Label(Fheading, text="|| શ્રી બહુચર કૃપા ||", bg=colbg)
link1=Label(FFoot, text="Build with       Divyesh Ranpariya", font=("arial 10 bold"), bg=colbg, fg=colbtn, bd=0, padx=10)
link1.pack(side=LEFT)
link1.bind("<Button-1>", lambda e: callfooter("https://www.facebook.com/divyesh599/"))
Label(FFoot, image=imgheart, bd=0).place(x=78, y=0)




Fbtn=Frame(root, bg=colbg)
Fbtn.place(x=0, y=100, relheight=1)























#root.attributes('-fullscreen', True)
root.mainloop()