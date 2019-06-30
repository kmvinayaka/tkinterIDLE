import tkinter as tk

counter = 0 
def counter_label(label,a=0):
  print(a)
  global counter
  
  def count():
    global counter
    
    counter += 1
    label.config(text=str(counter))
    label.after(10, count)
  if a == 1:
    global counter
    counter = 0
    count()
  else:
    count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button1 = tk.Button(root, text='pause', width=25, command=counter_label(label,1))

button.pack()
button1.pack()
root.mainloop()
