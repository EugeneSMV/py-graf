from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами
tablo = Tk()
tablo.title("Графическая часть Python")
tablo.geometry('700x400+100+50')

s = ttk.Style()
s.theme_use('alt')  # Вибирает тему виджетов из стандарнтых 'alt', 'default', 'clam', 'classic'
t = s.theme_use()

lbl0 = ttk.Label(tablo, text="Используется тема      " + t)
lbl0.place(relx=0.2, rely=0.05)
lbl1 = ttk.Label(tablo, text="\n   Ввести\n   название\n", width=15, relief="groove")
lbl1.place(relx=0.05, rely=0.1)
txt = Entry(tablo, width=20)
txt.place(relx=0.3, rely=0.2)
lbl2 = ttk.Label(tablo, text="Фаза")
lbl2.place(relx=0.05, rely=0.3)
lbl3 = ttk.Label(tablo, text="Объект")
lbl3.place(relx=0.05, rely=0.4)
rb1 = ttk.Radiobutton(tablo, text='5', value=5)
rb1.place(relx=0.05, rely=0.5)
but = ttk.Button(tablo, text='Next')
but.place(relx=0.05, rely=0.6)
tablo.mainloop()
