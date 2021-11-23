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
        self.selectedC=""
        self.csearch=PhotoImage(file="img/csearch.png")
        self.psearch=PhotoImage(file="img/psearch1.png")

        #--------------Frame1--------------
        self.frame1=Frame(self.f1, bg=bgcol)
        self.frame1.place(x=0, y=0)

        Label(self.frame1, text="બિલ નંબર :", anchor=E, width=15, bg=bgcol).pack(side=LEFT, pady=15)
        self.billno=Label(self.frame1, text=self.cdate.strftime("%y%m%d%H%M"), font="arial 10 bold", bg=bgcol, fg="red", anchor=W, width=20).pack(side=LEFT)
        Label(self.frame1, text="બિલની તારીખ :", bg=bgcol, anchor=E, width=20).pack(side=LEFT)
        self.billdate=Label(self.frame1, text=self.cdate.strftime("%d %b %Y"), font="arial 10 bold", bg=bgcol, fg="red", anchor=W, width=20).pack(side=LEFT)
        Button(self.frame1, text="Refresh Bill", font="arial 10 bold", width=15, bd=2, bg=btncol, fg="white").pack(side=LEFT)

        #--------------Frame2--------------
        self.frame2=Frame(self.f1, bg=bgcol)
        self.frame2.place(x=0, y=70)
        
        Label(self.frame2, text="Search Customer :", bg=bgcol, fg=btncol).grid(row=0, column=0, sticky=W, padx=10)
        
        self.c_id.trace("w", self.callback)
        self.c_entry=Entry(self.frame2, font="arial 10", textvariable=self.c_id, fg="red", width=30, bd=2)
        self.c_entry.grid(row=0, column=1, columnspan=2, sticky=W)
        self.c_entry.bind('<KeyRelease>', self.clistbox_visibility)
        

        #--------------SearchFrame1--------------
        self.sFrame1=Frame(self.f1)
        self.clistbox=Listbox(self.sFrame1, width=70)
        self.clistbox.pack()
        self.clistbox.bind("<Double-1>", self.cListboxOnSelect)
        self.clistbox.bind("<<ListboxSelect>>", self.cListboxSelectedItem)

        self.cAddBtn=Button(self.sFrame1, text="Add", command=self.addCDetails)
        self.cAddBtn.pack(fill=X)


        #--------------Frame3--------------
        self.frame3=Frame(self.f1, bg=bgcol)
        self.frame3.place(x=400, y=70)
        Label(self.frame3, text="નામ :", anchor=E, width=15, bg=bgcol).grid(row=0, column=0)
        self.cLabelname=Label(self.frame3, anchor=W, width=30, font="arial 10 bold", bg=bgcol, fg="red")
        self.cLabelname.grid(row=0, column=1)
        Label(self.frame3, text="મોબાઈલ નંબર :", anchor=E, width=15, bg=bgcol).grid(row=0, column=2)
        self.cLabelMobile=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=bgcol, fg="red")
        self.cLabelMobile.grid(row=0, column=3)
        Label(self.frame3, text="ગામ :", anchor=E, width=5, bg=bgcol).grid(row=0, column=4)
        self.cLabelVillage=Label(self.frame3, anchor=W, width=15, font="arial 10 bold", bg=bgcol, fg="red")
        self.cLabelVillage.grid(row=0, column=5)
        

    def cListboxSelectedItem(self, evt):
        selection=self.clistbox.curselection()
        if selection:
            self.selectedC=self.clistbox.get(selection)[:10]
    
        
    def addCDetails(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        if self.selectedC!="":
            curr.execute("select * from customerlist where CMobileNo="+self.selectedC)
            clist=curr.fetchall()
            if len(clist)!=0:
                self.cLabelname.config(text=clist[0][1]+" "+clist[0][2]+" "+clist[0][3])
                self.cLabelMobile.config(text=clist[0][0])
                self.cLabelVillage.config(text=clist[0][4])
        conn.commit()
        conn.close()
        self.c_entry.delete(0, END)
        self.sFrame1.place_forget()
    
    def cListboxOnSelect(self, evt):
        cs=self.clistbox.curselection()
        if cs:
            self.selectedC=self.clistbox.get(cs)[:10]
        self.addCDetails()

    def callback(self, var, indx, mode):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        x=self.c_entry.get()
        curr.execute("select * from customerlist where CMobileNo LIKE '%"+ x +"%' OR CFirstName LIKE '%"+ x +"%' OR CMiddleName LIKE '%"+ x +"%' OR CLastName LIKE '%"+ x +"%' OR CVillage LIKE '%"+ x +"%'")
        clist=curr.fetchall()
        self.clistbox.delete(0, END)
        if len(clist)!=0:
            for row in clist:
                s=str(row[0])+"    "+row[1]+" "+row[2]+" "+row[3]+"    "+row[4]
                self.clistbox.insert("end", s)

    def clistbox_visibility(self, e):
        if self.c_entry.get() != "":
            self.sFrame1.lift()
            self.sFrame1.place(x=122, y=93)
        else:
            self.sFrame1.place_forget()






















class customerClass:
    def __init__(self, frame):
        self.f2=frame

#--------All Variables------
        self.mobileno=StringVar()
        self.fname=StringVar()
        self.mname=StringVar()
        self.sname=StringVar()
        self.village=StringVar()


#--------Frame 1------------
        self.frame1=Frame(self.f2, bg=bgcol)
        self.frame1.place(x=0, y=0, width=400)

        self.List1=[]
        self.List1.append([Label(self.frame1, text="ગ્રાહકની માહિતી નું સંચાલન", font="arial 10 bold", bg=bgcol, fg="#DE3163"), 0])
        self.List1.append([Label(self.frame1, text="મોબાઈલ નંબર* :", bg=bgcol), Entry(self.frame1, textvariable=self.mobileno)])
        self.List1.append([Label(self.frame1, text="મૂળ નામ :", bg=bgcol), Entry(self.frame1, textvariable=self.fname)])
        self.List1.append([Label(self.frame1, text="પિતાનું નામ :", bg=bgcol), Entry(self.frame1, textvariable=self.mname)])
        self.List1.append([Label(self.frame1, text="અટક :", bg=bgcol), Entry(self.frame1, textvariable=self.sname)])
        self.List1.append([Label(self.frame1, text="ગામ :", bg=bgcol), Entry(self.frame1, textvariable=self.village)])

        self.List1[0][0].grid(row=0, column=0, columnspan=2, pady=10)
        for i in range(1, 6):
            for j in range(2):
                self.List1[i][j].grid(row=i, column=j, sticky=W, pady=5, padx=10)

#-------Buttons--------------
        self.btnframe=Frame(self.f2, bg=bgcol)
        self.btnframe.place(x=0, y=500, width=400)
        self.padd_btn=Button(self.btnframe, text="Add", command=self.add_customer, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.padd_btn.grid(row=0, column=0, pady=10)
        self.pupdate_btn=Button(self.btnframe, text="Update", command=self.update_customer, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pupdate_btn.grid(row=0, column=1, pady=10)
        self.pdelete_btn=Button(self.btnframe, text="Delete", command=self.delete_customer, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pdelete_btn.grid(row=0, column=2, pady=10)
        self.pclear_btn=Button(self.btnframe, text="Clear", command=self.clear_list1, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pclear_btn.grid(row=0, column=4, pady=10)

#--------Frame 2------------

        self.frame2=Frame(self.f2, bg=bgcol)
        self.frame2.place(x=410, y=0, width=780, height=575)
        
        self.List2=[]
        self.List2.append(Label(self.frame2, text="Search By", font="arial 10 bold", bg=bgcol, fg=btncol))
        self.List2.append(ttk.Combobox(self.frame2, state="readonly"))
        self.List2[1]["values"]=("મોબાઈલ નંબર", "મૂળ નામ", "પિતાનું નામ", "અટક")
        self.List2[1].current(0)
        self.sv=StringVar()
        self.sv.trace("w", self.callback)
        self.List2.append(Entry(self.frame2, textvariable=self.sv, width=50))
        self.List2.append(Button(self.frame2, text="Search", command=self.search_items, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5))
        self.List2.append(Button(self.frame2, text="Show All", command=self.show_all_customer, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5))
        for i in range(5):
            self.List2[i].grid(row=0, column=i, padx=5)


        #Treeview-------------------------------------------------------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5"), show="headings", height=22)
        self.tree.place(x=0, y=50, width=765)
        
        self.col_name=["મોબાઈલ નંબર",
                        "મૂળ નામ",
                        "પિતાનું નામ",
                        "અટક",
                        "ગામ"]
        self.col_size=[80, 70, 70, 70, 80]

        for i in range(5):
            self.tree.column('#'+str(i+1), anchor=CENTER, width=self.col_size[i])
            self.tree.heading('#'+str(i+1), text=self.col_name[i])

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=764, y=50, height=482)
        self.v.config(command=self.tree.yview)

        self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=515, width=763)
        self.h.config(command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.v.set, xscrollcommand=self.h.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #Treeview-------------------------------------------------------------END
        
        self.show_all_customer()




    def selectItem(self, a):
        treeItem = self.tree.focus()
        try:
            for i in range(1,6):
                self.List1[i][1].delete(0,END)
                self.List1[i][1].insert(0, self.tree.item(treeItem)['values'][i-1])
        except IndexError as e:
            pass


    def show_all_customer(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        
        curr.execute("select * from customerlist")
        self.clist=curr.fetchall()
        if len(self.clist)!=0:
            self.tree.delete(*self.tree.get_children())
            for row in self.clist:
                self.tree.insert("", END, values=row)
            conn.commit()
        conn.close()


    def add_customer(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        try:
            curr.execute("insert into customerlist values(%s, %s, %s, %s, %s)",
                            (self.mobileno.get(),
                            self.fname.get().capitalize(),
                            self.mname.get().capitalize(),
                            self.sname.get().capitalize(),
                            self.village.get().capitalize())
                        )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
            self.clear_list1()
        self.show_all_customer()

    def update_customer(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        curr.execute("SELECT COUNT(*) FROM customerlist WHERE CMobileNo="+self.mobileno.get())
        x=curr.fetchall()
        if x == ((1,),):
            curr.execute("UPDATE customerlist SET CFirstName='"+self.fname.get().capitalize()
                        +"', CMiddleName='"+self.mname.get().capitalize()
                        +"', CLastName='"+self.sname.get().capitalize()
                        +"', CVillage='"+self.village.get()
                        +"' WHERE CID="+self.cid.get())
        conn.commit()
        conn.close()
        self.clear_list1()
        self.show_all_customer()

    def delete_customer(self):
        if self.cid.get()!="":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="DBHariAgro")
            curr=conn.cursor()
            curr.execute("DELETE FROM customerlist WHERE CMobileNo="+self.mobileno.get())
            conn.commit()
            conn.close()
        self.clear_list1()
        self.show_all_customer()

    def clear_list1(self):
        for i in range(1,6):
            self.List1[i][1].delete(0,END)

    def callback(self, var, indx, mode):
        self.search_items()

    def search_items(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        x = self.List2[1].get()
        if x=="મોબાઈલ નંબર":
            curr.execute("select * from customerlist where CMobileNo LIKE '%"+self.List2[2].get()+"%' OR CFirstName LIKE '%"+self.List2[2].get()+"%' OR CMiddleName LIKE '%"+self.List2[2].get()+"%' OR CLastName LIKE '%"+self.List2[2].get()+"%'")
            self.clist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            if len(self.clist)!=0:
                for row in self.clist:
                    self.tree.insert("", END, values=row)
        elif x=="મૂળ નામ":
            curr.execute("select * from customerlist where CFirstName LIKE '%"+self.List2[2].get()+"%'")
            self.clist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            if len(self.clist)!=0:
                for row in self.clist:
                    self.tree.insert("", END, values=row)
        elif x=="પિતાનું નામ":
            curr.execute("select * from customerlist where CMiddleName LIKE '%"+self.List2[2].get()+"%'")
            self.clist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            if len(self.clist)!=0:
                for row in self.clist:
                    self.tree.insert("", END, values=row)
        elif x=="અટક":
            curr.execute("select * from customerlist where CLastName LIKE '%"+self.List2[2].get()+"%'")
            self.clist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            if len(self.clist)!=0:
                for row in self.clist:
                    self.tree.insert("", END, values=row)













class productClass:
    def __init__(self, frame):
        self.f3=frame

#--------All Variables------
        self.p_id=StringVar()
        self.p_batch_no=StringVar()
        self.company=StringVar()
        self.name=StringVar()
        self.net_content=StringVar()
        self.buy_price=StringVar()
        self.print_price=StringVar()
        self.sell_price=StringVar()

#--------Frame 1------------
        self.frame1=Frame(self.f3, bg=bgcol)
        self.frame1.place(x=0, y=0, width=400)

        self.List1=[]
        self.List1.append([Label(self.frame1, text="પ્રોડક્ટની માહિતી નું સંચાલન", font="arial 10 bold", bg=bgcol, fg="#DE3163"), 0])
        self.List1.append([Label(self.frame1, text="પ્રોડક્ટ નંબર* :", bg=bgcol), Entry(self.frame1, textvariable=self.p_id, fg="red")])
        self.List1.append([Label(self.frame1, text="બેંચ નંબર :", bg=bgcol), Entry(self.frame1, textvariable=self.p_batch_no)])
        self.List1.append([Label(self.frame1, text="ઉત્પાદકનું નામ :", bg=bgcol), Entry(self.frame1, textvariable=self.company)])
        self.List1.append([Label(self.frame1, text="જંતુ. દવાનું નામ/ રા. ખાતરનું નામ :", bg=bgcol), Entry(self.frame1, textvariable=self.name)])
        self.List1.append([Label(self.frame1, text="પેકિંગ (મિલી/ગ્રામ) :", bg=bgcol), Entry(self.frame1, textvariable=self.net_content)])
        self.List1.append([Label(self.frame1, text="પ્રિન્ટેડ કિંમત :", bg=bgcol), Entry(self.frame1, textvariable=self.print_price)])
        self.List1.append([Label(self.frame1, text="વેચાણ કિંમત :", bg=bgcol), Entry(self.frame1, textvariable=self.sell_price)])
        self.List1.append([Label(self.frame1, text="ખરીદ કિંમત :", bg=bgcol), Entry(self.frame1, textvariable=self.buy_price, show="*")])

        self.List1[0][0].grid(row=0, column=0, columnspan=2, pady=10)
        for i in range(1, 9):
            for j in range(2):
                self.List1[i][j].grid(row=i, column=j, sticky=W, pady=5, padx=10)


#-------Buttons--------------
        self.btnframe=Frame(self.f3, bg=bgcol)
        self.btnframe.place(x=0, y=500, width=400)
        self.padd_btn=Button(self.btnframe, text="Add", command=self.add_product,font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.padd_btn.grid(row=0, column=0, pady=10)
        self.pupdate_btn=Button(self.btnframe, text="Update", command=self.update_product, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pupdate_btn.grid(row=0, column=1, pady=10)
        self.pdelete_btn=Button(self.btnframe, text="Delete", command=self.delete_product, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pdelete_btn.grid(row=0, column=2, pady=10)
        self.pclear_btn=Button(self.btnframe, text="Clear", command=self.clear_list1, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5)
        self.pclear_btn.grid(row=0, column=4, pady=10)

#--------Frame 2------------
        self.frame2=Frame(self.f3, bg=bgcol)
        self.frame2.place(x=410, y=0, width=780, height=575)
        
        self.List2=[]
        self.List2.append(Label(self.frame2, text="Search By", font="arial 10 bold", bg=bgcol, fg=btncol))
        self.List2.append(ttk.Combobox(self.frame2, state="readonly"))
        self.List2[1]["values"]=("પ્રોડક્ટ નંબર", "બેંચ નંબર", "ઉત્પાદકનું નામ", "જંતુ. દવાનું નામ")
        self.List2[1].current(0)
        self.List2.append(Entry(self.frame2, width=50))
        self.List2.append(Button(self.frame2, text="Search", command=self.search_items, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5))
        self.List2.append(Button(self.frame2, text="Show All", command=self.show_all_product, font="arial 10 bold", bg=btncol, fg="white", width=10, bd=5))
        for i in range(5):
            self.List2[i].grid(row=0, column=i, padx=5)

        #Treeview-------------------------------------------------------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8"),
                    show="headings", height=22)
        self.tree.place(x=0, y=50, width=765)
        
        self.col_name=["પ્રોડક્ટ નંબર",
                        "બેંચ નંબર",
                        "ઉત્પાદકનું નામ",
                        "જંતુ. દવાનું નામ/ રા. ખાતરનું નામ",
                        "પેકિંગ (મિલી/ગ્રામ)",
                        "પ્રિન્ટેડ કિંમત",
                        "વેચાણ કિંમત",
                        "ખરીદ કિંમત"]

        self.col_size=[70, 70, 150, 220, 100, 75, 75, 75]

        for i in range(8):
            self.tree.column('#'+str(i+1), anchor=CENTER, width=self.col_size[i])
            self.tree.heading('#'+str(i+1), text=self.col_name[i])

        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=764, y=50, height=482)
        self.v.config(command=self.tree.yview)

        self.h=Scrollbar(self.frame2, orient="horizontal")
        self.h.place(x=0, y=515, width=763)
        self.h.config(command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.v.set, xscrollcommand=self.h.set)

        self.tree.bind('<<TreeviewSelect>>', self.selectItem)
        #Treeview-------------------------------------------------------------END
        
        self.show_all_product()


    def selectItem(self, a):
        treeItem = self.tree.focus()
        try:
            for i in range(1,9):
                self.List1[i][1].delete(0,END)
                self.List1[i][1].insert(0, self.tree.item(treeItem)['values'][i-1])
        except IndexError as e:
            pass

        
    def add_product(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        try:
            curr.execute("insert into productlist values(%s, %s, %s, %s, %s, %s, %s, %s)",
                            (self.p_id.get(),
                            self.p_batch_no.get(),
                            self.company.get().capitalize(),
                            self.name.get().capitalize(),
                            self.net_content.get(),
                            self.print_price.get(),
                            self.sell_price.get(),
                            self.buy_price.get())
                        )
        except pymysql.err.Error as e:
            pass
        finally:
            conn.commit()
            conn.close()
            self.clear_list1()
        self.show_all_product()
        

    def update_product(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        curr.execute("SELECT COUNT(*) FROM productlist WHERE productlist.PID="+self.p_id.get())
        x=curr.fetchall()
        if x == ((1,),):
            curr.execute("UPDATE productlist SET PBatchNo="+self.p_batch_no.get()
                        +", CompanyName='"+self.company.get().capitalize()
                        +"', PName='"+self.name.get().capitalize()
                        +"', PNetContent="+self.net_content.get()
                        +", PPrintedPrice="+self.print_price.get()
                        +", PSellingPrice="+self.sell_price.get()
                        +", PBuyingPrice="+self.buy_price.get()
                        +" WHERE PID="+self.p_id.get())
        conn.commit()
        conn.close()
        self.clear_list1()
        self.show_all_product()


    def delete_product(self):
        if self.p_id.get()!="":
            conn=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="DBHariAgro")
            curr=conn.cursor()
            curr.execute("DELETE FROM productlist WHERE PID="+self.p_id.get())
            conn.commit()
            conn.close()
        self.clear_list1()
        self.show_all_product()


    def clear_list1(self):
        for i in range(1,9):
            self.List1[i][1].delete(0,END)


    def show_all_product(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        curr.execute("select * from productlist")
        self.plist=curr.fetchall()
        self.tree.delete(*self.tree.get_children())
        for row in self.plist:
            self.tree.insert("", END, values=row)
        conn.commit()
        conn.close()


    def search_items(self):
        conn=pymysql.connect(host="localhost",
                            user="root",
                            password="",
                            database="DBHariAgro")
        curr=conn.cursor()
        x = self.List2[1].get()
        if x=="પ્રોડક્ટ નંબર":
            curr.execute("select * from productlist where PID="+self.List2[2].get())
            self.plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in self.plist:
                self.tree.insert("", END, values=row)
        elif x=="બેંચ નંબર":
            curr.execute("select * from productlist where PBatchNo LIKE '%"+self.List2[2].get()+"%'")
            self.plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in self.plist:
                self.tree.insert("", END, values=row)
        elif x=="ઉત્પાદકનું નામ":
            curr.execute("select * from productlist where CompanyName LIKE '%"+self.List2[2].get()+"%'")
            self.plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in self.plist:
                self.tree.insert("", END, values=row)
        elif x=="જંતુ. દવાનું નામ":
            curr.execute("select * from productlist where PName LIKE '%"+self.List2[2].get()+"%'")
            self.plist=curr.fetchall()
            self.tree.delete(*self.tree.get_children())
            for row in self.plist:
                self.tree.insert("", END, values=row)
        conn.commit()
        conn.close()






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