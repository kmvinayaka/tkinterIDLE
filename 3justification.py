import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="image2.png")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w = tk.Label(root, 
             compound = tk.LEFT,
             text=explanation, 
             image=logo).pack(side="right")

root.mainloop()
