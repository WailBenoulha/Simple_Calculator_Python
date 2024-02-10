from tkinter import *

# Define the graphical pannel

root = Tk()
root.title("Calculator")
e = Entry(root, width=30, borderwidth=12)
e.grid(row=0, column=0,columnspan=3, padx=20, pady=10)

# Define the Functions

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def button_clear():
    e.delete(0, END) 

def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = float(first_number)  
    e.delete(0,END) 

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = float(first_number)  
    e.delete(0,END) 

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplying"
    f_num = float(first_number)  
    e.delete(0,END) 

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "dividing"
    f_num = float(first_number)  
    e.delete(0,END) 

def button_equal():
    if math == 'addition':
        second_number = e.get()
        e.delete(0,END)
        e.insert(0, f_num + float(second_number)) 
    if math == 'subtraction':
        second_number = e.get()
        e.delete(0,END)
        e.insert(0, f_num - float(second_number))   
    if math == 'multiplying':
        second_number = e.get()
        e.delete(0,END)
        e.insert(0, f_num * float(second_number))   
    if math == 'dividing':
        second_number = e.get()
        e.delete(0,END)
        e.insert(0, f_num / float(second_number))            

# Define the Buttons

bcomma = Button(root, text=",", command=lambda: button_click('.'), width=10, padx=5, pady=10).grid(row=1,column=0)
bback = Button(root, text="clear", command=button_clear, width=10, padx=5, pady=10).grid(row=1,column=1)
b0 = Button(root, text="0",command=lambda: button_click(0), width=10, padx=5, pady=10).grid(row=1, column=2)

b1 = Button(root, text="1",command=lambda: button_click(1), width=10, padx=5, pady=10).grid(row=2, column=0)
b2 = Button(root, text="2",command=lambda: button_click(2), width=10, padx=5, pady=10).grid(row=2, column=1)
b3 = Button(root, text="3",command=lambda: button_click(3), width=10, padx=5, pady=10).grid(row=2, column=2)

b4 = Button(root, text="4",command=lambda: button_click(4), width=10, padx=5, pady=10).grid(row=3, column=0)
b5 = Button(root, text="5",command=lambda: button_click(5), width=10, padx=5, pady=10).grid(row=3, column=1)
b6 = Button(root, text="6",command=lambda: button_click(6), width=10, padx=5, pady=10).grid(row=3, column=2)

b7 = Button(root, text="7",command=lambda: button_click(7), width=10, padx=5, pady=10).grid(row=4, column=0)
b8 = Button(root, text="8",command=lambda: button_click(8), width=10, padx=5, pady=10).grid(row=4, column=1)
b9 = Button(root, text="9",command=lambda: button_click(9), width=10, padx=5, pady=10).grid(row=4, column=2)

badd = Button(root, text="+",command=button_add, width=10, padx=5, pady=10).grid(row=5, column=0)
bminus = Button(root, text="-",command=button_subtract, width=10, padx=5, pady=10).grid(row=5, column=1)
btime = Button(root, text="x",command=button_multiply, width=10, padx=5, pady=10).grid(row=5, column=2)

bdive = Button(root, text="/",command=button_divide, width=10, padx=5, pady=10).grid(row=6, column=0)
bequal = Button(root, text="=",command=button_equal, width=23, padx=5, pady=10, bg="green").grid(row=6, column=1, columnspan=2)
root.mainloop()