from tkinter import *
from tkinter import messagebox
root = Tk()
window = Tk()
w2 = Tk()
window.title("Второе окно")
window.geometry('500x300')
def set_blue():
    bt2['bg'] = 'blue'
    bt2['activeforeground'] = 'blue'
def show_message():
    messagebox.showinfo("wrj;vnwrgv", ent.get())
root.title("Окно без заголовка")
root.geometry("500x300+0+0")
image = PhotoImage(file="images.jpg")
bt1 = Button(root, bg='red', fg='white', image=image)
bt1.place(x=0, y=0)
bt2 = Button(root, text='Кнопка 2', bg='red', fg='white', font=('Comic Sans', 10), padx=10, pady=10, activebackground='white', activeforeground='red')
bt2['command'] = set_blue
bt2.place(x=400, y=0)
bt3 = Button(window, height=300, width=500)
bt3.place(x=0, y=0)
b1 = Button(w2)
b2 = Button(w2)
b3 = Button(w2)
b4 = Button(w2)
txt = Label(w2, text="Текст")
b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=0, row=1)
b4.grid(column=1, row=1)
txt.grid(column=2, row=0)
ent = Entry(w2)
ent.grid(column=2, row=1)
b4['command'] = show_message
root.mainloop()
window.mainloop()
