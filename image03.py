from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами виджетов
import webbrowser   # для вкладки 4

tablo = Tk()   # создание окна
tablo.title("Виды разметок виджетов tkinter")
tablo.geometry('800x600')

tab_control = ttk.Notebook(tablo)  # класс Notebook, создание элеемента управления вкладкой

tab1 = Frame(tab_control)   # класс frame, создание вклажки 1 нет необходимости импорта в виде <ttk.Frame>
tab2 = Frame(tab_control)   # класс frame, создание вклажки 2
tab3 = Frame(tab_control)   # класс frame, создание вклажки 3
tab4 = Frame(tab_control)   # класс frame, создание вклажки 4
tab_control.add(tab1, text='Разметка Tk Grid')   # добавление вкладки 1 в элемент управления вкладками
tab_control.add(tab2, text='Разметка Ttk ')    # добавление вкладки 2 в элемент управления вкладками
tab_control.add(tab3, text='Третья')    # добавление вкладки 3 в элемент управления вкладками
tab_control.add(tab4, text='Открыть страницу Google')    # добавление вкладки 4 в элемент управления вкладками

# виджеты вкладки 1


def clicked():          # выполняемая функция при нажатии кнопки Next, Всталяет текст из поля Entry  в поле lbl13
    res = "Объект:  {}".format(txt.get())
    lbl13.configure(text=res)


btn = Button(tab1, text="Next", command=clicked, font=("Arial Narrow", 14), )
btn.grid(column=4, row=0, sticky=E, padx=10)

lbl11 = Label(tab1, text="Ввести название ==>", font=("Arial Narrow", 14))
lbl11.grid(column=0, row=0)
txt = Entry(tab1, width=20)
txt.grid(column=1, row=0)
lbl12 = Label(tab1, text="Фаза", font=("Arial Narrow", 14))
lbl12.grid(column=2, row=0, padx=10)
combo = ttk.Combobox(tab1)  # параменты поля с выпадающим списком,
# импорт выполнен ttk.Combobox, если взять просто  Combobox
# то нужно выполнить импорт модуля ttk из пакета Tkinter, вначале <from tkinter.ttk import Combobox>
combo['values'] = ("A", "B", "C", "Текст")
combo.current(0)                # установите вариант по умолчанию - номер по порядку
combo.grid(column=3, row=0, padx=10)
lbl13 = Label(tab1, text="Объект:", font=("Arial Narrow", 14))
lbl13.grid(column=0, row=1)

# виджеты вкладки 2
lbl22 = Label(tab2, text='Вкладка 2')
lbl22.grid(column=0, row=0)
lbl23 = Label(tab2, text="Объект:", font=("Arial Narrow", 14))
lbl23.grid(column=3, row=0, sticky=E)
combo2 = ttk.Combobox(tab2)  # параменты поля с выпадающим списком,
# импорт выполнен ttk.Combobox, если взять просто  Combobox
# то нужно выполнить импорт модуля ttk из пакета Tkinter, вначале <from tkinter.ttk import Combobox>
combo2['values'] = ("A", "B", "C", "Текст")
combo2.current(0)                # установите вариант по умолчанию - номер по порядку
combo2.grid(column=2, row=0, padx=10)

# виджеты вкладки 3


def change():
    b['fg'] = "blue"
    b['activeforeground'] = "blue"


b = Button(tab3, text='BLUE', width=10, height=3)
b.bind('<Button-1>', change)
b.bind('<Return>', change)
b.pack()

# виджеты вкладки 4


class WebOpen3:
    def __init__(self):
        self.A = "http://www.google.ru"

    def open(self):
        webbrowser.open_new(self.A)


test = WebOpen3()
b1 = Button(tab4, text="Google", command=test.open)
b1.pack()
tab_control.pack(expand=1, fill='both')   # запаковывает элемент управления вкладками
tablo.mainloop()
