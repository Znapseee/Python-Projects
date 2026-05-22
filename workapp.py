import tkinter as tk
from tkinter import ttk
from math import pi

def calculate():
    try:
        figure = shape_var.get().lower()

        radius = float(radius_entry.get())
        height = float(height_entry.get())
        constant = float(constant_entry.get())
        overflow = float(overflow_entry.get())

        if figure == "cylinder":
            volume = pi * (radius ** 2) * height
            centroid = height / 2

        elif figure == "cone":
            volume = (1/3) * pi * (radius ** 2) * height
            centroid = height / 4

        elif figure == "sphere":
            volume = (4/3) * pi * (radius ** 3)
            centroid = (3/8) * radius

        else:
            result_label.config(text="Invalid shape")
            return

        work = constant * volume * (centroid + overflow)

        result_label.config(
            text=f"Pumping Work = {work:.2f}"
        )

    except ValueError:
        result_label.config(
            text="Please enter valid numbers."
        )

root = tk.Tk()
root.title("Tank Pumping Work Calculator")
root.geometry("400x400")

shape_var = tk.StringVar()

ttk.Label(root, text="Tank Shape").pack()
shape_menu = ttk.Combobox(
    root,
    textvariable=shape_var,
    values=["cylinder", "cone", "sphere"]
)
shape_menu.pack()

ttk.Label(root, text="Radius").pack()
radius_entry = ttk.Entry(root)
radius_entry.pack()

ttk.Label(root, text="Height").pack()
height_entry = ttk.Entry(root)
height_entry.pack()

ttk.Label(root, text="Constant").pack()
constant_entry = ttk.Entry(root)
constant_entry.pack()

ttk.Label(root, text="Overflow Height").pack()
overflow_entry = ttk.Entry(root)
overflow_entry.pack()

ttk.Button(
    root,
    text="Calculate",
    command=calculate
).pack(pady=10)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()