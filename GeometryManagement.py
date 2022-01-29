from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами виджетов
import webbrowser   # для вкладки 4
import pprint

tablo = Tk()   # создание окна
tablo.title("Упаковщики виджетов tkinter")
tablo.geometry('800x600')

s = ttk.Style()  # Создание экземпляра класса ttk.Style для работы с темами
t = s.theme_use()  # Вызывает применяемую  по умолчанию тему





# создание элемента управления вкладками
tab_control = ttk.Notebook(tablo, padding=10)  # класс Notebook,

tab0 = Frame(tab_control)
tab1 = Frame(tab_control)   # класс frame, создание вклажки 1
tab2 = Frame(tab_control)   # класс frame, создание вклажки 2
tab3 = Frame(tab_control)   # класс frame, создание вклажки 3
tab4 = Frame(tab_control)   # класс frame, создание вклажки 4
tab_control.add(tab0, text='Виджеты')   # добавление вкладки 0 в элемент управления вкладками
tab_control.add(tab1, text='Разметка Pack')   # добавление вкладки 1 в элемент управления вкладками
tab_control.add(tab2, text='Разметка Grid')    # добавление вкладки 2 в элемент управления вкладками
tab_control.add(tab3, text='Разметка Place')    # добавление вкладки 3 в элемент управления вкладками
tab_control.add(tab4, text='Спрака WIKIVERSITY')    # добавление вкладки 4 в элемент управления вкладками

# виджеты вкладки 0

def check():          # выполняется изменение темы по выбору в radiobutton
    rb = "{}".format(var.get())
    s.theme_use(rb)  # Применяет тему по выбору в radiobutton
    th = s.theme_use()  # Вызывает применяемую тему после изменениния в radiobutton
    lbl0.configure(text="Используется тема      " + th)
    lbl1.configure(text="Выбрана тема    " + rb)


def tk_print(new_string):  #  печать в окно entr1  из переменной wg2
    entr1.insert(END, new_string)

def process(self, *args):
        lbl04['text'] = entr1.get()  # вывод в lbl04 значения из entr1

def callbackfunc(event): #  выполняется изменение виджета по выбору combobox
    wg1 = event.widget.get()
    lbl03.configure(text=wg1)
    wg2 = lbl03.cget('text')
    tk_print(wg2)  #  печать в окно entr1  из переменной wg2 иместо print вызывается функция tk_print
    pprint.pprint(lbl03.config())  #  печатает все доступные параметры lbl02

  # Radiobutton
var = StringVar()  # Задание класса переменной var для Radiobutton  (BooleanVar, IntVar, DoubleVar, StringVar)
var.set('default')  # Значение переменной var по умолчанию
rb1 = ttk.Radiobutton(tab0, text='alt', variable=var, value='alt', command=check)
rb2 = ttk.Radiobutton(tab0, text='default', variable=var, value='default', command=check)
rb3 = ttk.Radiobutton(tab0, text='clam', variable=var, value='clam', command=check)
rb4 = ttk.Radiobutton(tab0, text='classic', variable=var, value='classic', command=check)

  # Entry
var1 = ()
entr1 = ttk.Entry(tab0, textvariable=var1)
  #var1.trace('w', process)  #  вызов функции вывода текста из entr1 в lbl04

  # Combobox
vc1 = StringVar()  # Задание класса переменной var для combobox
combo1 = ttk.Combobox(tab0, textvariable = vc1)  # Create Combobox, выбор виджета для отображения кофигурации
combo1['values'] = ("Button", "Radiobutton", "Checkbutton", "Entry", "Text", "Label", "Scale", "Combobox",
                    "Scrollbar", "Frame", "LabelFrame", "Listbox", "Canvas", "PanedWindow", "Menu", "Tk", "Toplevel")
combo1.current(2)
combo1.bind("<<ComboboxSelected>>", callbackfunc)


lbl1 = ttk.Label(tab0, text="Выбрана тема    " + var.get())
lbl0 = ttk.Label(tab0, text="Используется тема      " + t)
lbl10 = ttk.Label(tab0, text="Конфигурация виджета", underline=0)  # underline  указывает подчеркнутый символ
lbl03 = Label(tab0, text='выбор виджета', width=17, borderwidth=2, relief="groove")

lbl04 = ttk.Label(tab0, text='', width=17, borderwidth=2, relief="groove")

rb1.place(relx=0.05, rely=0.15)
rb2.place(relx=0.05, rely=0.2)
rb3.place(relx=0.05, rely=0.25)
rb4.place(relx=0.05, rely=0.3)
lbl1.place(relx=0.05, rely=0.1)
lbl0.place(relx=0.05, rely=0.03)
lbl10.place(relx=0.4, rely=0.03)
combo1.place(relx=0.4, rely=0.15)
entr1.place(relx=0.4, rely=0.25)
lbl03.place(relx=0.4, rely=0.1)
lbl04.place(relx=0.4, rely=0.3)


# виджеты вкладки 1
lbl11 = Label(tab1, text='1 метка\nside=left')
lbl13 = Label(tab1, text='2 метка\nside=top')
lbl12 = Label(tab1, text='3 метка\nside=left')
lbl14 = Label(tab1, text='4 метка\nside=top')
lbl15 = Label(tab1, text='5 метка\nside=top')
lbl16 = Label(tab1, text='6 метка\nside=left')
lbl17 = Label(tab1, text='7 метка\nside=right')
lbl18 = Label(tab1, text='8 метка\nside=right')
lbl19 = Label(tab1, text='9 метка\nside=bottom')
lbl10 = Label(tab1, text='10 метка\nside=bottom')
lbl11.pack(side='left')
lbl13.pack(side='top')
lbl12.pack(side='left')
lbl14.pack(side='top')
lbl15.pack(side='top')
lbl16.pack(side='left')
lbl17.pack(side='right')
lbl18.pack(side='right')
lbl19.pack(side='bottom')
lbl10.pack(side='bottom')

# виджеты вкладки 2
lbl21 = Label(tab2, text='1 column=0, row=0, columnspan=3, sticky=E', relief=GROOVE)
lbl22 = Label(tab2, text='2 column=0, row=1', relief=GROOVE)
lbl23 = Label(tab2, text='3 column=1, row=1', relief=GROOVE)
lbl24 = Label(tab2, text='4 column=2, row=1', relief=GROOVE)
lbl25 = Label(tab2, text='5 column=3, row=1', relief=GROOVE)
lbl26 = Label(tab2, text='6 column=0, row=2', relief=GROOVE)
lbl27 = Label(tab2, text='7 column=1, row=2', relief=GROOVE)
lbl28 = Label(tab2, text='8 column=2, row=2', relief=GROOVE)
lbl29 = Label(tab2, text='9 column=3, row=2', relief=GROOVE)
lbl20 = Label(tab2, text='10 column=0, row=3, columnspan=2, sticky=E', relief=GROOVE)
lbl21.grid(column=0, row=0, columnspan=3, sticky=E)
lbl22.grid(column=0, row=1)
lbl23.grid(column=1, row=1)
lbl24.grid(column=2, row=1)
lbl25.grid(column=3, row=1)
lbl26.grid(column=0, row=2)
lbl27.grid(column=1, row=2)
lbl28.grid(column=2, row=2)
lbl29.grid(column=3, row=2)
lbl20.grid(column=0, row=3, columnspan=2,  sticky=E)

# виджеты вкладки 3
lbl31 = Label(tab3, text='1 абсолютные координаты\nx=20,y=60')
lbl32 = Label(tab3, text='2 абсолютные координаты\nx=20,y=100')
lbl33 = ttk.Label(tab3, text='3 абсолютные координаты\nx=20,y=140')
lbl34 = Label(tab3, text='относительные координаты\n relx=0.75, rely=0.25, anchor=CENTER)')
lbl35 = Label(tab3, text='относительные координаты\n relx=0.25, rely=0.75 anchor не указан')
lbl36 = Label(tab3, text='относительные координаты\n relx=0.75, rely=0.75, anchor=CENTER)')
  # относительные координаты
lbl37 = Label(tab3, text='относительные координаты\nrelx=0.5, rely=0.5, anchor=CENTER')
lblNW = Label(tab3, text='относительные координаты\n relx=0, rely=0\nanchor не указан')
lblSE = Label(tab3, text='относительные координаты\n relx=1, rely=1, anchor=SE')
lblNE = Label(tab3, text='относительные координаты\n relx=1, rely=0, anchor=NE')
lblSW = Label(tab3, text='относительные координаты\n relx=0, rely=1, anchor=SW')
lblN = Label(tab3, text='относительные координаты\n relx=0.5, rely=0, anchor=N')
lblS = Label(tab3, text='относительные координаты\n relx=0.5, rely=1, anchor=S')
lblW = Label(tab3, text='относительные координаты\n relx=0, rely=0.5, anchor=W')
lblE = Label(tab3, text='относительные координаты\n relx=1, rely=0.5, anchor=E')
lbl31.place(x=20, y=60)  # абсолютные координаты
lbl32.place(x=20, y=100)  # абсолютные координаты
                              # при Label выравнивание строк текста внутри виджета по центру
lbl33.place(x=20, y=140)  # абсолютные координаты
                     # при ttk.Label выравнивание строк текста внутри виджета по левому краю
lbl34.place(relx=0.75, rely=0.25, anchor=CENTER)  # относительные координаты,
                                                  # при развертывании окна смещаются
lbl35.place(relx=0.25, rely=0.75)  # относительные координаты
lbl35.place(relx=0.25, rely=0.75)  # относительные координаты
lbl36.place(relx=0.75, rely=0.75, anchor=CENTER)  # относительные координаты
lbl37.place(relx=0.5, rely=0.5, anchor=CENTER)  # anchor показывает как текст привязан к указанной точке
# привязан центром к относительной точке relx=0.5, rely=0.5
lblNW.place(relx=0, rely=0)  # по умолчанию привязан левым верхним углом к относительной точке 0, 0
lblSE.place(relx=1, rely=1, anchor=SE)  # привязан правым нижним углом к относительной точке 1, 1
lblNE.place(relx=1, rely=0, anchor=NE)  # привязан правым верхним углом к относительной точке 1, 0
lblSW.place(relx=0, rely=1, anchor=SW)  # привязан левым нижним углом к относительной точке 0, 1
lblN.place(relx=0.5, rely=0, anchor=N)
lblS.place(relx=0.5, rely=1, anchor=S)
lblW.place(relx=0, rely=0.5, anchor=W)
lblE.place(relx=1, rely=0.5, anchor=E)
# виджеты вкладки 4


class WebOpen:
    def __init__(self):
        self.A = "https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_" \
                 "%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_" \
                 "%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5"
        self.B = "https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book#%D0%9E%D0%B1%D1%89%D0%B8%D0%B9_" \
                 "%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC"
        self.C = "https://www.etutorialspoint.com/index.php/274-python-tkinter-overview-and-examples"

    def open(self):
        webbrowser.open_new(self.A)
        webbrowser.open(self.B)
        webbrowser.open(self.C)


test = WebOpen()
b1 = Button(tab4, text="Tkinter\nWEB", command=test.open)
b1.pack()

tab_control.pack(expand=1, fill='both')   # запаковывает элемент управления вкладками
tablo.mainloop()
