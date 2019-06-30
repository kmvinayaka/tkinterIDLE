from  tkinter import *
from tkinter import filedialog
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
root.withdraw()
