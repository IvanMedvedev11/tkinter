from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x500")
def create_circle(ev):
    try:
        canvas.create_oval(int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()), fill='yellow')
    except ValueError:
        messagebox.showerror(message="Неверные данные")
def create_rectangle(ev):
    try:
        canvas.create_rectangle(int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()), fill='yellow')
    except ValueError:
        messagebox.showerror(message="Неверные данные")
def create_triangle(ev):
    try:
        canvas.create_polygon(int(ent1.get()), int(ent2.get()), int(ent3.get()), int(ent4.get()), int(ent5.get()), int(ent6.get()), fill='yellow')
    except ValueError:
        messagebox.showerror(message="Неверные данные")
def circle_btn_ent(ev):
    circle_btn['bg'] = 'white'
    circle_btn['fg'] = 'lightgreen'
def circle_btn_leave(ev):
    circle_btn['bg'] = 'lightgreen'
    circle_btn['fg'] = 'white'
def rectangle_btn_ent(ev):
    rectangle_btn['bg'] = 'white'
    rectangle_btn['fg'] = 'lightgreen'
def rectangle_btn_leave(ev):
    rectangle_btn['bg'] = 'lightgreen'
    rectangle_btn['fg'] = 'white'
def triangle_btn_ent(ev):
    triangle_btn['bg'] = 'white'
    triangle_btn['fg'] = 'lightgreen'
def triangle_btn_leave(ev):
    triangle_btn['bg'] = 'lightgreen'
    triangle_btn['fg'] = 'white'
canvas = Canvas(root, width=500, height=500, bg='lightblue', cursor='pencil')
canvas.pack(anchor=CENTER, expand=1)
circle_btn = Button(root, text="Create Circle", bg='lightgreen', fg='white')
circle_btn.place(x=10, y=50)
rectangle_btn = Button(root, text="Create Rectangle", bg='lightgreen', fg='white')
rectangle_btn.place(x=110, y=50)
triangle_btn = Button(root, text="Create Triangle", bg='lightgreen', fg='white')
triangle_btn.place(x=210, y=50)
ent1 = Entry(root)
ent2 = Entry(root)
ent3 = Entry(root)
ent4 = Entry(root)
ent5 = Entry(root)
ent6 = Entry(root)
ent1.place(x=10, y=100)
ent2.place(x=10, y=150)
ent3.place(x=10, y=200)
ent4.place(x=10, y=250)
ent5.place(x=10, y=300)
ent6.place(x=10, y=350)
circle_btn.bind('<Button-1>', create_circle)
circle_btn.bind('<Enter>', circle_btn_ent)
circle_btn.bind('<Leave>', circle_btn_leave)
rectangle_btn.bind('<Button-1>', create_rectangle)
rectangle_btn.bind('<Enter>', rectangle_btn_ent)
rectangle_btn.bind('<Leave>', rectangle_btn_leave)
triangle_btn.bind('<Button-1>', create_triangle)
triangle_btn.bind('<Enter>', triangle_btn_ent)
triangle_btn.bind('<Leave>', triangle_btn_leave)
root.mainloop()
