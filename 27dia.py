from tkinter import *
from tkinter import messagebox

def answer():
    messagebox.showerror("Answer", "Sorry, no answer available")

def callback():
    if messagebox.askyesno('Verify', 'Really quit?'):
        messagebox.showwarning('Yes', 'Not yet implemented')
    else:
        messagebox.showwarning('No', 'Quit has been cancelled')
        
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()
