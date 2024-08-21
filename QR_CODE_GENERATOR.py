from tkinter import *
import pyqrcode
from PIL import ImageTk, Image

root = Tk()
root.title("QR Code Generator")

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(300,550,window=image_label)



canvas =  Canvas(root, width=700, height=800)
canvas.pack()
app_label = Label(root, text="QR CODE GENERATOR",fg='blue',font=("Arial", 30))
canvas.create_window(380,100,window=app_label)

name_label = Label(root,text="Link Name")
link_label = Label(root,text="Link")
canvas.create_window(320,200,window=name_label)
canvas.create_window(320,300,window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)

canvas.create_window(320,170,window=name_entry)
canvas.create_window(320,270,window=link_entry)

button = Button(text="Generate QR Code",command=generate)
canvas.create_window(320,330, window=button)

root.mainloop()