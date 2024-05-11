import tkinter as tk
from tkinter import ttk

root = tk.Tk()
width,height = 200,100

screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

left=int(screen_width/2-width/2)
top=int(screen_height/2-height/2)

root.geometry(f'{width}x{height}+{left}+{top}')

def greet_func():
    greet_lbl.configure(text='Hello, '+name_entry.get()+'. How are you?')


name_lbl = ttk.Label(root,text='Enter your name: ')
name_lbl.pack()

name_entry = ttk.Entry(root)
name_entry.pack()

greet_lbl = ttk.Label(root)
greet_lbl.pack()

button = ttk.Button(root,text='Greet!',command=greet_func)
button.pack()

root.mainloop()