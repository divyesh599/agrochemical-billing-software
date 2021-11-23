from tkinter import *
from tkinter import ttk
import pymysql
import datetime







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





Fheading=Frame(root, bg=colbg)
Fheading.place(x=0, y=0, relwidth=1)
Label(Fheading, text="|| શ્રી શ્રીનાથજી ||", bg=colbg).place(x=0, y=0)
Label(Fheading, text="|| શ્રી ગણેશાય નમઃ ||", bg=colbg).place(x=600, y=0)
Label(Fheading, text="|| શ્રી બહુચર કૃપા ||", bg=colbg).place(x=1240, y=0)
Label(Fheading, text="શ્રી હરી એગ્રો સેન્ટર", font=("", 30, "bold"), bg=colbg, fg=colhead, pady=15).place(x=0, y=40)
Label(Fheading, image=imgGod, bd=0).place(x=1280, y=20)






Fbtn=Frame(root, bg=colbg)
Fbtn.place(x=0, y=100, relheight=1)























#root.attributes('-fullscreen', True)
root.mainloop()