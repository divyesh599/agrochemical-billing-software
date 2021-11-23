from tkinter import *
from tkinter import ttk
import pymysql
import datetime







conn=pymysql.connect(host="localhost",
                    user="root",
                    password="")
curr=conn.cursor()
curr.execute("CREATE DATABASE IF NOT EXISTS Database23Nov")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.customerData\
    (MobileNo BIGINT,\
    FName VARCHAR(20),\
    MName VARCHAR(20),\
    LName VARCHAR(20),\
    City VARCHAR(20),\
    Balance INT,\
    PRIMARY KEY (MobileNo))")
curr.execute("CREATE TABLE IF NOT EXISTS Database23Nov.productData\
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

conn.commit()
conn.close()