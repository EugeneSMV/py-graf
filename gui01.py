from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами

tablo = Tk()
tablo.title("Графическая часть Python")
tablo.geometry('700x400+100+50')

s = ttk.Style()
s.configure('Bold.TLabel', font=('Helvetica', 12, 'normal'))
s.configure('Bold.TLabel',  borderwidth=3, relief=GROOVE,
            background="#ccc", width=17, height=20, padx=5, pady=5, anchor=CENTER)

lbl1 = ttk.Label(tablo, text="Ввести название",  style='Bold.TLabel')
lbl1.place(relx=0.05, rely=0.1)
txt = Entry(tablo, width=20, relief=GROOVE,  borderwidth=5)
txt.place(relx=0.3, rely=0.2)
lbl2 = ttk.Label(tablo, text="Фаза", style='Bold.TLabel')
lbl2.place(relx=0.05, rely=0.2)
lbl3 = ttk.Label(tablo, text="Объект:", style='Bold.TLabel')
lbl3.place(relx=0.05, rely=0.3)

tablo.mainloop()
