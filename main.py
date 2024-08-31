from tkinter import *
equation=
expression = ""
def press(num):
          global expression
          expression = expression + str(num)
          equation.set(expression)
def equalpress():
          try:
                    global expression
                    total = str(eval(expression))
                    equation.set(total)
                    expression = ""
          except:
                    equation.set(" error ")
                    expression = ""
def clear():
          global expression
          expression = ""
          equation.set("")
          gui = Tk()
          gui.configure(background="black")
          gui.title("Simple Calculator")
          gui.geometry("270x150")
          equation = StringVar()
          expression_field = Entry(gui, textvariable=equation)
          expression_field.grid(columnspan=4, ipadx=70)
          button1 = Button(gui, text=' 1 ', fg='black', bg='yellow',command=lambda: press(1), height=1, width=7)
          button1.grid(row=2, column=0)
          button2 = Button(gui, text=' 2 ', fg='black', bg='yellow',command=lambda: press(2), height=1, width=7)
          button2.grid(row=2, column=1)
          button3 = Button(gui, text=' 3 ', fg='black', bg='yellow',command=lambda: press(3), height=1, width=7)
          button3.grid(row=2, column=2)
          button4 = Button(gui, text=' 4 ', fg='black', bg='yellow',command=lambda: press(4), height=1, width=7)
          button4.grid(row=3, column=0)
          button5 = Button(gui, text=' 5 ', fg='black', bg='yellow',command=lambda: press(5), height=1, width=7)
          button5.grid(row=3, column=1)
          button6 = Button(gui, text=' 6 ', fg='black', bg='yellow',command=lambda: press(6), height=1, width=7)
          button6.grid(row=3, column=2)
          button7 = Button(gui, text=' 7 ', fg='black', bg='yellow',command=lambda: press(7), height=1, width=7)
          button7.grid(row=4, column=0)

          
button8 = Button(gui, text=' 8 ', fg='black', bg='yellow',command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(gui, text=' 9 ', fg='black', bg='yellow',command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(gui, text=' 0 ', fg='black', bg='yellow',command=lambda: press(0), height=1, width=7)

button0.grid(row=5, column=0)

          plus = Button(gui, text=' + ', fg='black', bg='yellow',command=lambda: press("+"), height=1, width=7)

          plus.grid(row=2, column=3)

          minus = Button(gui, text=' - ', fg='black', bg='yellow',command=lambda: press("-"), height=1, width=7)

          minus.grid(row=3, column=3)

          multiply = Button(gui, text=' X ', fg='black', bg='yellow',command=lambda: press("*"), height=1, width=7)

          multiply.grid(row=4, column=3)

          divide = Button(gui, text=' / ', fg='black', bg='yellow',command=lambda: press("/"), height=1, width=7)

          divide.grid(row=5, column=3)

          equal = Button(gui, text=' = ', fg='black', bg='yellow',command=equalpress, height=1, width=7)

          equal.grid(row=5, column=2)

          clear = Button(gui, text='Clear', fg='black', bg='yellow',command=clear, height=1, width=7)

          clear.grid(row=5, column='1')

          Decimal= Button(gui, text='.', fg='black', bg='yellow',command=lambda: press('.'), height=1, width=7)

          Decimal.grid(row=6, column=0)

          gui.mainloop()

   


2.	Create a dropdown list to select a city from the given list of cities
from tkinter import * 
 
root = Tk() 
 
root.geometry( "200x200" ) 
 
def show():  label.config( text = clicked.get() ) 
 
options = [  "Ahmedabad",  "Rajkot",  "Delhi",  "Jaipur",  "Mumbai",  "Allahabad",  "Hyderabad" ] 
 
clicked = StringVar() 
 
clicked.set( "Cities" ) 
 
drop = OptionMenu( root , clicked , *options ) 
drop.pack() 
 
button = Button( root , text = "click Me" , command = show ).pack() 
 
label = Label( root , text = " " ) 
label.pack() 
 
root.mainloop() 

 
3.	Write a tkinter code to place an image/picture in the window.

from tkinter import * 
from PIL import ImageTk, Image 
 
win = Tk() 
 
win.geometry("666x1000") 
 
frame = Frame(win, width=666, height=1000) 
frame.pack() 
frame.place(anchor='center', relx=0.5, rely=0.5) 
 
img = ImageTk.PhotoImage(Image.open("Scar.jpg")) 
 
label = Label(frame, image = img) 
label.pack() 
 
win.mainloop()
 





4.	Create Registration window.

import tkinter as tk
 
def register():     name = name_entry.get()     email = email_entry.get()     password = password_entry.get() 
 
    print("Name:", name)     print("Email:", email)     print("Password:", password) 
 
root = tk.Tk() root.title("Registration Form") 
 
name_label = tk.Label(root, text="Name:") name_label.pack() name_entry = tk.Entry(root) name_entry.pack() 
 
email_label = tk.Label(root, text="Email:") email_label.pack() email_entry = tk.Entry(root) email_entry.pack() 
 
password_label = tk.Label(root, text="Password:") password_label.pack() password_entry = tk.Entry(root, show="*") password_entry.pack() 
 
register_button = tk.Button(root, text="Register", command=register) register_button.pack() 
 
root.mainloop()

 
 
