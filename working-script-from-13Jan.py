from tkinter import *
from tkinter import ttk
import pymysql
import datetime
import webbrowser
"""from fpdf import FPDF"""
import socket



class generateBill:
    def __init__(self):
        #---variables--------------------------------------
        self.cdate=datetime.datetime.now()
        self.selected_cust=""
        self.selected_prod=""
        self.billno=self.cdate.strftime("%y%m%d%H%M")
        self.billdate=self.cdate.strftime("%d %b %Y")
        self.all_item=[]


        self.Fnewbill=Toplevel(root)
        #self.Fnewbill.protocol("WM_DELETE_WINDOW", self.close_window)
        self.Fnewbill.title("Add New Bill")
        self.Fnewbill.geometry("1150x500")
        center(self.Fnewbill)
        self.Fnewbill.grab_set()
        self.Fnewbill.configure(background=colbg)


        #--------------Frame1-------------------------------------------------------------------------------
        self.frame1=Frame(self.Fnewbill, bg=colbg)
        self.frame1.pack(pady=5)

        Label(self.frame1, text="Bill Date :", bg=colbg, anchor=E, width=15).pack(side=LEFT)
        Label(self.frame1, text=self.billdate, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=15).pack(side=LEFT)
        Label(self.frame1, text="Bill Number :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        Label(self.frame1, text=self.billno, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=15).pack(side=LEFT)




        #--------------Frame2-------------------------------------------------------------------------------
        self.frame2=Frame(self.Fnewbill, bg=colbg)
        self.frame2.pack(fill=X, pady=5, padx=10)

        Label(self.frame2, text="* Search Customer :", bg=colbg, fg=colbtn, width=15, anchor=E).pack(side=LEFT)
        self.ECust=Entry(self.frame2, bg=colbglight, bd=1, font="arial 10", fg="red", width=30)
        self.ECust.pack(side=LEFT)
        self.ECust.bind('<KeyRelease>', self.search_cust)

        #--------------Customer SearchFrame1--------------
        self.sFrame1=Frame(self.Fnewbill)

        self.clistbox=Listbox(self.sFrame1, width=70, bg=colbglight)
        self.clistbox.pack()
        self.clistbox.bind("<Double-1>", self.cust_two_click_evt)
        self.clistbox.bind("<<ListboxSelect>>", self.on_select_evt1)
        Button(self.sFrame1, text="Add", command=self.add_cust_info).pack(fill=X)


        #--------------Frame3--------------------------------------------------------------------------------
        self.frame3=Frame(self.Fnewbill, bg=colbg)
        self.frame3.pack(pady=5)

        Label(self.frame3, text="Name :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        self.cnamelbl=Label(self.frame3, anchor=W, width=30, font="arial 10 bold", bg=colbg, fg="red")
        self.cnamelbl.pack(side=LEFT)
        Label(self.frame3, text="Mobile No. :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        self.mobilelbl=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red")
        self.mobilelbl.pack(side=LEFT)
        Label(self.frame3, text="City :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        self.villagelbl=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red")
        self.villagelbl.pack(side=LEFT)



        #--------------Frame4----------------------------------------------------------------------------------
        self.frame4=Frame(self.Fnewbill, bg=colbg)
        self.frame4.pack(fill=X, pady=5, padx=10)

        Label(self.frame4, text="Search Product :", bg=colbg, fg=colbtn, width=15, anchor=E).pack(side=LEFT)
        self.EProd=Entry(self.frame4, bg=colbglight, bd=1, font="arial 10", fg="red", width=30)
        self.EProd.bind('<KeyRelease>', self.search_prod)

        #--------------Product SearchFrame2--------------
        self.sFrame2=Frame(self.Fnewbill)

        self.plistbox=Listbox(self.sFrame2, width=90, bg=colbglight)
        self.plistbox.pack()
        self.plistbox.bind("<Double-1>", self.prod_two_click_evt)
        self.plistbox.bind("<<ListboxSelect>>", self.on_select_evt2)
        Button(self.sFrame2, text="Add", command=self.add_prod_info).pack(fill=X)


        # Frame 5 Table---------------------------------------------------------------------------------------
        self.frame5=Frame(self.Fnewbill, bg=colbg)
        self.frame5.pack(fill=X, padx=10)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame5, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), show="headings", height=7)
        self.tree.pack(fill=X, expand=TRUE, side=LEFT)

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
        self.v.pack(side=LEFT, fill=Y)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #Treeview----------------END


        # Frame 6 Buttons------------------------------------------------------------------------------------
        self.frame6=Frame(self.Fnewbill, bg=colbg)
        self.frame6.pack(fill=X, padx=10)
        Label(self.frame6, text="PID :", anchor=E, bg=colbg).pack(side=LEFT)
        self.pidlbl=Label(self.frame6, text="", anchor=W, width=5, bg=colbg)
        self.pidlbl.pack(side=LEFT)
        Label(self.frame6, text="Selling Price :", anchor=E, width=10, bg=colbg).pack(side=LEFT)
        self.Etree1=Entry(self.frame6, font="arial 10", bg=colbglight, fg="red", width=10, bd=1)
        self.Etree1.pack(side=LEFT)
        Label(self.frame6, text="Quantity :", anchor=E, width=10, bg=colbg).pack(side=LEFT)
        self.Etree2=Entry(self.frame6, font="arial 10", bg=colbglight, fg="red", width=10, bd=1)
        self.Etree2.pack(side=LEFT)
        Button(self.frame6, text="Update", command=self.edit_into_table, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=2).pack(side=LEFT, padx=10)
        Button(self.frame6, text="Delete", command=self.delete_into_table, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=2).pack(side=LEFT)
        Label(self.frame6, text="* Including all taxes", font="arial 9 bold", bg=colbg).pack(side=RIGHT)


        #--------------Frame7----------------------------------------------------------------------------------
        self.frame7=Frame(self.Fnewbill, bg=colbg)
        self.frame7.pack(pady=10)

        Label(self.frame7, text="Total Amount :", anchor=E, width=15, bg=colbg).grid(row=0, column=0)
        self.totalamonut=Label(self.frame7, text=0, font="arial 20 bold", bg=colbg, fg="red", anchor=W)
        self.totalamonut.grid(row=0, column=1)
        Label(self.frame7, text="Rs.", anchor=E, bg=colbg).grid(row=0, column=2)
        Label(self.frame7, text="Cash / Debit :", anchor=E, width=15, bg=colbg).grid(row=1, column=0)
        self.cd=ttk.Combobox(self.frame7, state="readonly")
        self.cd.grid(row=1, column=1)
        self.cd["values"]=("Cash", "Debit")
        self.cd.current(1)


        # Frame 8 Buttons------------------------------------------------------------------------------------
        self.frame8=Frame(self.Fnewbill, bg=colbg)
        self.frame8.pack(side=BOTTOM, pady=10)
        Button(self.frame8, text="OK", command=self.create_bill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT, padx=10)
        Button(self.frame8, text="Print", font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT, padx=10)



    def search_cust(self, evt):
        if self.ECust.get() != "":
            self.sFrame1.lift()
            self.sFrame1.place(x=120, y=58)
            conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
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


    def search_prod(self, e):
        if self.EProd.get() != "":
            self.sFrame2.lift()
            self.sFrame2.place(x=120, y=121)
            conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
            curr=conn.cursor()
            varx=self.EProd.get()
            curr.execute("select * from productdata where PName LIKE '%"+ varx +"%' OR TechName LIKE '%"+ varx +"%' OR Company LIKE '%"+ varx +"%' OR BatchNo LIKE '%"+ varx +"%'")
            plist=curr.fetchall()
            self.plistbox.delete(0, END)
            if len(plist)!=0:
                for row in plist:
                    s=str(row[0])+"    "+row[1]+" "+row[2]+"    "+row[3]+"    "+row[4]+"    "+str(row[5])+" ml/gm"      #+"    "+str(row[7])+" Rs."
                    self.plistbox.insert("end", s)
        else:
            self.sFrame2.place_forget()


    def selectItem(self, evt):
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


    def edit_into_table(self):
        if self.pidlbl["text"] !="":
            for i in range(len(self.all_item)):
                if self.all_item[i][3]==int(self.pidlbl["text"]):
                    self.all_item[i][8]=int(self.Etree1.get())
                    self.all_item[i][9]=int(self.Etree2.get())
                    self.all_item[i][10]=int(self.Etree1.get())*int(self.Etree2.get())
                    break
        self.total_sum_amount()
        self.update_tree()


    def delete_into_table(self):
        if self.pidlbl["text"] !="":
            for i in range(len(self.all_item)):
                if self.all_item[i][3]==int(self.pidlbl["text"]):
                    self.all_item.pop(i)
                    break
        self.total_sum_amount()
        self.update_tree()


    def cust_two_click_evt(self, evt):
        varx=self.clistbox.curselection()
        if varx:
            self.selected_cust=self.clistbox.get(varx)[:10]
        self.add_cust_info()


    def on_select_evt1(self, evt):
        varx=self.clistbox.curselection()
        if varx:
            self.selected_cust=self.clistbox.get(varx)[:10]


    def add_cust_info(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        if self.selected_cust!="":
            curr.execute("select * from customerdata where MobileNo="+self.selected_cust)
            clist=curr.fetchall()
            if len(clist)!=0:
                self.cnamelbl.config(text=clist[0][1]+" "+clist[0][2]+" "+clist[0][3])
                self.mobilelbl.config(text=clist[0][0])
                self.villagelbl.config(text=clist[0][4])
        conn.commit()
        conn.close()
        self.ECust.delete(0, END)
        self.sFrame1.place_forget()
        self.EProd.pack(side=LEFT)


    def prod_two_click_evt(self, evt):
        varx=self.plistbox.curselection()
        if varx:
            i=self.plistbox.get(varx).index(" ")
            self.selected_prod=self.plistbox.get(varx)[:i]
        self.add_prod_info()


    def on_select_evt2(self, evt):
        varx=self.plistbox.curselection()
        if varx:
            i=self.plistbox.get(varx).index(" ")
            self.selected_prod=self.plistbox.get(varx)[:i]


    def add_prod_info(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        if self.selected_prod!="":
            curr.execute("select * from productdata where PID="+self.selected_prod)
            plist=curr.fetchall()
            plist=list(plist[0])
            if plist[0]!=0:
                flag=True
                for i in range(len(self.all_item)):
                    if self.all_item[i][3]==plist[0]:
                        flag=False
                        break
                if flag:
                    self.all_item.append([self.billdate, self.mobilelbl["text"], self.billno, plist[0], plist[1]+" "+plist[2], plist[3], plist[4], plist[5], plist[7], 1, plist[7]])
        conn.commit()
        conn.close()
        self.total_sum_amount()
        self.update_tree()
        self.EProd.delete(0, END)
        self.sFrame2.place_forget()


    def update_tree(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.all_item:
            self.tree.insert("", END, values=row[3:])


    def total_sum_amount(self):
        total=0
        for i in range(len(self.all_item)):
            total+=self.all_item[i][-1]
        self.totalamonut.config(text=total)


    def create_bill(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        if len(self.all_item) !=0:
            sql_data=""
            for i in range(len(self.all_item)):
                sql_data+="("
                for j in range(11):
                    if j == 10:
                         sql_data=sql_data+"'"+str(self.all_item[i][10])+"'),"
                    else:
                        sql_data=sql_data+"'"+str(self.all_item[i][j])+"',"
            
            curr.execute("insert into subbilldetails (`BillDate`, `MobileNo`, `BillNo`, `PID`, `Description`, `Company`, `BatchNo`, `NetContent`, `SellPrice`, `Qty`, `Amount`) VALUES"+sql_data[:-1])
            curr.execute("insert into allbills values(%s, %s, %s, %s, %s, %s, %s)",
                            (self.billdate,
                            self.billno,
                            self.mobilelbl["text"],
                            self.cnamelbl["text"],
                            self.villagelbl["text"],
                            self.cd.get(),
                            self.totalamonut["text"])
                        )
            if self.cd.get()=="Debit":
                curr.execute("insert into balancesheet values(%s, %s, %s, %s, %s, %s, %s)",
                                (self.mobilelbl["text"],
                                self.billdate,
                                self.billno,
                                "Debit Product Buying",
                                self.totalamonut["text"],
                                0,
                                -(self.totalamonut["text"]))
                            )
                curr.execute("select sum(Balance) from balancesheet where MobileNo="+str(self.mobilelbl["text"]))
                temp_var=curr.fetchall()
                curr.execute("update customerdata set Balance="+str(temp_var[0][0])+" where MobileNo="+str(self.mobilelbl["text"]))
            elif self.cd.get()=="Cash":
                curr.execute("insert into balancesheet values(%s, %s, %s, %s, %s, %s, %s)",
                                (self.mobilelbl["text"],
                                self.billdate,
                                self.billno,
                                "Cash payment",
                                self.totalamonut["text"],
                                0,
                                -(self.totalamonut["text"]))
                            )
                curr.execute("insert into balancesheet values(%s, %s, %s, %s, %s, %s, %s)",
                                (self.mobilelbl["text"],
                                self.billdate,
                                self.billno,
                                "Cash payment",
                                0,
                                self.totalamonut["text"],
                                self.totalamonut["text"])
                            )
            conn.commit()
            conn.close()
        self.Fnewbill.destroy()
        objf1.show_all_bill()
        objf2.show_all_cust()















class billInfoClass:
    def __init__(self, var1, var2):
        #---variables--------------------------------------
        self.billdetail=var1
        self.var2=var2
        self.billdate=self.billdetail[0]
        self.billno=self.billdetail[1]


        self.Fbillinfo=Toplevel(root)
        self.Fbillinfo.title("Bill No: "+str(self.billno)+" --> Name: "+self.billdetail[3]+" --> Date: "+self.billdate)
        self.Fbillinfo.geometry("1150x500")
        center(self.Fbillinfo)
        self.Fbillinfo.grab_set()
        self.Fbillinfo.configure(background=colbg)


        #--------------Frame1-------------------------------------------------------------------------------
        self.frame1=Frame(self.Fbillinfo, bg=colbg)
        self.frame1.pack(pady=10)

        Label(self.frame1, text="Bill Date :", bg=colbg, anchor=E, width=15).pack(side=LEFT)
        Label(self.frame1, text=self.billdate, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=15).pack(side=LEFT)
        Label(self.frame1, text="Bill Number :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        Label(self.frame1, text=self.billno, font="arial 10 bold", bg=colbg, fg="red", anchor=W, width=15).pack(side=LEFT)


        #--------------Frame2-----------------------------------------------------------------------------
        self.frame2=Frame(self.Fbillinfo, bg=colbg)
        self.frame2.pack(pady=20)

        Label(self.frame2, text="Name :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        Label(self.frame2, text=self.billdetail[3], anchor=W, width=30, font="arial 10 bold", bg=colbg, fg="red").pack(side=LEFT)
        Label(self.frame2, text="Mobile No. :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        Label(self.frame2, text=str(self.billdetail[2]), anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red").pack(side=LEFT)
        Label(self.frame2, text="City :", anchor=E, width=15, bg=colbg).pack(side=LEFT)
        Label(self.frame2, text=self.billdetail[4], anchor=W, width=15, font="arial 10 bold", bg=colbg, fg="red").pack(side=LEFT)


        #--------------Frame 3 Table----------------------------------------------------------------------
        self.frame3=Frame(self.Fbillinfo, bg=colbg)
        self.frame3.pack(fill=X, padx=10)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame3, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), show="headings", height=7)
        self.tree.pack(fill=X, expand=TRUE, side=LEFT)

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

        self.v=Scrollbar(self.frame3, orient="vertical")
        self.v.pack(side=LEFT, fill=Y)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)
        
        #Treeview----------------END


        # Frame 4 Buttons------------------------------------------------------------------------------------
        self.frame4=Frame(self.Fbillinfo, bg=colbg)
        self.frame4.pack(fill=X, padx=10)
        Label(self.frame4, text="* Including all taxes", font="arial 9 bold", bg=colbg).pack(side=RIGHT)


        #--------------Frame5----------------------------------------------------------------------------------
        self.frame5=Frame(self.Fbillinfo, bg=colbg)
        self.frame5.pack(pady=20)

        Label(self.frame5, text="Total Amount :", anchor=E, width=15, bg=colbg).grid(row=0, column=0)
        Label(self.frame5, text=self.billdetail[-1], font="arial 20 bold", bg=colbg, fg="red", anchor=W).grid(row=0, column=1)
        Label(self.frame5, text="Rs.", anchor=E, bg=colbg).grid(row=0, column=2)
        Label(self.frame5, text="Cash / Debit :", anchor=E, width=15, bg=colbg).grid(row=1, column=0)
        Label(self.frame5, text=self.billdetail[-2], font="arial 10 bold", width=15, bg=colbg).grid(row=1, column=1)
        

        # Frame 6 Buttons------------------------------------------------------------------------------------
        self.frame6=Frame(self.Fbillinfo, bg=colbg)
        self.frame6.pack(side=BOTTOM, pady=20)
        Button(self.frame6, text="Print", font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT, padx=5)
        if self.var2==0:
            Button(self.frame6, text="Delete", command=self.bill_info_delete, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT, padx=5)

        self.show_all_item()

    def show_all_item(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("select * from subbilldetails where BillNo="+str(self.billdetail[1]))
        item=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in item:
            self.tree.insert("", END, values=row[3:])
        conn.commit()
        conn.close()
    
    def bill_info_delete(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("delete from subbilldetails where BillNo="+str(self.billdetail[1]))
        curr.execute("delete from allbills where BillNo="+str(self.billdetail[1]))
        curr.execute("delete from balancesheet where BillNo="+str(self.billdetail[1]))
        curr.execute("select sum(Balance) from balancesheet where MobileNo="+str(self.billdetail[2]))
        temp_var=curr.fetchall()
        temp_var1=0
        if temp_var[0][0]!=None:
            temp_var1=temp_var[0][0]
        curr.execute("update customerdata set Balance="+str(temp_var1)+" where MobileNo="+str(self.billdetail[2]))
        conn.commit()
        conn.close()
        self.Fbillinfo.destroy()
        objf1.show_all_bill()
        objf2.show_all_cust()

























class allBills:
    """
    List of bills, and Button features to add, delete and update list.
    """
    def __init__(self, F):
        self.Fbills=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.var1=""


        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fbills, bg=colbg)
        self.frame1.pack(pady=20)
        Label(self.frame1, text="Search Bill :", font="arial 10", bg=colbg, fg=colbtn, width=15).pack(side=LEFT)
        self.Etext=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.Etext.pack(side=LEFT)
        self.Etext.bind('<KeyRelease>', self.search_call_bill)


        # Frame 2 Table-------------------------------------------------------------------------------------
        self.frame2=Frame(self.Fbills, bg=colbg)
        self.frame2.pack(fill=BOTH, expand=TRUE, padx=20)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7"), show="headings", height=5)
        self.tree.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.tree.column("#1", anchor=CENTER, width=80)
        self.tree.column("#2", anchor=CENTER, width=80)
        self.tree.column("#3", anchor=CENTER, width=80)
        self.tree.column("#4", anchor=CENTER, width=250)
        self.tree.column("#5", anchor=CENTER, width=80)
        self.tree.column("#6", anchor=CENTER, width=80)
        self.tree.column("#7", anchor=CENTER, width=80)
        self.tree.heading("#1", text="Bill Date")
        self.tree.heading("#2", text="Bill Number")
        self.tree.heading("#3", text="Mobile No.")
        self.tree.heading("#4", text="Customer Name")
        self.tree.heading("#5", text="City")
        self.tree.heading("#6", text="Cash / Debit")
        self.tree.heading("#7", text="Bill Amount")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.pack(side=RIGHT, fill=Y)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        self.tree.bind("<Double-1>", self.double_click_event)
        #Treeview----------------END

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fbills, bg=colbg)
        self.frame3.pack(fill=X, side=LEFT, padx=20)
        Button(self.frame3, text="New", command=self.newBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        #Button(self.frame3, text="Edit", command=self.editBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Delete", command=self.deleteBill, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Info", command=self.billInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)

        self.show_all_bill()



    def selectItem(self, evt):
        treeItem = self.tree.focus()
        try:
            self.var1=self.tree.item(treeItem)['values']
        except:
            self.var1=""
    
    def double_click_event(self, evt):
        treeItem = self.tree.focus()
        self.var1=self.tree.item(treeItem)['values']
        self.billInfo()

    def search_call_bill(self, evt):
        if self.Etext.get() != "":
            conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
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
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("select * from allbills")
        blist=curr.fetchall()
        blist=blist[::-1]
        self.tree.delete(*self.tree.get_children())
        for row in blist:
            self.tree.insert("", END, values=row)
        conn.commit()
        conn.close()


    def newBill(self):
        obj_new_bill=generateBill()
    def editBill(self):
        obj_edit_bill=instructionClass("You can not edit into Bill. You must need Admin access.")
    def deleteBill(self):
        if self.var1 != "":
            obj_delete_bill=billInfoClass(self.var1, 0)
        else:
            obj_delete_bill=instructionClass("Please, Select one Bill item from table.")
    def billInfo(self):
        if self.var1 != "":
            obj_bill_info=billInfoClass(self.var1, 1)
        else:
            obj_delete_bill=instructionClass("Please, Select one Bill item from table.")




















class customerClass:
    """
    List of Customer, and Button features to add, delete and update list.
    """
    def __init__(self, F):
        self.Fcust=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.var1=""

        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.Fcust, bg=colbg)
        self.frame1.pack(pady=20)
        Label(self.frame1, text="Search Customer :", font="arial 10", bg=colbg, fg=colbtn, width=15).pack(side=LEFT)
        self.Etext=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.Etext.pack(side=LEFT)
        self.Etext.bind('<KeyRelease>', self.search_cust)


        # Frame 2 Table---------------------------------------------------------------------------------------
        self.frame2=Frame(self.Fcust, bg=colbg)
        self.frame2.pack(fill=BOTH, expand=TRUE, padx=20)
        
        #Treeview----------------start        
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "5"), show="headings", height=5)
        self.tree.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.tree.column("#1", anchor=CENTER, width=80)
        self.tree.column("#2", anchor=CENTER, width=250)
        self.tree.column("#3", anchor=CENTER, width=80)
        self.tree.column("#4", anchor=CENTER, width=80)
        self.tree.column("#5", anchor=CENTER)
        self.tree.heading("#1", text="Mobile No.")
        self.tree.heading("#2", text="Name")
        self.tree.heading("#3", text="City")
        self.tree.heading("#4", text="Balance")
        self.tree.heading("#5", text="")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.pack(side=RIGHT, fill=Y)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        self.tree.bind("<Double-1>", self.double_click_event)
        #Treeview----------------END
        self.show_all_cust()
        

        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.Fcust, bg=colbg)
        self.frame3.pack(fill=X, side=LEFT, padx=20)
        Button(self.frame3, text="New", command=self.newCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Edit", command=self.editCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        #Button(self.frame3, text="Delete", command=self.deleteCust, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Info", command=self.custInfo, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)



    def selectItem(self, a):
        treeItem = self.tree.focus()
        try:
            self.var1=self.tree.item(treeItem)['values']
        except:
            self.var1=""


    def double_click_event(self, a):
        treeItem = self.tree.focus()
        self.var1=self.tree.item(treeItem)['values']
        self.custInfo()


    def show_all_cust(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("select * from customerdata")
        clist=curr.fetchall()
        clist=clist[::-1]
        self.tree.delete(*self.tree.get_children())
        for row in clist:
            self.tree.insert("", END, values=(row[0], row[1]+" "+row[2]+" "+row[3], row[4], row[5]))
        conn.commit()
        conn.close()


    def search_cust(self, e):
        if self.Etext.get() != "":
            conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
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
        obj_new_cust=modifyCust("")
    def editCust(self):
        if self.var1!="":
            obj_edit_cust=modifyCust(self.var1[0])
        else:
            self.newCust()
    def deleteCust(self):
        obj_delete_cust=instructionClass("You can not Delete Customer Data. You must need Admin access.")
    def custInfo(self):
        if self.var1!="":
            obj_cust_info=balanceSheet(self.var1)








class modifyCust:
    """
    To Add, Delete, or Update in Customer List.
    """
    def __init__(self, var1):
        # All Variables -------------------------------------------------------------------------------------
        self.selected_cust=var1


        self.FmodifyCust=Toplevel(root)
        if self.selected_cust=="":
            self.FmodifyCust.title("Add New Customer")
        else:
            self.FmodifyCust.title("Edit into Customer Data")
        self.FmodifyCust.geometry("600x350")
        center(self.FmodifyCust)
        self.FmodifyCust.grab_set()
        self.FmodifyCust.configure(background=colbg)

        self.headlbl=Label(self.FmodifyCust, text=" ", font="arial 12 bold", bg=colbg, fg=col1)
        self.headlbl.pack(pady=5)


        #--------------Frame1--------------------------------------------------------------------------------
        self.frame1=Frame(self.FmodifyCust, bg=colbg)
        self.frame1.pack()

        Label(self.frame1, text="Mobile No :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=0, column=0, pady=5)
        Label(self.frame1, text="First Name :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=1, column=0, pady=5)
        Label(self.frame1, text="Middle name :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=2, column=0, pady=5)
        Label(self.frame1, text="Surname :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=3, column=0, pady=5)
        Label(self.frame1, text="City :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=4, column=0, pady=5)
        Label(self.frame1, text="Balance :", font="arial 10", anchor=E, width=10, bg=colbg).grid(row=5, column=0, pady=5)

        self.list1=[]
        for i in range(5):
            self.list1.append(Entry(self.frame1, width=40))
            self.list1[i].grid(row=i, column=1, padx=10)

        self.Lbalance=Label(self.frame1, text="", font="arial 10", bg=colbg, fg="red")
        self.Lbalance.grid(row=5, column=1)


        # Button Frame ---------------------------------------------------
        self.frame2=Frame(self.FmodifyCust, bg=colbg)
        self.frame2.pack(pady=10)
        self.editbtn=Button(self.frame2, text=" ",command=self.addCust, font="arial 10 bold", bg=colbtn, fg="white", width=15, bd=5)
        self.editbtn.pack(side=LEFT, padx=5,)

        self.modify_Entry()



    def modify_Entry(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        if self.selected_cust == "":
            self.headlbl.config(text="Adding new Customer into database.")
            self.editbtn.config(text="Add")
            self.Lbalance.config(text="0")
            self.list1[0].config(fg="red")
        else:
            curr.execute("select * from customerdata where MobileNo="+str(self.selected_cust))
            item=curr.fetchall()
            for i in range(5):
                self.list1[i].insert(0, item[0][i])
            self.Lbalance.config(text=item[0][5])
            self.headlbl.config(text="Are you sure to edit into this customer?")
            self.editbtn.config(text="Update")
            self.list1[0].config(state=DISABLED)
        conn.commit()
        conn.close()


    def addCust(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        try:
            if self.selected_cust == "":
                curr.execute("insert into customerdata values(%s, %s, %s, %s, %s, %s)",
                                (self.list1[0].get(),
                                self.list1[1].get(),
                                self.list1[2].get(),
                                self.list1[3].get(),
                                self.list1[4].get(),
                                0)
                            )
            else:
                curr.execute("UPDATE customerdata SET FName='"+self.list1[1].get()
                            +"', MName='"+self.list1[2].get()
                            +"', LName='"+self.list1[3].get()
                            +"', City='"+self.list1[4].get()
                            +"' WHERE MobileNo="+str(self.list1[0].get())
                            )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
        self.FmodifyCust.destroy()
        objf2.show_all_cust()














class balanceSheet:
    """
    To view customer's debit, credit and total balance. 
    """
    def __init__(self, var1):
        #--------------All Variables-----------------------------------------------------------------------------
        self.var1=var1
        self.cdate=datetime.datetime.now()
        self.bill_date=self.cdate.strftime("%d %b %Y")


        self.child_frame=Toplevel(root)
        self.child_frame.title("Balance Sheet --> Mobile No. :  "+str(self.var1[0])+" --> Name :  "+ self.var1[1])
        self.child_frame.geometry("1300x500")
        center(self.child_frame)
        self.child_frame.grab_set()
        self.child_frame.configure(background=colbg, padx=20)


        #--------------Frame1-----------------------------------------------------------------------------
        self.frame1=Frame(self.child_frame, bg=colbg)
        self.frame1.pack(side=LEFT, fill=Y, pady=40)
        Label(self.frame1, text="Date :", bg=colbg, anchor=E, width=15).grid(row=0, column=0, pady=10)
        Label(self.frame1, text=self.bill_date, font="arial 10 bold", bg=colbg, anchor=W, width=30).grid(row=0, column=1)
        Label(self.frame1, text="Mobile No. :", anchor=E, width=15, bg=colbg).grid(row=1, column=0, pady=10)
        Label(self.frame1, text=self.var1[0], anchor=W, width=30, font="arial 10 bold", bg=colbg).grid(row=1, column=1)
        Label(self.frame1, text="Name :", anchor=E, width=15, bg=colbg).grid(row=2, column=0, pady=10)
        Label(self.frame1, text=self.var1[1], anchor=W, width=30, font="arial 10 bold", bg=colbg).grid(row=2, column=1)
        Label(self.frame1, text="City :", anchor=E, width=15, bg=colbg).grid(row=3, column=0, pady=10)
        Label(self.frame1, text=self.var1[2], anchor=W, width=30, font="arial 10 bold", bg=colbg).grid(row=3, column=1)
        Label(self.frame1, text="Total Balance :", anchor=E, width=15, bg=colbg).grid(row=4, column=0, pady=10)
        self.total=Label(self.frame1, anchor=W, width=15, font="arial 12 bold", bg=colbg, fg=col1)
        self.total.grid(row=4, column=1)


        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.frame1, bg=colbg)
        self.frame3.grid(row=5, column=0, columnspan=2, pady=20)
        Button(self.frame3, text="OK", font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=3).pack(side=LEFT, padx=10)
        Button(self.frame3, text="Print", font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=3).pack(side=LEFT, padx=10)


        #--------------Frame 2 Table----------------------------------------------------------------------
        self.frame2=Frame(self.child_frame, bg=colbg)
        self.frame2.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=10)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6"), show="headings", height=10)
        self.tree.pack(fill=BOTH, expand=TRUE, side=LEFT)
        self.tree.column("#1", anchor=CENTER, width=100)
        self.tree.column("#2", anchor=CENTER, width=100)
        self.tree.column("#3", anchor=CENTER, width=150)
        self.tree.column("#4", anchor=CENTER, width=100)
        self.tree.column("#5", anchor=CENTER, width=100)
        self.tree.column("#6", anchor=CENTER, width=100)
        self.tree.heading("#1", text="Date")
        self.tree.heading("#2", text="Bill No.")
        self.tree.heading("#3", text="Description")
        self.tree.heading("#4", text="Debit")
        self.tree.heading("#5", text="Credit")
        self.tree.heading("#6", text="Balance")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.pack(side=LEFT, fill=Y)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)
        #Treeview----------------------------------------------END

        self.show_all_records()


    def show_all_records(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("select * from balancesheet where MobileNo="+str(self.var1[0])+" order by BillNo desc")
        records=curr.fetchall()
        records[::-1]
        self.tree.delete(*self.tree.get_children())
        for row in records:
            self.tree.insert("", END, values=row[1:])
        
        curr.execute("select sum(Balance) from balancesheet where MobileNo="+str(self.var1[0]))
        temp_var=curr.fetchall()
        self.total.config(text=temp_var[0][0])
        conn.commit()
        conn.close()







































class productClass:
    """
    List of Product, and Button features to add, delete and update list.
    """
    def __init__(self, F):
        self.prod_frame=F
        
        # All Variables -------------------------------------------------------------------------------------
        self.var1=""


        # Frame 1 Searching----------------------------------------------------------------------------------
        self.frame1=Frame(self.prod_frame, bg=colbg)
        self.frame1.pack(pady=20)
        Label(self.frame1, text="Search Product :", font="arial 10", bg=colbg, fg=colbtn, width=15).pack(side=LEFT)
        self.search_entry=Entry(self.frame1, font="arial 11", fg="red", width=40, bd=2)
        self.search_entry.pack(side=LEFT)

        self.search_entry.bind('<KeyRelease>', self.search_prod)


        # Frame 2 Table---------------------------------------------------------------------------------------
        self.frame2=Frame(self.prod_frame, bg=colbg)
        self.frame2.pack(fill=BOTH, expand=TRUE, padx=20)

        #Treeview----------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"), show="headings", height=5)
        self.tree.pack(side=LEFT, expand=TRUE, fill=BOTH)
        self.tree.column("#1", anchor=CENTER, width=30)
        self.tree.column("#2", anchor=CENTER, width=80)
        self.tree.column("#3", anchor=CENTER, width=200)
        self.tree.column("#4", anchor=CENTER, width=200)
        self.tree.column("#5", anchor=CENTER, width=80)
        self.tree.column("#6", anchor=CENTER, width=80)
        self.tree.column("#7", anchor=CENTER, width=80)
        self.tree.column("#8", anchor=CENTER, width=80)
        #self.tree.column("#9", anchor=CENTER, width=80)
        self.tree.heading("#1", text="PID")
        self.tree.heading("#2", text="Product name")
        self.tree.heading("#3", text="Technical name")
        self.tree.heading("#4", text="Company name")
        self.tree.heading("#5", text="Batch no.")
        self.tree.heading("#6", text="Net Content")
        self.tree.heading("#7", text="Printed price")
        self.tree.heading("#8", text="Selling price")
        #self.tree.heading("#9", text="Buying price")

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.pack(side=RIGHT, fill=Y)
        self.v.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v.set)

        self.tree.bind('<<TreeviewSelect>>', self.tree_selected_item)
        self.tree.bind("<Double-1>", self.double_click_event)
        self.show_all_prod()
        #Treeview----------------END


        # Frame 3 Buttons------------------------------------------------------------------------------------
        self.frame3=Frame(self.prod_frame, bg=colbg)
        self.frame3.pack(fill=X, side=LEFT, padx=20)
        Button(self.frame3, text="New", command=self.new_prod, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Edit", command=self.edit_prod, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)
        Button(self.frame3, text="Delete", command=self.delete_prod, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=5).pack(side=LEFT)



    def tree_selected_item(self, a):
        treeItem = self.tree.focus()
        try:
            self.var1=self.tree.item(treeItem)['values'][0]
        except:
            self.var1=""


    def double_click_event(self, a):
        treeItem = self.tree.focus()
        self.var1=self.tree.item(treeItem)['values'][0]
        self.edit_prod()


    def show_all_prod(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("select * from productdata")
        plist=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in plist:
            self.tree.insert("", END, values=row[:8])
        conn.commit()
        conn.close()


    def search_prod(self, e):
        if self.search_entry.get() != "":
            conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
            curr=conn.cursor()
            varx=self.search_entry.get()
            curr.execute("select * from productdata where PName LIKE '%"+ varx +"%' OR TechName LIKE '%"+ varx +"%' OR Company LIKE '%"+ varx +"%' OR BatchNo LIKE '%"+ varx +"%'")
            plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in plist:
                self.tree.insert("", END, values=row[:8])
            conn.commit()
            conn.close()
        else:
            self.show_all_prod()

    def new_prod(self):
        ogj_new_prod=modifyProd("")
    def edit_prod(self):
        if self.var1!=0:
            ogj_edit_prod=modifyProd(self.var1)
    def delete_prod(self):
        if self.var1!=0:
            obj_delete_prod=modifyProd(self.var1)




class modifyProd:
    """
    To Add, Delete, or Update in Product List.
    """
    def __init__(self, var1):
        # All Variables -------------------------------------------------------------------------------------
        self.selected_prod=var1
        self.password_view="*"

        
        self.child_window=Toplevel(root)
        if self.selected_prod=="":
            self.child_window.title("Add New Product")
        else:
            self.child_window.title("Edit into Product Data")
        self.child_window.geometry("600x400")
        center(self.child_window)
        self.child_window.grab_set()
        self.child_window.configure(background=colbg)

        self.head_lbl=Label(self.child_window, text=" ", font="arial 12 bold", bg=colbg, fg=col1)
        self.head_lbl.pack(pady=5)
        
        #--------------Frame1--------------------------------------------------------------------------------
        self.frame1=Frame(self.child_window, bg=colbg)
        self.frame1.pack()
        Label(self.frame1, text="PID :", font="arial 10", anchor=E, width=20, bg=colbg).grid(row=0, column=0, pady=5)
        self.pid_lbl=Label(self.frame1, font="arial 10", anchor=W, bg=colbg)
        self.pid_lbl.grid(row=0, column=1, pady=5)
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

        self.list1[7].config(show="*")

        Button(self.frame1, text="Show", command=self.show, bg=colbg, bd=1).grid(row=8, column=2)


        # Button Frame2 ---------------------------------------------------
        self.frame2=Frame(self.child_window, bg=colbg)
        self.frame2.pack(pady=10)
        self.dlt_btn=Button(self.frame2, text="Delete", command=self.delete, font="arial 10 bold", bg=colbtn, fg="white", width=15, bd=5)
        self.edit_btn=Button(self.frame2, text=" ", command=self.add_Prod, font="arial 10 bold", bg=colbtn, fg="white", width=15, bd=5)
        self.edit_btn.pack(side=LEFT, padx=5)

        self.modify_Entry()



    def show(self):
        if self.password_view=="*":
            self.list1[7].config(show="")
            self.password_view=""
        else:
            self.list1[7].config(show="*")
            self.password_view="*"


    def modify_Entry(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        if self.selected_prod == "":
            curr.execute("select count(PID) from productdata")
            pid=curr.fetchall()[0][0]
            self.head_lbl.config(text="Adding new product into product list")
            self.edit_btn.config(text="Add")
        else:
            pid=self.selected_prod
            curr.execute("select * from productdata where PID="+str(pid))
            item=curr.fetchall()
            for i in range(8):
                self.list1[i].insert(0, item[0][i+1])
            self.head_lbl.config(text="Are you sure to edit into this product?")
            self.edit_btn.config(text="Update")
            self.dlt_btn.pack(side=LEFT, padx=5)
        self.pid_lbl.config(text=pid)


    def add_Prod(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        try:
            if self.selected_prod == "":
                curr.execute("insert into productdata values(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (str(self.pid_lbl["text"]),
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
                            +" WHERE PID="+str(self.pid_lbl["text"])
                            )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
        self.child_window.destroy()
        objf3.show_all_prod()


    def delete(self):
        conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="database23nov")
        curr=conn.cursor()
        curr.execute("DELETE FROM productdata WHERE PID="+str(self.pid_lbl["text"]))
        conn.commit()
        conn.close()
        self.child_window.destroy()
        objf3.show_all_prod()






class instructionClass:
    """
    To display error or messege.
    """
    def __init__(self, msg):
        self.msg=msg

        self.msg_frame=Toplevel(root)
        self.msg_frame.title("Instruction")
        self.msg_frame.geometry("600x150")
        center(self.msg_frame)
        self.msg_frame.grab_set()
        self.msg_frame.configure(background=colbg)

        Label(self.msg_frame, text=self.msg, font="arial 10", bg=colbg, fg=col1).pack(fill=BOTH, expand=True, padx=5, pady=10)
        Button(self.msg_frame, text="OK", command=self.ok, font="arial 10 bold", bg=colbtn, fg="white", width=10, bd=3).pack(side=BOTTOM, pady=10)


    def ok(self):
        self.msg_frame.destroy()









def center(win):
    """
    Centers a tkinter window
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











# Create Tables ---------------------------------------------------------------------------------------------
conn=pymysql.connect(host="127.0.0.1",user="root",password="")
curr=conn.cursor()

curr.execute("CREATE DATABASE IF NOT EXISTS database23nov")
curr.execute("CREATE TABLE IF NOT EXISTS database23nov.customerdata\
    (MobileNo BIGINT,\
    FName VARCHAR(20),\
    MName VARCHAR(40),\
    LName VARCHAR(20),\
    City VARCHAR(20),\
    Balance INT,\
    PRIMARY KEY (MobileNo))")
curr.execute("CREATE TABLE IF NOT EXISTS database23nov.productdata\
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
curr.execute("CREATE TABLE IF NOT EXISTS database23nov.allbills\
    (BillDate VARCHAR(20),\
    BillNo BIGINT,\
    MobileNo BIGINT,\
    Name VARCHAR(100),\
    City VARCHAR(20),\
    CashDebit VARCHAR(10),\
    BillAmount INT,\
    PRIMARY KEY (BillNo, MobileNo))")
curr.execute("CREATE TABLE IF NOT EXISTS database23nov.subbilldetails\
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
curr.execute("CREATE TABLE IF NOT EXISTS database23nov.balancesheet\
    (MobileNo BIGINT,\
    BillDate VARCHAR(20),\
    BillNo BIGINT,\
    Description VARCHAR(100),\
    DebitAmount INT,\
    CreditAmount INT,\
    Balance INT)")
curr.execute("insert ignore into database23nov.productdata values(0,'CASH', 'Payment', '-', '0000', 0, 0, 0, 0)")

conn.commit()
conn.close()





# Color Variables ------------------------------------------------------------------------------------------
colbg="#B8D4BD"
colbglight="#cfe2d3"
colbtn="#3C4ACA"
colhead="#0F9D58"
col1="#DE3163"



#############################################################################################################
root=Tk()
root.title("Local Agro Business Invoice Management System")
root.state('zoomed')
root.geometry("1350x710+0+0")
root.configure(background=colbg)
tw=root.winfo_screenwidth()


# Style Database & Some Extra Variables----------------------------------------------------------------------
imgGod1=PhotoImage(file="img/bahuchar.png")
imgGod2=PhotoImage(file="img/ganesha.png")
imgheart=PhotoImage(file="img/heart.png")

all_style=ttk.Style()
all_style.theme_use("clam")
all_style.configure("Treeview", background=colbg, fieldbackground=colbg)
all_style.configure("TNotebook", background=colbg, bordercolor=colbg, tabposition="n")
all_style.configure("TNotebook.Tab", background=colbglight, foreground=colbtn, bordercolor=colbg, font=("", 10, "bold"), padding=[80,5,80,5])
all_style.map("TNotebook.Tab", padding=[("selected", [80,5,80,5])], background=[("selected", colbg)])

"""
# option={"font": ("", 11, "bold")}
**option as key argument.
"""


# Heading Frame ---------------------------------------------------------------------------------------------
Fheading=Frame(root, bg=colbg)
Fheading.pack(fill=X, padx=10)
Label(Fheading, text="|| Shree Bahuchar Krupa ||", bg=colbg, fg=col1).pack(side=LEFT)
Label(Fheading, text="|| Shreenathji Krupa ||", bg=colbg, fg=col1).pack(side=LEFT, expand=TRUE)
Label(Fheading, text="|| Shri Ganeshay Nam: ||", bg=colbg, fg=col1).pack(side=RIGHT)

Ftitle=Frame(root, bg=colbg)
Ftitle.pack(fill=X, padx=30)
Label(Ftitle, image=imgGod1, bd=0).pack(side=LEFT)
Label(Ftitle, text="Shri Hari Agro Center", font=("", 30, "bold"), bg=colbg, fg=colhead, pady=5).pack(side=LEFT, expand=TRUE)
Label(Ftitle, image=imgGod2, bd=0).pack(side=RIGHT)


# Body Frame --------- Labels & Buttons ---------------------------------------------------------------------
notebook = ttk.Notebook(root)
notebook.pack(fill=BOTH, expand=TRUE)

f1=Frame(notebook, bg=colbg)
f2=Frame(notebook, bg=colbg)
f3=Frame(notebook, bg=colbg)

f1.pack()
f2.pack()
f3.pack()

objf1=allBills(f1)
objf2=customerClass(f2)
objf3=productClass(f3)

notebook.add(f1, text="All Bills")
notebook.add(f2, text="Customer Info")
notebook.add(f3, text="Product Info")


# Footer Frame ----------------------------------------------------------------------------------------------
FFoot=Frame(root, bg=colbg, pady=5)
FFoot.pack(side=BOTTOM, pady=10)
Label(FFoot, text="Build with ", font=("MV Boli", 9, "bold"), fg="#264653", bg=colbg).pack(side=LEFT)
#Label(FFoot, text="\U0001f394", font=("MV Boli", 12, "bold"), fg="red", bg=colbg).pack(side=LEFT)
Label(FFoot, image=imgheart, bd=0).pack(side=LEFT)
link1=Label(FFoot, text=" by Maganbhai (Divyesh Ranpariya, Mo. 9601500840)", font=("MV Boli", 9, "bold"), fg="#264653", bg=colbg)
link1.pack(side=LEFT)
link1.bind("<Button-1>", lambda e: webbrowser.open_new("https://www.facebook.com/divyesh599/"))


root.mainloop()