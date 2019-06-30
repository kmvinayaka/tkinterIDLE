import tkinter as tk
master = tk.Tk()
whatever_you_do = "Life's most persistent and urgent question is, What are you doing for others? .\n(Martin Luther)"
msg = tk.Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack()
tk.mainloop()
