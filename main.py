from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Initialize the main window
root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#000000")


def BMI():
    try:
        h = float(Height.get())
        w = float(Weight.get())
        m = h / 100  # Convert height to meters
        bmi = round(float(w / m**2), 1)
        lable1.config(text=bmi)

        if bmi <= 18.5:
            lable2.config(text="Underweight")
            lable3.config(text="You have lower weight than normal body!")
        elif 18.5 < bmi <= 25:
            lable2.config(text="Normal")
            lable3.config(text="It indicates that you are healthy!")
        elif 25 < bmi <= 30:
            lable2.config(text="Overweight!")
            lable3.config(
                text="It indicates that a person is \n slightly overweight! \n A doctor may advise to lose some \n weight for health reasons!"
            )
        else:
            lable2.config(text="Obese!")
            lable3.config(
                text="Health may be at risk if you do not \n lose weight!"
            )
    except ValueError:
        lable1.config(text="Error")
        lable2.config(text="")
        lable3.config(text="Please enter valid numbers!")


def update_man_image(height_value):
    """Resize the man image dynamically based on the height slider."""
    try:
        # Scale the image proportionally based on height value
        new_height = int(height_value)  # Convert height to an integer
        resized_image = original_man_image.resize((60, max(new_height, 50)))  # Width fixed, height scaled
        updated_image = ImageTk.PhotoImage(resized_image)

        # Update the image in the label
        man_image_label.config(image=updated_image)
        man_image_label.image = updated_image  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error resizing image: {e}")


# Icon
Image_icon = PhotoImage(file="asetes/icon.png")
root.iconphoto(False, Image_icon)

# Top Image
top = PhotoImage(file="asetes/top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=-10)

# Bottom Box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# Two Boxes for Height and Weight
box = PhotoImage(file="asetes/box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale Image
Scale = PhotoImage(file="asetes/scale.png")
Label(root, image=Scale, bg="lightblue").place(x=20, y=310)

# Load Man Image
original_man_image = Image.open("asetes/man.png")  # Ensure this file exists in the same directory

# Man Image Label
man_image_label = Label(root, bg="lightblue")
man_image_label.place(x=120, y=310)  # Initial position of the man image

# Slider for Height
current_value = tk.DoubleVar()


def get_current_value():
    return "{:.2f}".format(current_value.get())


def slider_changed(event):
    height_value = current_value.get()
    Height.set(get_current_value())  # Update height entry
    update_man_image(height_value)  # Adjust man image height


style = ttk.Style()
style.configure("TScale", background="White")
slider = ttk.Scale(
    root,
    from_=0,
    to=220,
    orient="horizontal",
    style="TScale",
    command=slider_changed,
    variable=current_value,
)
slider.place(x=80, y=250)

# Slider for Weight
current_value2 = tk.DoubleVar()


def get_current_value2():
    return "{:.2f}".format(current_value2.get())


def slider_changed2(event):
    Weight.set(get_current_value2())


style2 = ttk.Style()
style2.configure("TScale", background="White")
slider2 = ttk.Scale(
    root,
    from_=0,
    to=200,
    orient="horizontal",
    style="TScale",
    command=slider_changed2,
    variable=current_value2,
)
slider2.place(x=300, y=250)

# Entry Boxes for Height and Weight
Height = StringVar()
Weight = StringVar()

height = Entry(
    root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER
)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(
    root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER
)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# View Report Button
Button(
    root,
    text="View Report",
    width=15,
    height=2,
    font="arial 10 bold",
    bg="#1f6e68",
    fg="white",
    command=BMI,
).place(x=280, y=340)

# Labels for BMI Result and Description
lable1 = Label(root, font="arial 60 bold", bg="lightblue", fg="#fff")
lable1.place(x=125, y=305)

lable2 = Label(root, font="arial 20 bold", bg="lightblue", fg="#3b3a3a")
lable2.place(x=280, y=430)

lable3 = Label(root, font="arial 10", bg="lightblue")
lable3.place(x=200, y=500)

# Main Loop
root.mainloop()
