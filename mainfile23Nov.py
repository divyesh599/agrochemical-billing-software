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
conn.commit()
conn.close()