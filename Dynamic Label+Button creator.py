# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 11:12:07 2022

@author: ishar
"""

from tkinter import *
root=Tk()
root.geometry("900x900")
root.title("Classes")
root.configure(bg="lightblue")



class Create_Elements:
    def __init__(self):
        print("This is Create_Elements class")
        
    def create_new_element(self):
        label=Label(root, text="A new label has been created using this class", fg="red", bg="lavender")
        label.pack()
        btn=Button(root, text="A new button has been created", command=self.message, fg="red",bg="lavender")
        btn.pack(padx=20, pady=10)
        
    def message(self):
        messagebox.showinfo("show info", "You clicked the button created using the class")
       
obj_of_element=Create_Elements()
btn_main=Button(root, text="Click to create a new label and button element", fg="red", bg="lavender",command=obj_of_element.create_new_element())
btn_main.pack(padx=20, pady=10)


root.mainloop()