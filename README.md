# Billing Management software (shree-hari-agro.exe)
Billing and selling management software for Agricultural chemical products. Python based with SQL database desktop software. Currently working on this project. Date: 1 Jan 2022

---------------------------------------------------------------------------------------------
Revised or Learned Questions:

* Difference between Primary key and Unique key?
* SQL Composite Key?
* Tracing Tkinter textvariable in Python?
* TRUNCATE TABLE tempsubbill sql query..


Date: 7 Jan 2022
* Working on product class, delete features.
* Modifying UI of main app view.
* trying to change UI from .tkraise() to Notebook widget.

---------------------------------------------------------------------------------------------

# For my rough use

Product-Details-table
- productID (PK)
- product_batch_no
- product_company
- product_name
- product_net_content
- product_printed_price
- product_buy_price**
- product_sell_price

* function properties
-add new product
-modify product
-delete product
-view all product


- Manufacturer
- Brand Name
- Technical Name
- productID (PK)
- p_batch_no
- p_technichal (Technical Name)
- p_company (Manufacturer)
- product_brand_name (Brand Name)
- product_net_content
- product_printed_price
- product_buy_price**
- product_sell_price

.................................................

Customer-Details-table

- customerID (PK)
- customer_name
- customer_mob_no
- customer_village

.................................................

Bill-Details-table

- bill_number
- customerID
- productID
- product_quantity
- bill_date
- bill_status

.................................................

C -----(M)----B-----(N)----- P (we can no reduce table.)

update color = 49A0AE




































