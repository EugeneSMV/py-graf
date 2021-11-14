from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами виджетов

tablo = Tk()   # создание окна
tablo.title("Кабельный журнал")
tablo.geometry('1000x600')


def clicked():          # выполняемая функция при нажатии кнопки Next, Всталяет текст из поля Entry  в поле lbl13
    res0 = "{}".format(num.get())
    res1 = "{}".format(comboT.get())
    res2 = "{}".format(comboC.get())
    res3 = "{}".format(comboS.get())
    res4 = "{}".format(length.get())
    lbl10.configure(text=res0 + '       ' + res1 + "  -  " + res2 + "x" + res3 + " мм     " + res4 + " м")


btn = Button(tablo, text="Добавить", command=clicked, font=("Arial Narrow", 14))
btn.grid(column=4, row=0, sticky=E, padx=10)

lbl01 = Label(tablo, text="Кабель:", font=("Arial Narrow", 14))
lbl01.grid(column=0, row=0)
lbl10 = Label(tablo, text="", font=("Arial Narrow", 14), width=60, borderwidth=3, relief="groove")
lbl10.grid(column=1, row=0, columnspan=3)
lbl11 = Label(tablo, text="Номер", font=("Arial Narrow", 14))
lbl11.grid(column=0, row=1)
lbl12 = Label(tablo, text="Тип", font=("Arial Narrow", 14))
lbl12.grid(column=1, row=1, padx=6)
lbl13 = Label(tablo, text="Жилы", font=("Arial Narrow", 14))
lbl13.grid(column=2, row=1, padx=10)
lbl14 = Label(tablo, text="Сечение", font=("Arial Narrow", 14))
lbl14.grid(column=3, row=1, padx=10)
lbl15 = Label(tablo, text="Длина", font=("Arial Narrow", 14))
lbl15.grid(column=4, row=1, padx=10)

num = Entry(tablo, width=20, borderwidth=3)   # Номер кабеля
num.grid(column=0, row=2)
comboT = ttk.Combobox(tablo)  # параменты поля с выпадающим списком ТИП
comboT['values'] = ("КВВГнг-ls", "КВВГнг-ls", "ВВГ", "Текст")
comboT.current(0)                # установите вариант по умолчанию - номер по порядку
comboT.grid(column=1, row=2, padx=10)
comboC = ttk.Combobox(tablo)  # параменты поля с выпадающим списком Колличество жил
comboC['values'] = ("2", "3", "4", "5", "7", "10", "15", "19", "Текст")
comboC.current(2)                # установите вариант по умолчанию - номер по порядку
comboC.grid(column=2, row=2, padx=10)
comboS = ttk.Combobox(tablo)  # параменты поля с выпадающим списком Сечение жил
comboS['values'] = ("0,75", "1,0", "1,5", "2,0", "2,5", "4,0", "6", "Текст")
comboS.current(2)                # установите вариант по умолчанию - номер по порядку
comboS.grid(column=3, row=2, padx=10)
length = Entry(tablo, width=20, borderwidth=3)   # Длина кабеля
length.grid(column=4, row=2)

tablo.mainloop()
