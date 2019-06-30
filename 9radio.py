import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    "Python",
    "Perl",
    "Java",
    "C+",
    "C"
]

val = range(len(languages))

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         padx = 20).pack()

for val, language in zip(val,languages):
    print("val",val,"language",language)
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)


root.mainloop()
