# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:43:52 2020

@author: yash gagneja
"""

from tkinter import *

window = Tk()
window.title("Welcome to tkinter")
window.geometry("540x100")
def from_kg2():
     pound=float(e2_value.get())*2.20462
     pound=str(str(pound)+'')
     t1.delete("1.0", END)
     t1.insert(END,pound)
def from_kg3():
     ounce=float(e2_value.get())*35.274
     ounce=str(str(ounce)+' ')
     t1.delete("1.0", END)
     t1.insert(END,ounce)

    
    
def from_kg1():
    gram=float(e2_value.get())*1000
    gram=str(str(gram)+'')
    t1.delete("1.0", END)
    t1.insert(END,gram)
    
  
e1=Label(window,text="")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e2.grid(row=0,column=1)

b1=Button(window,text="Convert into gram",command=from_kg1, fg='black', bg='red')
b1.grid(row=0,column=2)
b1=Button(window,text="Convert into pound",command=from_kg2, fg='black', bg='red')
b1.grid(row=1,column=2)
b1=Button(window,text="Convert into ounce",command=from_kg3, fg='black', bg='red')
b1.grid(row=2,column=2)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

window.mainloop()
