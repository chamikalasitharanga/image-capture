import cv2
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, Canvas
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

# Contrast, border, and thumbnail

root = Tk()
root.title("Photo Lab")
root.geometry("650x670")

# Create functions
img_path = ""
current_img = ""

def capture_image():
    global img_path, current_img
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("captured_image.png", frame)
        img_path = "captured_image.png"
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        current_img = img.filter(ImageFilter.BoxBlur(0))
        img1 = ImageTk.PhotoImage(current_img)
        canvas2.create_image(300, 210, image=img1)
        canvas2.image = img1
    cap.release()
    cv2.destroyAllWindows()

def selected():
    global img_path, current_img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    current_img = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1

def blur(event):                                
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    current_img = img.filter(ImageFilter.BoxBlur(v1.get()))
    img1 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image = img1

def brightness(event):                            
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    enhancer = ImageEnhance.Brightness(img)
    current_img = enhancer.enhance(v2.get())
    img2 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img2)
    canvas2.image = img2

def contrast(event):
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    enhancer = ImageEnhance.Contrast(img)
    current_img = enhancer.enhance(v3.get())
    img3 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img3)
    canvas2.image = img3

def rotate_image(event):
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    current_img = img.rotate(int(rotate_combo.get()))
    img4 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img4)
    canvas2.image = img4

def flip_image(event):
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    if flip_combo.get() == "FLIP LEFT TO RIGHT":
        current_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_combo.get() == "FLIP TOP TO BOTTOM":
        current_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    img5 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img5)
    canvas2.image = img5

def image_border(event):
    global img_path, current_img
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    border_size = int(border_combo.get())
    current_img = ImageOps.expand(img, border=border_size, fill=95)
    img6 = ImageTk.PhotoImage(current_img)
    canvas2.create_image(300, 210, image=img6)
    canvas2.image = img6

def save():
    global current_img
    file = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("All Files", "*.*"), ("PNG Files", "*.png"), ("JPG Files", "*.jpg")])
    if file:
        ext = file.split(".")[-1].lower()
        if ext in ["jpg", "jpeg"] and current_img.mode == "RGBA":
            current_img = current_img.convert("RGB")
        current_img.save(file)

# Create labels, scales, and comboboxes 

blurr = Label(root, text="Blur", font=("Arial 17 bold"), width=9, anchor='e')
blurr.place(x=1, y=8)
v1 = IntVar()
Scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur)
Scale1.place(x=150, y=15)

bright = Label(root, text="Brightness", font=("Arial 17 bold"))
bright.place(x=15, y=50)
v2 = IntVar()
Scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness)
Scale2.place(x=150, y=55)

contrastt = Label(root, text="Contrast", font=("Arial 17 bold"))
contrastt.place(x=15, y=92)
v3 = IntVar()
Scale3 = ttk.Scale(root, from_=0, to=10, variable=v3, orient=HORIZONTAL, command=contrast)
Scale3.place(x=150, y=100)

rotate = Label(root, text="Rotate", font=("Arial 17 bold"))
rotate.place(x=370, y=8)
values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=("Arial 10 bold"))
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

flip = Label(root, text="Flip", font=("Arial 17 bold"))
flip.place(x=370, y=50)
values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=("Arial 10 bold"))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)

border = Label(root, text="Add border", font=("Arial 17 bold"))
border.place(x=360, y=92)
values2 = [i for i in range(0 , 10)]
border_combo = ttk.Combobox(root, values=values2, font=("Arial 10 bold"))
border_combo.place(x=460, y=99)
border_combo.bind("<<ComboboxSelected>>", image_border)

# Create canvas to display image

canvas2 = Canvas(root, width="600", height="420", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

# Create buttons

btn_capture = Button(root, text="Capture Image", width=12, bg='black', fg='gold', font=('Arial 15 bold'), relief=GROOVE, command=capture_image)
btn_capture.place(x=15, y=595)

btn_select = Button(root, text="Select Image", width=12, bg='black', fg='gold', font=('Arial 15 bold'), relief=GROOVE, command=selected)
btn_select.place(x=170, y=595)

btn_save = Button(root, text="Save", width=12, bg='black', fg='gold', font=('Arial 15 bold'), relief=GROOVE, command=save)
btn_save.place(x=325, y=595)

btn_exit = Button(root, text="Exit", width=12, bg='black', fg='gold', font=('Arial 15 bold'), relief=GROOVE, command=root.destroy)
btn_exit.place(x=480, y=595)

root.mainloop()
