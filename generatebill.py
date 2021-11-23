from tkinter import *
from tkinter import ttk
import pymysql
import datetime




class generateBill:
    def __init__(self, frame):
        self.f1=frame

        #---variables------
        self.cdate=datetime.datetime.now()
        self.c_id=StringVar()
        self.p_id=StringVar()
        self.quantity=StringVar()

#--------------Frame1--------------        
        self.frame1=Frame(self.f1, bg=bgcol)
        self.frame1.place(x=250, y=0)

        #--------List1---------
        self.List1=[]
        self.List1.append(Label(self.frame1, text="બિલ નંબર :", anchor=E, width=15, bg=bgcol))
        self.List1[0].pack(side=LEFT, pady=15)
        self.List1.append(Label(self.frame1, text=self.cdate.strftime("%y%m%d%H%M"), font="arial 10 bold", bg=bgcol, fg="red", anchor=W, width=20))
        self.List1[1].pack(side=LEFT)
        self.List1.append(Label(self.frame1, text="બિલની તારીખ :", bg=bgcol, anchor=E, width=20))
        self.List1[2].pack(side=LEFT)
        self.List1.append(Label(self.frame1, text=self.cdate.strftime("%d %b %Y"), font="arial 10 bold", bg=bgcol, fg="red", anchor=W, width=20))
        self.List1[3].pack(side=LEFT)
        self.List1.append(Button(self.frame1, text="Refresh Bill", command=self.create_new_bill, font="arial 10 bold", width=15, bd=2, bg=btncol, fg="white"))
        self.List1[4].pack(side=LEFT)

#--------------Frame2--------------
        self.frame2=Frame(self.f1, bg=bgcol)
        self.frame2.place(x=0, y=50)
        self.List2=[]

        #List2 row (0) column (0-8)
        self.csearch=PhotoImage(file="img/csearch.png")
        self.psearch=PhotoImage(file="img/psearch1.png")
        self.List2.append([Label(self.frame2, text="મોબાઈલ નંબર :", bg=bgcol),
                            Entry(self.frame2, font="arial 10", textvariable=self.c_id, fg="red", width=10, bd=2),
                            Button(self.frame2, image=self.csearch, command=self.customer_search, bd=2, bg=btncol),
                            #Button(self.frame2, text="Search", command=self.customer_search, bd=2, bg=btncol, fg="white"),
                            Label(self.frame2, text="નામ :", anchor=E, width=5, bg=bgcol),
                            Label(self.frame2, anchor=W, width=30, font="arial 10 bold", bg=bgcol, fg="red"),
                            Label(self.frame2, text="મોબાઈલ નંબર :", anchor=E, width=15, bg=bgcol),
                            Label(self.frame2, anchor=W, width=15, font="arial 10 bold", bg=bgcol, fg="red"),
                            Label(self.frame2, text="ગામ :", anchor=E, width=5, bg=bgcol),
                            Label(self.frame2, anchor=W, width=15, font="arial 10 bold", bg=bgcol, fg="red")
                        ])
        self.List2[0][0].grid(row=0, column=0, sticky=W, pady=32, padx=10)
        self.List2[0][1].grid(row=0, column=1, columnspan=2, sticky=W)
        self.List2[0][2].grid(row=0, column=2, sticky=W)
        for i in range(3, 9):
            self.List2[0][i].grid(row=0, column=i)

        #List2 row (1) column (0-2)
        self.List2.append([Label(self.frame2, text="પ્રોડક્ટ નંબર :", bg=bgcol),
                            Entry(self.frame2, font="arial 9", textvariable=self.p_id, fg="red", width=10, bd=2),
                            Button(self.frame2, image=self.psearch, command=self.product_search, bd=2, bg=btncol)
                            ])
        self.List2[1][0].grid(row=1, column=0, sticky=W, pady=5, padx=10)
        self.List2[1][1].grid(row=1, column=1, columnspan=2, sticky=W, pady=5)
        self.List2[1][2].grid(row=1, column=2, sticky=W, pady=5)
        
        #List2 row (2-8) column (0-2)
        self.List2.append([Label(self.frame2, text="પ્રોડક્ટ નંબર :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol, fg="red")])
        self.List2.append([Label(self.frame2, text="જંતુ. દવાનું નામ :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol)])
        self.List2.append([Label(self.frame2, text="ઉત્પાદકનું નામ :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol)])
        self.List2.append([Label(self.frame2, text="બેંચ નંબર :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol)])
        self.List2.append([Label(self.frame2, text="પેકિંગ (મિલી/ગ્રામ) :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol)])
        self.List2.append([Label(self.frame2, text="વેચાણ કિંમત :", bg=bgcol), Label(self.frame2, font="arial 9 bold", bg=bgcol)])
        self.List2.append([Label(self.frame2, text="વેચેલ જથ્થો :", bg=bgcol), Entry(self.frame2, textvariable=self.quantity, font="arial 9 bold", fg="red", width=10, bd=2)])
        self.List2[8][1].insert(0,"1")
        self.List2.append([Button(self.frame2, text="Add", command=self.add_item_into_bill, width=10, bd=2, bg=btncol, fg="white")])
        self.List2.append([Button(self.frame2, text="Update", command=self.update_item_into_bill, width=10, bd=2, bg=btncol, fg="white")])
        self.List2.append([Button(self.frame2, text="Delete", command=self.delete_item_into_bill, width=10, bd=2, bg=btncol, fg="white")])

        for i in range(2, 9):
            self.List2[i][0].grid(row=i, column=0, sticky=W, pady=5, padx=(10, 0))
            self.List2[i][1].grid(row=i, column=1, columnspan=2, sticky=W)
        
        #List2 row (8-9) column (1-3)
        self.List2[9][0].grid(row=8, column=2, sticky=W)
        self.List2[10][0].grid(row=8, column=3, sticky=W)
        self.List2[11][0].grid(row=9, column=1, sticky=W, pady=5)

#-------#Treeview-------------------------------------------------------------start
        self.tree=ttk.Treeview(self.f1, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"),
                    show="headings", height=9)
        self.tree.place(x=280, y=140, width=900)
        
        self.col_name=["પ્રોડક્ટ નંબર",
                        "જંતુ. દવાનું નામ/ રા. ખાતરનું નામ",
                        "ઉત્પાદકનું નામ",
                        "બેંચ નંબર",
                        "પેકિંગ (મિલી/ગ્રામ)",
                        "વેચાણ કિંમત",
                        "વેચેલ જથ્થો",
                        "કુલ રકમ (₹.)"]
        
        self.col_size=[70, 220, 150, 70, 100, 75, 75, 80]

        for i in range(8):
            self.tree.column('#'+str(i+1), anchor=CENTER, width=self.col_size[i])
            self.tree.heading('#'+str(i+1), text=self.col_name[i])

        self.v=Scrollbar(self.f1, orient="vertical")
        self.v.place(x=1180, y=140, height=210)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #Treeview-------------------------------------------------------------END

#--------------Frame2--------------
        self.frame3=Frame(self.f1, bg=bgcol)
        self.frame3.place(x=1000, y=355)

        self.List3=[]
        
        #List3 row (0-2) column (0-1)
        self.List3.append(Label(self.frame3, text="કુલ રકમ :", font="arial 10 bold", bg=bgcol))
        self.List3.append(Label(self.frame3, text="7000", font="arial 10 bold underline", fg="red", bg=bgcol))
        self.List3.append(ttk.Combobox(self.frame3, state="readonly", font="arial 11 bold", width=20))
        self.List3[2]["values"]=("કેશ પેમેન્ટ", "પેમેન્ટ બાકી")
        self.List3[2].current(0)
        self.List3.append(Button(self.frame3, text="બિલ કાઢો", font="arial 10 bold", width=20, bd=3, bg=btncol, fg="white"))
        
        self.List3[0].grid(row=0, column=0, sticky=W, pady=5)
        self.List3[1].grid(row=0, column=1, pady=5)
        self.List3[2].grid(row=1, column=0, columnspan=2, pady=5)
        self.List3[3].grid(row=2, column=0, columnspan=2, pady=5)

        self.show_all_bill_item()


    def selectItem(self, a):
        treeItem = self.tree.focus()
        try:
            for i in range(2,8):
                self.List2[i][1].config(text=self.tree.item(treeItem)['values'][i-2])
            self.List2[8][1].delete(0, END)
            self.List2[8][1].insert(0, self.tree.item(treeItem)['values'][6])
        except IndexError as e:
            pass

    def show_all_bill_item(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        
        curr.execute("select * from tempbill")
        self.billlist=curr.fetchall()
        if len(self.billlist)!=0:
            self.tree.delete(*self.tree.get_children())
            for row in self.billlist:
                self.tree.insert("", END, values=row[2:])
        conn.commit()
        conn.close()
    
    def customer_search(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        x=self.List2[0][1].get()
        if x!="":
            curr.execute("select * from customerlist where CMobileNo="+x)
            self.clist=curr.fetchall()
            if len(self.clist)!=0:
                self.List2[0][4].config(text=self.clist[0][1]+" "+self.clist[0][2]+" "+self.clist[0][3])
                self.List2[0][6].config(text=self.clist[0][0])
                self.List2[0][8].config(text=self.clist[0][4])
        conn.commit()
        conn.close()

    def product_search(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        x=self.List2[1][1].get()
        if x!="":
            curr.execute("select * from productlist where PID="+x)
            self.plist=curr.fetchall()
            if len(self.plist)!=0:
                self.List2[2][1].config(text=self.plist[0][0])
                self.List2[3][1].config(text=self.plist[0][3])
                self.List2[4][1].config(text=self.plist[0][2])
                self.List2[5][1].config(text=self.plist[0][1])
                self.List2[6][1].config(text=self.plist[0][4])
                self.List2[7][1].config(text=self.plist[0][6])
        conn.commit()
        conn.close()

    def add_item_into_bill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        try:
            if str(self.List2[0][6].cget("text"))!="":
                curr.execute("insert into tempbill values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    self.List2[0][6].cget("text"),
                                    self.List1[1].cget("text"),
                                    self.List2[2][1].cget("text"),
                                    self.List2[3][1].cget("text"),
                                    self.List2[4][1].cget("text"),
                                    self.List2[5][1].cget("text"),
                                    self.List2[6][1].cget("text"),
                                    self.List2[7][1].cget("text"),
                                    self.quantity.get(),
                                    self.List2[7][1].cget("text")*int(self.quantity.get())
                                )
                            )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
        self.show_all_bill_item()

    def update_item_into_bill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        curr.execute("SELECT COUNT(*) FROM tempbill WHERE PID="+str(self.List2[2][1].cget("text")))
        x=curr.fetchall()
        if x == ((1,),):
            curr.execute("UPDATE tempbill SET Quantity="+self.quantity.get()
                        +", TotalPrice="+str(self.List2[7][1].cget("text")*int(self.quantity.get()))
                        +" WHERE PID="+str(self.List2[2][1].cget("text")))
        conn.commit()
        conn.close()
        self.show_all_bill_item()

    def delete_item_into_bill(self):
        if str(self.List2[2][1].cget("text"))!="":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="DBHariAgro")
            curr=conn.cursor()
            curr.execute("DELETE FROM tempbill WHERE PID="+str(self.List2[2][1].cget("text")))
            conn.commit()
            conn.close()
        self.show_all_bill_item()

    def create_new_bill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        curr.execute("DELETE FROM tempbill")
        conn.commit()
        conn.close()

        self.cdate=datetime.datetime.now()
        self.List1[1].config(text=self.cdate.strftime("%y%m%d%H%M"))
        self.List1[3].config(text=self.cdate.strftime("%d %b %Y"))
        self.List2[0][1].delete(0, END)
        self.List2[0][4].config(text="")
        self.List2[0][6].config(text="")
        self.List2[0][8].config(text="")
        self.List2[1][1].delete(0, END)
        for i in range(2,8):
            self.List2[i][1].config(text="")
        self.List2[8][1].delete(0, END)
        self.List2[8][1].insert(0, 1)
        self.show_all_bill_item()












class customerClass:
    def __init__(self, frame):
        self.f2=frame














class productClass:
    def __init__(self, frame):
        self.f3=frame














conn=pymysql.connect(host="localhost",
                    user="root",
                    password="")
curr=conn.cursor()
curr.execute("CREATE DATABASE IF NOT EXISTS DBHariAgro")
curr.execute("CREATE TABLE IF NOT EXISTS DBHariAgro.productlist (PID int NOT NULL UNIQUE, PBatchNo varchar(20), CompanyName varchar(30), PName varchar(40), PNetContent int, PPrintedPrice int, PSellingPrice int, PBuyingPrice int)")
curr.execute("CREATE TABLE IF NOT EXISTS DBHariAgro.customerlist (CMobileNo bigint(15) NOT NULL UNIQUE, CFirstName varchar(20), CMiddleName varchar(20), CLastName varchar(20), CVillage varchar(20))")
curr.execute("CREATE TABLE IF NOT EXISTS DBHariAgro.tempbill (CMobileNo bigint(15), BillNo bigint(15), PID int NOT NULL UNIQUE, PName varchar(40), CompanyName varchar(30), PBatchNo varchar(20), PNetContent int, PSellingPrice int, Quantity int, TotalPrice int)")
curr.execute("DELETE FROM DBHariAgro.tempbill")
conn.commit()
conn.close()

bgcol="#B8D4BD"
btncol="#3C4ACA"

root=Tk()
root.title("શ્રી હરી એગ્રો સેન્ટર - Billing Software")
root.geometry("1360x730+0+0")
root.configure(background=bgcol)

heading=Label(root, text="શ્રી હરી એગ્રો સેન્ટર", font=("times new roman", 30, "bold"), relief=GROOVE, bg=bgcol, fg="#0F9D58", pady=10, bd=5)
heading.pack(fill=X)

iframe=Frame(root, bg=bgcol)
iframe.place(x=0, y=80, relheight=1)

style=ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background=bgcol, 
            fieldbackground=bgcol, foreground="black")

f1=LabelFrame(root, text="બિલની માહિતી", font=("times new roman", 11, "bold"), bg=bgcol, fg="#DE3163")
f2=LabelFrame(root, text="ગ્રાહકની માહિતી", font=("times new roman", 11, "bold"), bg=bgcol, fg="#DE3163")
f3=LabelFrame(root, text="દવાની માહિતી", font=("times new roman", 11, "bold"), bg=bgcol, fg="#DE3163")

for frame in (f1, f2, f3):
    frame.place(x=150, y=80, width=1200, height=600)

f1_obj=generateBill(f1)
f2_obj=customerClass(f2)
f3_obj=productClass(f3)

btnfont=("Verdana", 12, "bold")
left_manu1=Button(iframe, text="બિલ જનરેટ કરો", font=btnfont, relief=GROOVE, bg=bgcol, fg=btncol, borderwidth=0, command=lambda:f1.tkraise())
left_manu1.grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
left_manu2=Button(iframe, text="ગ્રાહકની માહિતી", font=btnfont, relief=GROOVE, bg=bgcol, fg=btncol, borderwidth=0, command=lambda:f2.tkraise())
left_manu2.grid(row=1, column=0, ipady=10, ipadx=10, sticky=W)
left_manu3=Button(iframe, text="દવાની માહિતી", font=btnfont, relief=GROOVE, bg=bgcol, fg=btncol, borderwidth=0, command=lambda:f3.tkraise())
left_manu3.grid(row=2, column=0, ipady=10, ipadx=10, sticky=W)

f1.tkraise()
root.mainloop()