from tkinter import*
root = Tk()

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
dsw = str(int(sw / 2))
dsh = str(int(sh / 2))
print(dsw)
print(dsh)

label = Label(text='text', font=('Arial','30'), fg='black', bg='white')
label.master.overrideredirect(True)
label.master.geometry("+"+dsw+"+"+dsh)
label.master.lift()
label.master.wm_attributes("-topmost", True)
label.master.wm_attributes("-disabled", True)
label.master.wm_attributes("-transparentcolor", "white")
label.pack()

label.mainloop()