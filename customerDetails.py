from tkinter import *
from tkinter import ttk





class generateBill:
    def __init__(self, frame):
        self.f1=frame
        lbl1=Label(f1, text="frame 1").pack()


class customerClass:
    def __init__(self, frame):
        self.f2=frame

#--------Frame 1------------
        self.frame1=Frame(self.f2)
        self.frame1.place(x=0, y=0, width=400)

        self.List1=[]
        self.List1.append([Label(self.frame1, text="Manage Customer"), 0])
        self.List1.append([Label(self.frame1, text="Customer ID:"), Label(self.frame1, text="ID lbl")])
        self.List1.append([Label(self.frame1, text="First Name:"), Entry(self.frame1)])
        self.List1.append([Label(self.frame1, text="Middle Name:"), Entry(self.frame1)])
        self.List1.append([Label(self.frame1, text="SurName:"), Entry(self.frame1)])
        self.List1.append([Label(self.frame1, text="Mobile No.:"), Entry(self.frame1)])
        self.List1.append([Label(self.frame1, text="Village:"), Entry(self.frame1)])

        self.List1[0][0].grid(row=0, column=0, columnspan=2, pady=10)
        for i in range(1, 7):
            for j in range(2):
                self.List1[i][j].grid(row=i, column=j, sticky=W, pady=5, padx=10)

#-------Buttons--------------
        self.btnframe=Frame(self.f2)
        self.btnframe.place(x=0, y=500, width=400)
        self.padd_btn=Button(self.btnframe, text="Add", font="arial 10 bold", width=10, bd=5)
        self.padd_btn.grid(row=0, column=0, pady=10)
        self.pupdate_btn=Button(self.btnframe, text="Update", font="arial 10 bold", width=10, bd=5)
        self.pupdate_btn.grid(row=0, column=1, pady=10)
        self.pdelete_btn=Button(self.btnframe, text="Delete", font="arial 10 bold", width=10, bd=5)
        self.pdelete_btn.grid(row=0, column=2, pady=10)
        self.pclear_btn=Button(self.btnframe, text="Clear", font="arial 10 bold", width=10, bd=5)
        self.pclear_btn.grid(row=0, column=4, pady=10)

#--------Frame 2------------

        self.frame2=Frame(self.f2)
        self.frame2.place(x=410, y=0, width=780, height=575)
        
        self.List2=[]
        self.List2.append(Label(self.frame2, text="Search By", font="arial 10 bold"))
        self.List2.append(ttk.Combobox(self.frame2, state="readonly"))
        self.List2[1]["values"]=("Customer ID", "Customer Name", "Mobile No.")
        self.List2.append(Entry(self.frame2, width=50))
        self.List2.append(Button(self.frame2, text="Search", font="arial 10 bold", width=10, bd=5))
        self.List2.append(Button(self.frame2, text="Show All", font="arial 10 bold", width=10, bd=5))
        for i in range(5):
            self.List2[i].grid(row=0, column=i, padx=5)


        #Treeview-------------------------------------------------------------start
        self.tree=ttk.Treeview(self.frame2, columns=("#1", "#2", "#3", "#4"), show="headings", height=22)
        self.tree.place(x=0, y=80, width=765)
        
        self.col_name=["Customer ID",
        "Customer Name",
        "Mobile no.",
        "Village"
        ]
        self.col_size=[40, 210, 80, 80]

        for i in range(4):
            self.tree.column('#'+str(i+1), anchor=CENTER, width=self.col_size[i])
            self.tree.heading('#'+str(i+1), text=self.col_name[i])

        #------Product Items list------
        self.pItemList1=[]

        #Insert Data into Treetable
        for row in self.pItemList1:
            self.tree.insert("", END, values=row)
        
        self.v=Scrollbar(self.frame2, orient="vertical")
        self.v.place(x=760, y=80, height=467)
        self.v.config(command=self.tree.yview)

        self.tree.configure(yscrollcommand=self.v.set)
        #Treeview-------------------------------------------------------------END











class productClass:
    def __init__(self, frame):
        self.f3=frame
















root=Tk()
root.title("શ્રી હરી એગ્રો સેન્ટર - Billing Software")
root.geometry("1360x690+0+0")

heading=Label(root, text="શ્રી હરી એગ્રો સેન્ટર", font=("times new roman", 30, "bold"), relief=GROOVE, fg="#0F9D58", pady=10, bd=5)
heading.pack(fill=X)

iframe=Frame(root)
iframe.place(x=0, y=80, relheight=1)

f1=LabelFrame(root, text="Generate Bill")
f2=LabelFrame(root, text="Customer Details")
f3=LabelFrame(root, text="Product Details")

for frame in (f1, f2, f3):
    frame.place(x=130, y=80, width=1200, height=600)

f1_obj=generateBill(f1)
f2_obj=customerClass(f2)
f3_obj=productClass(f3)

manubtn_color="red"
left_manu1=Button(iframe, text="Generate Bill", borderwidth=0, command=lambda:f1.tkraise(), fg=manubtn_color)
left_manu1.grid(row=0, column=0, ipady=10, ipadx=10, sticky=W)
left_manu2=Button(iframe, text="Customer Details", borderwidth=0, command=lambda:f2.tkraise(), fg=manubtn_color)
left_manu2.grid(row=1, column=0, ipady=10, ipadx=10, sticky=W)
left_manu3=Button(iframe, text="Product Details", borderwidth=0, command=lambda:f3.tkraise(), fg=manubtn_color)
left_manu3.grid(row=2, column=0, ipady=10, ipadx=10, sticky=W)

f2.tkraise()
root.mainloop()