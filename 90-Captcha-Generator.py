from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

image = ImageCaptcha(
    fonts=[
        "D:/Github pushed/100-Python-programs-Basic-to-Advanced/Caveat-VariableFont_wght.ttf"
    ]
)

random = str(randint(100000, 999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random, "out.png")

def verify():
    global random
    x = t1.get("1.0", END).strip()
    if x == random:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global random
    random = str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random, "out.png")
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.image = photo  

root = Tk()
photo = PhotoImage(file="out.png")

l1 = Label(root, image=photo, height=100, width=200)
t1 = Text(root, height=1, width=10)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()
