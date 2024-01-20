import tkinter as tk

def writefile():
    with open("name.txt", "a+") as f:
        f.writelines(name.get())
        print("File has been written !")
        root.update()
root = tk.Tk()

canvas = tk.Canvas(root,width = 800, height = 600)
canvas.pack()

frame = tk.Frame(root, bg = "yellow")
frame.place(relwidth = 1, relheight = 1)


name = tk.StringVar()

entry = tk.Entry(frame, textvariable = name, bg = "orange", font= "arial 18 ", justify = "center", fg = "black")
entry.place( relx = 0.25, rely = 0.05, relwidth = 0.5, relheight = 0.1)
entry.focus_set()

writefile()

root.mainloop()