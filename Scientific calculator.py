from tkinter import *
from math import*
import time
import random

#================Main window ===================

root = Tk()
root.geometry("480x500+0+0")
root.title("Scientific Calculator")





#==============variables =============

text_input= StringVar()
operator = ""

#===========Function==============

def display(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def clear():
    global operator
    operator = "0"
    text_input.set(operator)

def equal():
    global operator
    sump=str(eval(operator))
    text_input.set(sump)
    operator = ""

#=============Display Screem===================


dscreen = Entry(font = ("Arial", 15, 'bold'), bd=30, width=30, fg="steel blue", bg="powder blue", justify="right",textvariable = text_input)
dscreen.grid(columnspan=4)

#=======================================Butttons===============================

b1 =Button(root,padx=8, pady=10,text="7", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(7))
b2 =Button(root,padx=8, pady=10,text="8", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(8))
b3 =Button(root,padx=8, pady=10,text="9", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(9))
b4 =Button(root,padx=8, pady=10,text="+", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("+"))
b5 =Button(root,padx=8, pady=10,text="4", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(4))
b6 =Button(root,padx=8, pady=10,text="5", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(5))
b7 =Button(root,padx=8, pady=10,text="6", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(6))
b8 =Button(root,padx=8, pady=10,text="-", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("-"))
b9 =Button(root,padx=8, pady=10,text="1", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(1))
b0 =Button(root,padx=8, pady=10,text="2", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(2))
b11 =Button(root,padx=8, pady=10,text="3", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(3))
b12 =Button(root,padx=8, pady=10,text="/", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("/"))
b13=Button(root,padx=8, pady=10,text="0", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(0))
b14=Button(root,padx=8, pady=10,text="C", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=clear)
b15=Button(root,padx=8, pady=10,text="=", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=equal)
b16=Button(root,padx=8, pady=10,text="x", width=5, bd =10,bg="powder blue", font=("Arial", 15, ),command=lambda:display("*"))
b17=Button(root,padx=8, pady=10,text=".", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("."))
b18=Button(root,padx=8, pady=10,text="(", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("("))
b19=Button(root,padx=8, pady=10,text=")", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display(")"))
b20=Button(root,padx=8, pady=10,text=")", width=5, bd =10,bg="powder blue", font=("Arial", 15, 'bold'),command=lambda:display("\u221A"))


#======================================Griding the Butttons======================================

b1.grid(column=0, row=1)
b2.grid(column=1, row=1)
b3.grid(column=2, row=1)
b4.grid(column=3, row=1)
b5.grid(column=0, row=2)
b6.grid(column=1, row=2)
b7.grid(column=2, row=2)
b8.grid(column=3, row=2)
b9.grid(column=0, row=3)
b0.grid(column=1, row=3)
b11.grid(column=2, row=3)
b12.grid(column=3, row=3)
b13.grid(column=0, row=4)
b14.grid(column=1, row=4)
b15.grid(column=2, row=4)
b16.grid(column=3, row=4)
b17.grid(column=0, row=5)
b18.grid(column=1, row=5)
b19.grid(column=2, row=5)
b20.grid(column=3, row=5)


root.mainloop()
