from tkinter import *
import datetime



class Bill_App:
    bg_color="#B8D4BD"
    fg_color="#3C4ACA"
    cdate=datetime.datetime.now()

    def __init__(self, root):
        self.root=root
        
        title=Label(self.root, text="શ્રી હરી એગ્રો સેન્ટર", relief=GROOVE, bg=Bill_App.bg_color, fg="#0F9D58", font=("times new roman", 30, "bold"), pady=10, bd=5).pack(fill=X)

        #------------Customer Detail Frame-------------
        F1=LabelFrame(self.root, text="ગ્રાહકની માહિતી", font=("times new roman", 12, "bold"), bg=Bill_App.bg_color, fg=Bill_App.fg_color)
        F1.place(x=0, y=80, relwidth=1)

        cnumber_lbl=Label(F1, text="ગ્રાહક નંબર :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color).grid(row=0, column=0, pady=5, padx=20)
        cnumber_txt=Entry(F1, font="arial 10", width=10, bd=5).grid(row=0, column=1)

        cname_lbl=Label(F1, text="ગ્રાહકનું નામ :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color).grid(row=0, column=2, padx=20)
        cname_txt=Entry(F1, font="arial 10", width=60, bd=5).grid(row=0, column=3)

        cphone_lbl=Label(F1, text="મોબાઈલ નંબર :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color).grid(row=0, column=4, padx=20)
        cphone_txt=Entry(F1, font="arial 10", width=10, bd=5).grid(row=0, column=5)

        cvillage_lbl=Label(F1, text="ગામ :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color).grid(row=0, column=6, padx=20)
        cvillage_txt=Entry(F1, font="arial 10", width=15, bd=5).grid(row=0, column=7)

        csearch_btn=Button(F1, text="Search", font="arial 10 bold", width=10, bd=5, bg=Bill_App.fg_color, fg="white").grid(row=0, column=8, padx=10, pady=10)

        #------------Bill Detail Frame-------------
        F2=LabelFrame(self.root, text="બિલની માહિતી", font=("times new roman", 12, "bold"), bg=Bill_App.bg_color, fg=Bill_App.fg_color)
        F2.place(x=0, y=170, width=350, height=169)

        bnumber_lbl=Label(F2, text="બિલ નંબર :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color, anchor=E, width=20).grid(row=0,column=0, padx=(20, 0), pady=10, ipady=10)
        bnumber_txt=Label(F2, text="005524", font="arial 10 bold", bg=Bill_App.bg_color, fg="red", anchor=W, width=20).grid(row=0, column=1, ipady=10)
        bdate_lbl=Label(F2, text="બિલની તારીખ :", font=("times new roman", 10, "bold"), bg=Bill_App.bg_color, anchor=E, width=20).grid(row=1, column=0, padx=(20,0), ipady=10)
        bdate_txt=Label(F2, text=Bill_App.cdate.strftime("%d %b %Y  %I:%M %p"), font="arial 10 bold", bg=Bill_App.bg_color, fg="red", anchor=W, width=20).grid(row=1, column=1, ipady=10)

        #----------------Bill table------------------------
        F3=LabelFrame(self.root, bg=Bill_App.bg_color)
        F3.place(x=350, y=176, width=1000)
        
        table = []

        table_col_name = ["ક્રમ", "જંતુ. દવાનું નામ / રા. ખાતરનું નામ બ્રાન્ડ", "ઉત્પાદકનું નામ", "બેંચ નંબર", "પેકિંગ (લી. / કિ.)", "વેચાણ ભાવ", "વેચેલ જથ્થો", "કુલ રકમ (₹.)"]
        table_col_len = [5, 46, 18, 13, 22, 13, 15, 16]
        
        table_row = []
        for i in range(7):
            table_row.append(Label(F3, text=table_col_name[i], font=("times new roman", 10, "bold"), width=table_col_len[i], borderwidth=1, relief="ridge", pady=5).grid(row=0, column=i))
        table.append(table_row)

        for i in range(1,7): #row
            table_row = []
            for j in range(7): #column
                if j==0:
                    table_row.append(Label(F3, text=str(i), font="arial 10", width=table_col_len[0]).grid(row=i, column=0))
                else:
                    table_row.append(Entry(F3, font="arial 10", width=table_col_len[j]).grid(row=i, column=j))
            table.append(table_row)

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=None)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_command(label="Save as...", command=None)
filemenu.add_command(label="Close", command=None)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=None)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=None)
editmenu.add_command(label="Copy", command=None)
editmenu.add_command(label="Paste", command=None)
editmenu.add_command(label="Delete", command=None)
editmenu.add_command(label="Select All", command=None)

menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=None)
helpmenu.add_command(label="About...", command=None)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

root.geometry("1360x690+0+0")
root.configure(background=Bill_App.bg_color)
root.title("Billing Software - શ્રી હરી એગ્રો સેન્ટર")
obj = Bill_App(root)
root.mainloop()