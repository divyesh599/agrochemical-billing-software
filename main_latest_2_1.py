import tkinter
from tkinter import *
from tkinter import ttk
import pymysql
import datetime
import webbrowser




class generateBill:
    def __init__(self):
        #---variables------
        self.cdate=datetime.datetime.now()
        self.selectedC=""
        self.selectedP=""
        self.billno=self.cdate.strftime("%y%m%d%H%M")
        self.billdate=self.cdate.strftime("%d %b %Y")


        self.Fnewbill=Toplevel(root)
        self.Fnewbill.protocol("WM_DELETE_WINDOW", self.close_window)
        self.Fnewbill.title("Add New Bill")
        self.Fnewbill.geometry("1150x500+150+150")
        self.Fnewbill.configure(background=colbg)
        

        #--------------Frame1-------------------------------------------------------------------------------
        self.frame1=Frame(self.Fnewbill, bg=colbg)
        self.frame1.place(x=698, y=10)

        Label(self.frame1, text="બિલ નંબર :", anchor=E, width=15, bg=colbg).pack(side=LEFT, pady=10)
        Label(self.frame1, text=self.billno, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=12).pack(side=LEFT)
        Label(self.frame1, text="બિલની તારીખ :", bg=colbg, anchor=E, width=12).pack(side=LEFT)
        Label(self.frame1, text=self.billdate, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=15).pack(side=LEFT)
        #Button(self.frame1, text="Refresh Bill", font="arial 10 bold", width=15, bd=2, bg=colbtn, fg="white").pack(side=LEFT)


        #--------------Frame2-------------------------------------------------------------------------------
        self.frame2=Frame(self.Fnewbill, bg=colbg)
        self.frame2.place(x=0, y=70)

        Label(self.frame2, text="Search Customer * :", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.ECust=Entry(self.frame2, font="arial 10", fg="red", width=30, bd=2)
        self.ECust.grid(row=0, column=1, columnspan=2, sticky=W)
        self.ECust.bind('<KeyRelease>', self.search_call_cust)


        #--------------Customer SearchFrame1--------------
        self.sFrame1=Frame(self.Fnewbill)

        self.clistbox=Listbox(self.sFrame1, width=70)
        self.clistbox.pack()
        self.clistbox.bind("<Double-1>", self.on2clickL1)
        self.clistbox.bind("<<ListboxSelect>>", self.onSelectL1)
        Button(self.sFrame1, text="Add", command=self.addCustInfo).pack(fill=X)


        #--------------Frame3--------------------------------------------------------------------------------
        self.frame3=Frame(self.Fnewbill, bg=colbg)
        self.frame3.place(x=340, y=70)

        Label(self.frame3, text="નામ :", anchor=E, width=15, bg=colbg).grid(row=0, column=0)
        self.cnamelbl=Label(self.frame3, anchor=W, width=30, font="arial 10 bold", bg=colbg, fg="red")
        self.cnamelbl.grid(row=0, column=1)
        Label(self.frame3, text="મોબાઈલ નંબર :", anchor=E, width=15, bg=colbg).grid(row=0, column=2)
        self.mobilelbl=Label(self.frame3, anchor=W, width=12, font="arial 10 bold", bg=colbg, fg="red")
        self.mobilelbl.grid(row=0, column=3)
        Label(self.frame3, text="ગામ :", anchor=E, width=12, bg=colbg).grid(row=0, column=4)
        self.villagelbl=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red")
        self.villagelbl.grid(row=0, column=5)


        #--------------Frame4----------------------------------------------------------------------------------
        self.frame4=Frame(self.Fnewbill, bg=colbg)
        self.frame4.place(x=0, y=110)

        Label(self.frame4, text="Search Product    :", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.EProd=Entry(self.frame4, font="arial 10", fg="red", width=30, bd=2, state="disabled")
        self.EProd.grid(row=0, column=1, columnspan=2, sticky=W)
        self.EProd.bind('<KeyRelease>', self.search_call_prod)

        #--------------Product SearchFrame2--------------
        self.sFrame2=Frame(self.Fnewbill)

        self.plistbox=Listbox(self.sFrame2, width=90)
        self.plistbox.pack()
        self.plistbox.bind("<Double-1>", self.on2clickL2)
        self.plistbox.bind("<<ListboxSelect>>", self.onSelectL2)
        Button(self.sFrame2, text="Add", command=self.addProdInfo).pack(fill=X)


        # Frame 5 Table---------------------------------------------------------------------------------------
        self.frame5=Frame(self.Fnewbill, bg=colbg)
        self.frame5.place(x=10, y=150, relwidth=1, height=470)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame5, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), show="headings", height=7)
        self.tree.place(x=0, y=0, width=1110)

        self.tree.column("#1", anchor=CENTER, width=30)
        self.tree.column("#2", anchor=CENTER, width=200)
        self.tree.column("#3", anchor=CENTER, width=150)
        self.tree.column("#4", anchor=CENTER, width=80)
        self.tree.column("#5", anchor=CENTER, width=90)
        self.tree.column("#6", anchor=CENTER, width=80)
        self.tree.column("#7", anchor=CENTER, width=80)
        self.tree.column("#8", anchor=CENTER, width=80)
        self.tree.heading("#1", text="PID")
        self.tree.heading("#2", text="Product name")
        self.tree.heading("#3", text="Company name")
        self.tree.heading("#4", text="Batch no.")
        self.tree.heading("#5", text="Net Content (ml/gm)")
        self.tree.heading("#6", text="Selling price (Rs.)")
        self.tree.heading("#7", text="Quantity")
        self.tree.heading("#8", text="Amount (Rs.)")

        self.v=Scrollbar(self.frame5, orient="vertical")
        self.v.place(x=1110, y=0, height=170)
        self.v.config(command=self.tree.yview)

        '''self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=465, width=763)
        self.h.config(command=self.tree.xview)'''
        self.tree.configure(yscrollcommand=self.v.set) #xscrollcommand=self.h.set

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #self.show_all_product()
        #Treeview----------------END


        #--------------Frame6----------------------------------------------------------------------------------
        self.frame6=Frame(self.Fnewbill, bg=colbg)
        self.frame6.place(x=820, y=330)

        Label(self.frame6, text="Total Amount :", anchor=E, width=15, bg=colbg).grid(row=0, column=0)
        self.totalamonut=Label(self.frame6, text=0, font="arial 20 bold", bg=colbg, fg="red", anchor=W)
        self.totalamonut.grid(row=0, column=1)
        Label(self.frame6, text="Rs.", anchor=E, bg=colbg).grid(row=0, column=2)
        Label(self.frame6, text="Cash / Debit :", anchor=E, width=15, bg=colbg).grid(row=1, column=0)
        self.cd=ttk.Combobox(self.frame6, state="readonly")
        self.cd.grid(row=1, column=1)
        self.cd["values"]=("Cash", "Debit")
        self.cd.current(1)


        # Frame 7 Buttons------------------------------------------------------------------------------------
        self.frame7=Frame(self.Fnewbill, bg=colbg)
        self.frame7.place(x=10, y=320)
        Label(self.frame7, text="PID :", anchor=E, width=5, bg=colbg).grid(row=0, column=0)
        self.pidlbl=Label(self.frame7, text="", anchor=W, width=5, bg=colbg)
        self.pidlbl.grid(row=0, column=1)
        Label(self.frame7, text="Selling Price :", anchor=E, width=10, bg=colbg).grid(row=0, column=2)
        self.Etree1=Entry(self.frame7, font="arial 10", fg="red", width=10, bd=2)
        self.Etree1.grid(row=0, column=3, padx=10)
        Label(self.frame7, text="Quantity :", anchor=E, width=10, bg=colbg).grid(row=0, column=4)
        self.Etree2=Entry(self.frame7, font="arial 10", fg="red", width=10, bd=2)
        self.Etree2.grid(row=0, column=5, padx=10)
        Button(self.frame7, text="Edit", command=self.edit_into_tableI, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=2).grid(row=0, column=6)
        Button(self.frame7, text="Delete", command=self.delete_into_tableI, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=2).grid(row=0, column=7)


        # Frame 8 Buttons------------------------------------------------------------------------------------
        self.frame8=Frame(self.Fnewbill, bg=colbg)
        self.frame8.place(x=900, y=450)
        Button(self.frame8, text="OK", command=self.create_bill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame8, text="Print", font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)

        self.clear_tempbill_table()


    def create_bill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        if self.mobilelbl["text"] != "":
            curr.execute("insert into subbilldetails select * from tempsubbill")
            curr.execute("insert into allbills values(%s, %s, %s, %s, %s, %s, %s)",
                            (self.billdate,
                            self.billno,
                            self.mobilelbl["text"],
                            self.cnamelbl["text"],
                            self.villagelbl["text"],
                            self.cd.get(),
                            self.totalamonut["text"])
                        )
            conn.commit()
            conn.close()
            self.close_window()
        

    def selectItem(self, e):
        treeItem = self.tree.focus()
        try:
            self.pidlbl.config(text=self.tree.item(treeItem)['values'][0])
            self.Etree1.delete(0,END)
            self.Etree1.insert(0, self.tree.item(treeItem)['values'][5])
            self.Etree2.delete(0,END)
            self.Etree2.insert(0, self.tree.item(treeItem)['values'][6])
        except:
            self.pidlbl.config(text="")
            self.Etree1.delete(0,END)
            self.Etree2.delete(0,END)


    def edit_into_tableI(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        if self.pidlbl["text"] !="":
            curr.execute("UPDATE tempsubbill SET Qty="+self.Etree2.get()
                        +", SellPrice="+self.Etree1.get()
                        +", Amount="+str(int(self.Etree1.get())*int(self.Etree2.get()))
                        +" WHERE PID="+str(self.pidlbl["text"]))
        conn.commit()
        conn.close()
        self.total_sum_amount()
        self.show_tempbill()


    def delete_into_tableI(self):
        if self.pidlbl["text"] !="":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            curr.execute("DELETE FROM tempsubbill WHERE PID="+str(self.pidlbl["text"]))
            conn.commit()
            conn.close()
        self.total_sum_amount()
        self.show_tempbill()


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
                self.cnamelbl.config(text=clist[0][1]+" "+clist[0][2]+" "+clist[0][3])
                self.mobilelbl.config(text=clist[0][0])
                self.villagelbl.config(text=clist[0][4])
        conn.commit()
        conn.close()
        self.ECust.delete(0, END)
        self.sFrame1.place_forget()
        self.EProd.config(state="normal")


    def search_call_cust(self, e):
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


    def on2clickL2(self, evt):
        varx=self.plistbox.curselection()
        if varx:
            i=self.plistbox.get(varx).index(" ")
            self.selectedP=self.plistbox.get(varx)[:i]
        self.addProdInfo()


    def onSelectL2(self, evt):
        varx=self.plistbox.curselection()
        if varx:
            i=self.plistbox.get(varx).index(" ")
            self.selectedP=self.plistbox.get(varx)[:i]


    def addProdInfo(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        if self.selectedP!="":
            curr.execute("select * from productdata where PID="+self.selectedP)
            plist=curr.fetchall()
            if len(plist)!=0:
                try:
                    curr.execute("insert into tempsubbill values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                    (self.billdate,
                                    self.mobilelbl["text"],
                                    self.billno,
                                    plist[0][0],
                                    plist[0][1]+ "  " +plist[0][2],
                                    plist[0][3],
                                    plist[0][4],
                                    plist[0][5],
                                    plist[0][7],
                                    1,
                                    plist[0][7])
                                )
                except pymysql.err.Error as e:
                    pass
        conn.commit()
        conn.close()
        self.total_sum_amount()
        self.show_tempbill()
        self.EProd.delete(0, END)
        self.sFrame2.place_forget()


    def search_call_prod(self, e):
        if self.EProd.get() != "":
            self.sFrame2.lift()
            self.sFrame2.place(x=122, y=133)
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            varx=self.EProd.get()
            curr.execute("select * from productdata where PName LIKE '%"+ varx +"%' OR TechName LIKE '%"+ varx +"%' OR Company LIKE '%"+ varx +"%' OR BatchNo LIKE '%"+ varx +"%'")
            plist=curr.fetchall()
            self.plistbox.delete(0, END)
            if len(plist)!=0:
                for row in plist:
                    s=str(row[0])+"    "+row[1]+" "+row[2]+"    "+row[3]+"    "+row[4]+"    "+str(row[5])+" ml/gm"+"    "+str(row[7])+" Rs."
                    self.plistbox.insert("end", s)
        else:
            self.sFrame2.place_forget()


    def show_tempbill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        curr.execute("select * from tempsubbill")
        plist=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in plist:
            self.tree.insert("", END, values=row[3:])
        conn.commit()
        conn.close()


    def total_sum_amount(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        try:
            curr.execute("select sum(Amount) from tempsubbill")
            total=curr.fetchall()
            if total[0][0] != None:
                self.totalamonut.config(text=total[0][0])
            else:
                self.totalamonut.config(text=0)
        except pymysql.err.Error as e:
            pass
        conn.commit()
        conn.close()


    def clear_tempbill_table(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        curr.execute("TRUNCATE TABLE tempsubbill")
        conn.commit()
        conn.close()


    def close_window(self):
        self.clear_tempbill_table()
        self.Fnewbill.destroy()

















class allBills:
    def __init__(self, F):
        self.Fbills=F
        
        # All Variables -------------------------------------------------------------------------------------



        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fbills, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Bill :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.Etext=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        self.Etext.bind('<KeyRelease>', self.search_call_bill)


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
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fbills, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        Button(self.frame3, text="New", command=self.newBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=0)
        Button(self.frame3, text="Edit", command=self.editBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=1)
        Button(self.frame3, text="Delete", command=self.deleteBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=2)
        Button(self.frame3, text="Info", command=self.billInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=4)

        self.show_all_bill()


    def newBill(self):
        obj=generateBill()

    def editBill(self):
        pass
    def deleteBill(self):
        pass
    def billInfo(self):
        pass


    def search_call_bill(self, e):
        if self.Etext.get() != "":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            varx=self.Etext.get()
            curr.execute("select * from allbills where BillDate LIKE '%"+ varx +"%' OR BillNo LIKE '%"+ varx +"%' OR MobileNo LIKE '%"+ varx +"%' OR Name LIKE '%"+ varx +"%' OR City LIKE '%"+ varx +"%'")
            blist=curr.fetchall()
            blist=blist[::-1]
            self.tree.delete(*self.tree.get_children())
            for row in blist:
                self.tree.insert("", END, values=row)
            conn.commit()
            conn.close()
        else:
            self.show_all_bill()


    def show_all_bill(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        curr.execute("select * from allbills")
        blist=curr.fetchall()
        blist=blist[::-1]
        self.tree.delete(*self.tree.get_children())
        for row in blist:
            self.tree.insert("", END, values=row)
        conn.commit()
        conn.close()














class customerClass:
    def __init__(self, F):
        self.Fcust=F
        
        # All Variables -------------------------------------------------------------------------------------


        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fcust, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Customer :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.Etext=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        self.Etext.bind('<KeyRelease>', self.search_call_cust)


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
        self.show_all_cust()
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fcust, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        Button(self.frame3, text="New", command=self.newCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=0)
        #Button(self.frame3, text="Edit", command=self.editCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=1)
        #Button(self.frame3, text="Delete", command=self.deleteCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=2)
        #Button(self.frame3, text="Info", command=self.custInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=4)



    def show_all_cust(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        curr.execute("select * from customerdata")
        clist=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in clist:
            self.tree.insert("", END, values=(row[0], row[1]+" "+row[2]+" "+row[3], row[4], row[5]))
        conn.commit()
        conn.close()

    def search_call_cust(self, e):
        if self.Etext.get() != "":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            varx=self.Etext.get()
            curr.execute("select * from customerdata where MobileNo LIKE '%"+ varx +"%' OR FName LIKE '%"+ varx +"%' OR MName LIKE '%"+ varx +"%' OR LName LIKE '%"+ varx +"%' OR City LIKE '%"+ varx +"%'")
            clist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in clist:
                self.tree.insert("", END, values=(row[0], row[1]+" "+row[2]+" "+row[3], row[4], row[5]))
            conn.commit()
            conn.close()
        else:
            self.show_all_cust()

    def newCust(self):
        pass
    def editCust(self):
        pass
    def deleteCust(self):
        pass
    def custInfo(self):
        pass


















class productClass:
    def __init__(self, F):
        self.Fprod=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.var1=""

        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fprod, bg=colbg)
        self.frame1.place(x=0, y=20)

        Label(self.frame1, text="Search Product :", font="arial 10", bg=colbg, fg=colbtn).grid(row=0, column=0, sticky=W, padx=10)
        self.Etext=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.Etext.grid(row=0, column=1, columnspan=2, sticky=W)
        self.Etext.bind('<KeyRelease>', self.search_call_prod)


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

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        self.tree.bind("<Double-1>", self.double_click_event)
        self.show_all_prod()
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fprod, bg=colbg)
        self.frame3.place(x=10, y=520, relwidth=1)
        Button(self.frame3, text="New", command=self.newProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=0)
        Button(self.frame3, text="Edit", command=self.editProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=1)
        Button(self.frame3, text="Delete", command=self.deleteProd, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).grid(row=0, column=2)


    def selectItem(self, a):
        treeItem = self.tree.focus()
        try:
            self.var1=self.tree.item(treeItem)['values']
        except:
            self.var1=""
    
    def double_click_event(self, a):
        treeItem = self.tree.focus()
        self.var1=self.tree.item(treeItem)['values']
        self.editProd()


    def show_all_prod(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        curr.execute("select * from productdata")
        plist=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in plist:
            self.tree.insert("", END, values=row)
        conn.commit()
        conn.close()


    def search_call_prod(self, e):
        if self.Etext.get() != "":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="Database23Nov")
            curr=conn.cursor()
            varx=self.Etext.get()
            curr.execute("select * from productdata where PName LIKE '%"+ varx +"%' OR TechName LIKE '%"+ varx +"%' OR Company LIKE '%"+ varx +"%' OR BatchNo LIKE '%"+ varx +"%'")
            plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in plist:
                self.tree.insert("", END, values=row)
            conn.commit()
            conn.close()
        else:
            self.show_all_prod()

    def newProd(self):
        ogj=modifyProd("")
    def editProd(self):
        ogj=modifyProd(self.var1)
    def deleteProd(self):
        obj=deleteProduct(self.var1)




class modifyProd:
    def __init__(self, var1):
        # All Variables -------------------------------------------------------------------------------------
        self.selectedP=var1
        self.pid=""

        
        self.Fmodifyprod=Toplevel(root)
        self.Fmodifyprod.title("Add New Product")
        self.Fmodifyprod.geometry("600x400")        #+300+220
        center(self.Fmodifyprod)
        self.Fmodifyprod.grab_set()
        self.Fmodifyprod.configure(background=colbg)

        #--------------Frame1--------------------------------------------------------------------------------
        self.frame1=Frame(self.Fmodifyprod, bg=colbg)
        self.frame1.place(x=40, y=40)

        Label(self.frame1, text="PID :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=0, column=0, pady=5)
        self.pidlbl=Label(self.frame1, font="arial 10", anchor=W, bg=colbg)
        self.pidlbl.grid(row=0, column=1, pady=5)
        Label(self.frame1, text="Product name :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=1, column=0, pady=5)
        Label(self.frame1, text="Technical name :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=2, column=0, pady=5)
        Label(self.frame1, text="Company name :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=3, column=0, pady=5)
        Label(self.frame1, text="Batch no. :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=4, column=0, pady=5)
        Label(self.frame1, text="Net Content (ml/gm) :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=5, column=0, pady=5)
        Label(self.frame1, text="Printed price (Rs.) :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=6, column=0, pady=5)
        Label(self.frame1, text="Selling price (Rs.) :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=7, column=0, pady=5)
        Label(self.frame1, text="Buying price (Rs.) :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=8, column=0, pady=5)

        self.list1=[]

        for i in range(8):
            self.list1.append(Entry(self.frame1, width=40))
            self.list1[i].grid(row=i+1, column=1, padx=10)
        
        Button(self.frame1, text="Update Into ProductList", command=self.addProd, font="arial 10 bold", bg=colbtn, fg="white", bd=5).grid(row=9, column=1, pady=10)

        self.modify_Entry()

    def modify_Entry(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        if self.selectedP == "":
            curr.execute("select count(PID) from productdata")
            self.pid=curr.fetchall()[0][0] + 1
        else:
            self.pid=self.selectedP[0]
            for i in range(8):
                self.list1[i].insert(0, self.selectedP[i+1])
        self.pidlbl.config(text=self.pid)


    def addProd(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="Database23Nov")
        curr=conn.cursor()
        try:
            if self.selectedP == "":
                curr.execute("insert into productdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (str(self.pidlbl["text"]),
                                self.list1[0].get(),
                                self.list1[1].get(),
                                self.list1[2].get(),
                                self.list1[3].get(),
                                self.list1[4].get(),
                                self.list1[5].get(),
                                self.list1[6].get(),
                                self.list1[7].get())
                            )
            else:
                curr.execute("UPDATE productdata SET PName='"+self.list1[0].get()
                            +"', TechName='"+self.list1[1].get()
                            +"', Company='"+self.list1[2].get()
                            +"', BatchNo='"+self.list1[3].get()
                            +"', NetContent="+self.list1[4].get()
                            +", PrintPrice="+self.list1[5].get()
                            +", SellPrice="+self.list1[6].get()
                            +", BuyPrice="+self.list1[7].get()
                            +" WHERE PID="+str(self.pidlbl["text"])
                            )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
        self.Fmodifyprod.destroy()
        objf3.show_all_prod()





class deleteProduct:
    def __init__(self, var1):

        # All Variables -------------------------------------------------------------------------------------
        self.selectedP=var1


        self.FdelProd=Toplevel(root)
        self.FdelProd.title("Delete Product")
        self.FdelProd.geometry("500x180")
        center(self.FdelProd)
        self.FdelProd.grab_set()
        self.FdelProd.configure(background=colbg)    

        #--------------Frame1--------------
        self.frame1=Frame(self.FdelProd, bg=colbg)
        self.frame1.place(x=40, y=40)
        print(var1)
        Label(self.frame1, text="Are you realy want to delete product?", font="arial 10", bg=colbg).grid(row=0, column=0, pady=5)
        Button(self.frame1, text="Delete Product", font="arial 10 bold", bg=colbtn, fg="white", bd=5).grid(row=1, column=0, pady=10)

















def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()


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
    PRIMARY KEY (BillNo, MobileNo))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.subbilldetails\
    (BillDate VARCHAR(20),\
    MobileNo BIGINT,\
    BillNo BIGINT,\
    PID INT,\
    Description VARCHAR(100),\
    Company VARCHAR(40),\
    BatchNo VARCHAR(20),\
    NetContent INT,\
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
    NetContent INT,\
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
Label(Fheading, text="|| શ્રી ગણેશાય નમ: ||", bg=colbg, fg=col1, width=160).grid(row=0, column=1)
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
Button(Fbtn, text="બિલની માહિતી", font=("", 11, "bold"), anchor=W, bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f1.tkraise()).pack(fill=X)
Button(Fbtn, text="ગ્રાહકની માહિતી", font=("", 11, "bold"), anchor=W, bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f2.tkraise()).pack(fill=X)
Button(Fbtn, text="દવાની માહિતી", font=("", 11, "bold"), anchor=W, bd=0, bg=colbg, fg=colbtn, pady=5, command=lambda:f3.tkraise()).pack(fill=X)







# Footer Frame ------------------------------------------------------------------------------------------------
FFoot=Frame(root, bg=colbg)
FFoot.place(x=510, y=700, relwidth=1) # x=140
link1=Label(FFoot, text="Build with     by Maganbhai (Divyesh Ranpariya)", font=("MV Boli", 10, "bold"), bg=colbg, fg="#264653", bd=0, padx=10)
link1.pack(side=LEFT)
link1.bind("<Button-1>", lambda e: callfooter("https://www.facebook.com/divyesh599/"))
Label(FFoot, image=imgheart, bd=0).place(x=92, y=3)



f3.tkraise()
root.state('zoomed')
root.mainloop()