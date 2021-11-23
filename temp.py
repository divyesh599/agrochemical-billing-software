'''from tkinter import *

def callback(sv):
    print(sv.get())

root = Tk()
sv = StringVar()
#sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
sv.trace_add("write", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()'''


from tkinter import * 
  
  
root = Tk()
  
my_var = StringVar()
  
# defining the callback function (observer)
def my_callback(var, indx, mode):
    print("Traced variable {}".format(my_var.get()))

# registering the observer
my_var.trace_add('write', my_callback)

Label(root, textvariable = my_var).pack(padx = 5, pady = 5)
  
Entry(root, textvariable = my_var).pack(padx = 5, pady = 5)
  
root.mainloop()