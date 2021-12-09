from tkinter import *
from tkinter import ttk
import pymysql
import datetime
import webbrowser




class generateBill:
    def __init__(self):
        #---variables------
        self.cdate=datetime.datetime.now()
        self.cID=StringVar()
        self.selectedC=""


        self.Fnewbill=Tk()
        self.Fnewbill.title("Add New Bill")
        self.Fnewbill.geometry("1150x650+100+60")
        self.Fnewbill.configure(background=colbg)
        

        #--------------Frame1--------------
        self.frame1=Frame(self.Fnewbill, bg=colbg)
        self.frame1.place(x=0, y=0)

        Label(self.frame1, text="બિલ નંબર :", anchor=E, width=15, bg=colbg).pack(side=LEFT, pady=15)
        self.billno=Label(self.frame1, text=self.cdate.strftime("%y%m%d%H%M"), font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=20).pack(side=LEFT)
        Label(self.frame1, text="બિલની તારીખ :", bg=colbg, anchor=E, width=20).pack(side=LEFT)
        self.billdate=Label(self.frame1, text=self.cdate.strftime("%d %b %Y"), font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=20).pack(side=LEFT)
        #Button(self.frame1, text="Refresh Bill", font="arial 10 bold", width=15, bd=2, bg=colbtn, fg="white").pack(side=LEFT)

        #--------------Frame2--------------
        self.frame2=Frame(self.Fnewbill, bg=colbg)
        self.frame2.place(x=0, y=70)

        Label(self.frame2, text="Search Customer :", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.ECust=Entry(self.frame2, font="arial 10", fg="red", width=30, bd=2)
        self.ECust.grid(row=0, column=1, columnspan=2, sticky=W)
        self.ECust.bind('<KeyRelease>', self.callback)


        #--------------SearchFrame1--------------
        self.sFrame1=Frame(self.Fnewbill)
        self.clistbox=Listbox(self.sFrame1, width=70)
        self.clistbox.pack()
        self.clistbox.bind("<Double-1>", self.on2clickL1)
        self.clistbox.bind("<<ListboxSelect>>", self.onSelectL1)

        self.cAddBtn=Button(self.sFrame1, text="Add", command=self.addCustInfo)
        self.cAddBtn.pack(fill=X)


        #--------------Frame3--------------
        self.frame3=Frame(self.Fnewbill, bg=colbg)
        self.frame3.place(x=300, y=70)
        Label(self.frame3, text="નામ :", anchor=E, width=15, bg=colbg).grid(row=0, column=0)
        self.cLabelname=Label(self.frame3, anchor=W, width=30, font="arial 10 bold", bg=colbg, fg="red")
        self.cLabelname.grid(row=0, column=1)
        Label(self.frame3, text="મોબાઈલ નંબર :", anchor=E, width=15, bg=colbg).grid(row=0, column=2)
        self.cLabelMobile=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red")
        self.cLabelMobile.grid(row=0, column=3)
        Label(self.frame3, text="ગામ :", anchor=E, width=5, bg=colbg).grid(row=0, column=4)
        self.cLabelVillage=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red")
        self.cLabelVillage.grid(row=0, column=5)
        
        
        self.Fnewbill.mainloop()

    def on2clickL1(self, evt):
        varx=self.clistbox.curselection()
        if varx:
            self.selectedC=self.clistbox.get(varx)[:10]
        self.addCustInfo()

    def onSelectL1(self, evt):
        varx=self.clistbox.curselection()
        if varx:
            self.selectedC=self.clistbox.get(varx)[:10]

    def addCustInfo(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        if self.selectedC!="":
            curr.execute("select * from customerdata where MobileNo="+self.selectedC)
            clist=curr.fetchall()
            if len(clist)!=0:
                self.cLabelname.config(text=clist[0][1]+" "+clist[0][2]+" "+clist[0][3])
                self.cLabelMobile.config(text=clist[0][0])
                self.cLabelVillage.config(text=clist[0][4])
        conn.commit()
        conn.close()
        self.ECust.delete(0, END)
        self.sFrame1.place_forget()

    def callback(self, e):
        if self.ECust.get() != "":
            self.sFrame1.lift()
            self.sFrame1.place(x=122, y=93)
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            varx=self.ECust.get()
            curr.execute("select * from customerdata where MobileNo LIKE '%"+ varx +"%' OR FName LIKE '%"+ varx +"%' OR MName LIKE '%"+ varx +"%' OR LName LIKE '%"+ varx +"%' OR City LIKE '%"+ varx +"%'")
            clist=curr.fetchall()
            self.clistbox.delete(0, END)
            if len(clist)!=0:
                for row in clist:
                    s=str(row[0])+"    "+row[1]+" "+row[2]+" "+row[3]+"    "+row[4]+"    "+str(row[5])+" Rs."
                    self.clistbox.insert("end", s)
        else:
            self.sFrame1.place_forget()        










class allBills:
    def __init__(self, F):
        self.Fbills=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.Etextvar=StringVar()



        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fbills, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Bill :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        #self.Etextvar.trace("w", self.callBack)
        self.Etext=Entry(self.frame1, font="arial 11", textvariable=self.Etextvar, fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        #self.Etext.bind('<KeyRelease>', self.searchCallbill)


        # Frame 2 Table---------------------------------------------------------------------------------------
        self.frame2=Frame(self.Fbills, bg=colbg)
        self.frame2.place(x=10, y=50, relwidth=1, height=470)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show="headings", height=22)
        self.tree.place(x=0, y=0, width=1150)

        self.tree.column("#1", anchor=CENTER, width=80)
        self.tree.column("#2", anchor=CENTER, width=80)
        self.tree.column("#3", anchor=CENTER, width=80)
        self.tree.column("#4", anchor=CENTER, width=250)
        self.tree.column("#5", anchor=CENTER, width=80)
        self.tree.column("#6", anchor=CENTER, width=80)
        self.tree.column("#7", anchor=CENTER, width=80)
        self.tree.heading("#1", text="બિલ તારીખ")
        self.tree.heading("#2", text="બિલ નંબર")
        self.tree.heading("#3", text="મોબાઈલ નંબર")
        self.tree.heading("#4", text="ગ્રાહકનું નામ")
        self.tree.heading("#5", text="ગામ")
        self.tree.heading("#6", text="Cash / Debit")
        self.tree.heading("#7", text="Bill Amount")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=1149, y=0, height=470)
        self.v.config(command=self.tree.yview)

        '''self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=465, width=763)
        self.h.config(command=self.tree.xview)'''
        self.tree.configure(yscrollcommand=self.v.set) #xscrollcommand=self.h.set

        #self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #self.show_all_bills()
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fbills, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        self.Bnew=Button(self.frame3, text="New", command=self.newBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bnew.grid(row=0, column=0)
        self.Bedit=Button(self.frame3, text="Edit", command=self.editBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bedit.grid(row=0, column=1)
        self.Bdelete=Button(self.frame3, text="Delete", command=self.deleteBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bdelete.grid(row=0, column=2)
        self.Binfo=Button(self.frame3, text="Info", command=self.billInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Binfo.grid(row=0, column=4)



    def newBill(self):
        obj=generateBill()

    def editBill(self):
        pass
    def deleteBill(self):
        pass
    def billInfo(self):
        pass











class customerClass:
    def __init__(self, F):
        self.Fcust=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.Etextvar=StringVar()



        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fcust, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Customer :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        #self.Etextvar.trace("w", self.callback)
        self.Etext=Entry(self.frame1, font="arial 11", textvariable=self.Etextvar, fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        #self.Etext.bind('<KeyRelease>', self.searchCallCust)


        # Frame 2 Table---------------------------------------------------------------------------------------
        self.frame2=Frame(self.Fcust, bg=colbg)
        self.frame2.place(x=10, y=50, relwidth=1, height=470)
        
        #Treeview----------------start        
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "5"), show="headings", height=22)
        self.tree.place(x=0, y=0, width=1150)
        
        self.tree.column("#1", anchor=CENTER, width=80)
        self.tree.column("#2", anchor=CENTER, width=250)
        self.tree.column("#3", anchor=CENTER, width=80)
        self.tree.column("#4", anchor=CENTER, width=80)
        self.tree.column("#5", anchor=CENTER)
        self.tree.heading("#1", text="મોબાઈલ નંબર")
        self.tree.heading("#2", text="નામ")
        self.tree.heading("#3", text="ગામ")
        self.tree.heading("#4", text="Balance")
        self.tree.heading("#5", text="")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=1149, y=0, height=470)
        self.v.config(command=self.tree.yview)

        '''self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=465, width=763)
        self.h.config(command=self.tree.xview)'''
        self.tree.configure(yscrollcommand=self.v.set) #xscrollcommand=self.h.set

        #self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #self.show_all_customer()
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fcust, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        self.Bnew=Button(self.frame3, text="New", command=self.newCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bnew.grid(row=0, column=0)
        self.Bedit=Button(self.frame3, text="Edit", command=self.editCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bedit.grid(row=0, column=1)
        self.Bdelete=Button(self.frame3, text="Delete", command=self.deleteCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bdelete.grid(row=0, column=2)
        self.Binfo=Button(self.frame3, text="Info", command=self.custInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Binfo.grid(row=0, column=4)



    def newCust(self):
        pass
    def editCust(self):
        pass
    def deleteCust(self):
        pass
    def custInfo(self):
        pass


    '''def callback(self, var, indx, mode):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        tempv=self.Etext.get()
        curr.execute("select * from customerlist where\
            CMobileNo LIKE '%"+ tempv
            +"%' OR CFirstName LIKE '%"+ tempv
            +"%' OR CMiddleName LIKE '%"+ tempv
            +"%' OR CLastName LIKE '%"+ tempv
            +"%' OR CVillage LIKE '%"+ tempv
            +"%'")
        temparr=curr.fetchall()
        self.clistbox.delete(0, END)
        if len(clist)!=0:
            for row in clist:
                s=str(row[0])+"    "+row[1]+" "+row[2]+" "+row[3]+"    "+row[4]
                self.clistbox.insert("end", s)

    def callback(self, e):
        if self.ECust.get() != "":
            self.sFrame1.lift()
            self.sFrame1.place(x=122, y=93)
        else:
            self.sFrame1.place_forget()'''

















class productClass:
    def __init__(self, F):
        self.Fprod=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.Etextvar=StringVar()



        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fprod, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Product :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        #self.Etextvar.trace("w", self.callBack)
        self.Etext=Entry(self.frame1, font="arial 11", textvariable=self.Etextvar, fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        #self.Etext.bind('<KeyRelease>', self.searchCallProd)


        # Frame 2 Table---------------------------------------------------------------------------------------
        self.frame2=Frame(self.Fprod, bg=colbg)
        self.frame2.place(x=10, y=50, relwidth=1, height=470)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9"), show="headings", height=22)
        self.tree.place(x=0, y=0, width=1150)

        self.tree.column("#1", anchor=CENTER, width=30)
        self.tree.column("#2", anchor=CENTER, width=80)
        self.tree.column("#3", anchor=CENTER, width=200)
        self.tree.column("#4", anchor=CENTER, width=200)
        self.tree.column("#5", anchor=CENTER, width=80)
        self.tree.column("#6", anchor=CENTER, width=80)
        self.tree.column("#7", anchor=CENTER, width=80)
        self.tree.column("#8", anchor=CENTER, width=80)
        self.tree.column("#9", anchor=CENTER, width=80)
        self.tree.heading("#1", text="PID")
        self.tree.heading("#2", text="Product name")
        self.tree.heading("#3", text="Technical name")
        self.tree.heading("#4", text="Company name")
        self.tree.heading("#5", text="Batch no.")
        self.tree.heading("#6", text="Net Content")
        self.tree.heading("#7", text="Printed price")
        self.tree.heading("#8", text="Selling price")
        self.tree.heading("#9", text="Buying price")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=1149, y=0, height=470)
        self.v.config(command=self.tree.yview)

        '''self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=465, width=763)
        self.h.config(command=self.tree.xview)'''
        self.tree.configure(yscrollcommand=self.v.set) #xscrollcommand=self.h.set

        #self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #self.show_all_product()
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fprod, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        self.Bnew=Button(self.frame3, text="New", command=self.newProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bnew.grid(row=0, column=0)
        self.Bedit=Button(self.frame3, text="Edit", command=self.editProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bedit.grid(row=0, column=1)
        self.Bdelete=Button(self.frame3, text="Delete", command=self.deleteProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Bdelete.grid(row=0, column=2)
        self.Binfo=Button(self.frame3, text="Info", command=self.prodInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5)
        self.Binfo.grid(row=0, column=4)



    def newProd(self):
        pass
    def editProd(self):
        pass
    def deleteProd(self):
        pass
    def prodInfo(self):
        pass




















def callfooter(url):
    webbrowser.open_new(url)













# Create Tables ------------------------------------------------------------------------------------------------
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




# Color Variables ----------------------------------------------------------------------------------------------
colbg="#B8D4BD"
colbtn="#3C4ACA"
colhead="#0F9D58"
col1="#DE3163"



################################################################################################################
root=Tk()
root.title("શ્રી હરી એગ્રો સેન્ટર - Billing Software")
w=root.winfo_screenwidth() 
h=root.winfo_screenheight()
root.geometry("%dx%d" % (w, h))
#root.geometry("1360x730+0+0")
#root.attributes('-fullscreen',True)
root.configure(background=colbg)




# Treeview colors & Some Extra Variables------------------------------------------------------------------------
style=ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background=colbg, fieldbackground=colbg, foreground="black")

imgGod=PhotoImage(file="img/ganesha.png")
imgheart=PhotoImage(file="img/heart.png")



# Heading Frame -------------------------------------------------------------------------------------------------
Fheading=Frame(root, bg=colbg)
Fheading.place(x=0, y=0, relwidth=1)
Label(Fheading, text="|| શ્રી શ્રીનાથજી કૃપા ||", bg=colbg, fg=col1).grid(row=0, column=0, padx=10, pady=3)
Label(Fheading, text="|| શ્રી ગણેશાય નમઃ ||", bg=colbg, fg=col1, width=160).grid(row=0, column=1)
Label(Fheading, text="|| શ્રી બહુચર કૃપા ||", bg=colbg, fg=col1).grid(row=0, column=2)
Label(Fheading, text="શ્રી હરી એગ્રો સેન્ટર", font=("", 30, "bold"), bg=colbg, fg=colhead, pady=12).grid(row=1, column=1)
Label(Fheading, image=imgGod, bd=0).place(x=1280, y=25)


# Label Frames & Buttons ----------------------------------------------------------------------------------------
f1=LabelFrame(root, text="બિલની માહિતી", font=("", 10, "bold"), bg=colbg, fg=col1)
f2=LabelFrame(root, text="ગ્રાહકની માહિતી", font=("", 10, "bold"), bg=colbg, fg=col1)
f3=LabelFrame(root, text="દવાની માહિતી", font=("", 10, "bold"), bg=colbg, fg=col1)

for frame in (f1, f2, f3):
    frame.place(x=140, y=90, relwidth=1, height=600)

objf1=allBills(f1)
objf2=customerClass(f2)
objf3=productClass(f3)

Fbtn=Frame(root, bg=colbg)
Fbtn.place(x=20, y=90)
Button(Fbtn, text="બિલની માહિતી", font=("", 11, "bold"), bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f1.tkraise()).pack(fill=X)
Button(Fbtn, text="ગ્રાહકની માહિતી", font=("", 11, "bold"), bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f2.tkraise()).pack(fill=X)
Button(Fbtn, text="દવાની માહિતી", font=("", 11, "bold"), bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f3.tkraise()).pack(fill=X)







# Footer Frame ------------------------------------------------------------------------------------------------
FFoot=Frame(root, bg=colbg)
FFoot.place(x=140, y=700, relwidth=1)
Label(Fheading, text="|| શ્રી બહુચર કૃપા ||", bg=colbg)
link1=Label(FFoot, text="Build with       by Divyesh Ranpariya", font=("Mistral", 14, "bold"), bg=colbg, fg=colbtn, bd=0, padx=10)
link1.pack(side=LEFT)
link1.bind("<Button-1>", lambda e: callfooter("https://www.facebook.com/divyesh599/"))
Label(FFoot, image=imgheart, bd=0).place(x=97, y=2)



f1.tkraise()
root.mainloop()