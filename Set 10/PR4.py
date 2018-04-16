import tkinter as tk
def write_slogan():
    print("This is sample Message.")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="blue",
                   command=quit)
button.pack(side=tk.BOTTOM)
slogan = tk.Button(frame,
                   text="Print Message",
                   command=write_slogan)
slogan.pack(side=tk.TOP)

root.mainloop()
