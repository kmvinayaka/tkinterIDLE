import qrcode
from tkinter import *
from tkinter import messagebox
import json
import time
from PIL import ImageTk, Image
import os
ws = Tk()
ws.title('QR Code Generator')
ws.geometry('400x200')
ws.config(bg='#2a7a9c')



frame = Frame(ws, bg='#4a7a8c')
frame.pack(expand=True)

Label(
    frame,
    text='Name',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=0, column=0, sticky='w')

Label(
    frame,
    text='Emp ID',
    font = ('Times', 18),
    bg='#4a7a8c'
    ).grid(row=1, column=0, sticky='w')

name = Entry(frame)
name.grid(row=0, column=1)

emp = Entry(frame)
emp.grid(row=1, column=1)

Label(
    frame,
    text='Save as',
    font = ('Times', 18),
    bg='#4a7a8c',
).grid(row=2, column=0, sticky='w')

save_name = Entry(frame)
save_name.grid(row=2, column=1)



def generate():
    img = qrcode.make(json.dumps({"name":name.get(),"emp_id":emp.get(),"DOE":time.time()}))
    type(img)
    img.save(f'{save_name.get()}.png')
    show()


def show():
    global panel
    print(f"inside Image Show {os.path.join(os.getcwd(),save_name.get())}.png")
    img = ImageTk.PhotoImage(Image.open(f'{os.path.join(os.getcwd(),save_name.get())}.png'))
    panel = Label(ws, image = img)
    panel.image = img
    panel.place(x = 10, y = 60)


btn = Button(
    ws, 
    text='Generate QR code',
    command=generate
    )
btn.pack()


# btn1 = Button(
#     ws,
#     text='Show QR Code',
#     command=show
#     )
# btn1.pack()

ws.mainloop()