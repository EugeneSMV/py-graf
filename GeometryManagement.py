from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами виджетов
import webbrowser   # для вкладки 4


tablo = Tk()   # создание окна
tablo.title("Упаковщики виджетов tkinter")
tablo.geometry('800x600')

s = ttk.Style()

def check():          # выполняемая функция при нажатии кнопки Next, Всталяет текст из поля Entry  в поле lbl13
    rb = "{}".format(var.get())
    lbl1.configure(text=rb)
    s.theme_use(rb)  # Вибирает тему виджетов из стандарнтых 'alt', 'default', 'clam', 'classic'





tab_control = ttk.Notebook(tablo, padding=10)  # класс Notebook, создание элеемента управления вкладкой

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





var = StringVar()
var.set('classic')
rb1 = ttk.Radiobutton(tab0, text='alt', variable=var, value='alt', command=check)
rb1.place(relx=0.05, rely=0.15)
rb2 = ttk.Radiobutton(tab0, text='default', variable=var, value='default', command=check)
rb2.place(relx=0.05, rely=0.2)
rb3 = ttk.Radiobutton(tab0, text='clam', variable=var, value='clam', command=check)
rb3.place(relx=0.05, rely=0.25)
rb4 = ttk.Radiobutton(tab0, text='classic', variable=var, value='classic', command=check)
rb4.place(relx=0.05, rely=0.3)



lbl1 = ttk.Label(tab0, text=var.get())
lbl1.place(relx=0.05, rely=0.1)

t = s.theme_use()

lbl0 = ttk.Label(tab0, text="Используется тема      " + t)
lbl0.place(relx=0.05, rely=0.03)

# виджеты вкладки 1
lbl11 = Label(tab1, text='1 метка\nside=left')
lbl11.pack(side='left')
lbl13 = Label(tab1, text='2 метка\nside=top')
lbl13.pack(side='top')
lbl12 = Label(tab1, text='3 метка\nside=left')
lbl12.pack(side='left')
lbl14 = Label(tab1, text='4 метка\nside=top')
lbl14.pack(side='top')
lbl15 = Label(tab1, text='5 метка\nside=top')
lbl15.pack(side='top')
lbl16 = Label(tab1, text='6 метка\nside=left')
lbl16.pack(side='left')
lbl17 = Label(tab1, text='7 метка\nside=right')
lbl17.pack(side='right')
lbl18 = Label(tab1, text='8 метка\nside=right')
lbl18.pack(side='right')
lbl19 = Label(tab1, text='9 метка\nside=bottom')
lbl19.pack(side='bottom')
lbl10 = Label(tab1, text='10 метка\nside=bottom')
lbl10.pack(side='bottom')

# виджеты вкладки 2
lbl21 = Label(tab2, text='1 column=0, row=0, columnspan=3, sticky=E', relief=GROOVE)
lbl21.grid(column=0, row=0, columnspan=3, sticky=E)
lbl22 = Label(tab2, text='2 column=0, row=1', relief=GROOVE)
lbl22.grid(column=0, row=1)
lbl23 = Label(tab2, text='3 column=1, row=1', relief=GROOVE)
lbl23.grid(column=1, row=1)
lbl24 = Label(tab2, text='4 column=2, row=1', relief=GROOVE)
lbl24.grid(column=2, row=1)
lbl25 = Label(tab2, text='5 column=3, row=1', relief=GROOVE)
lbl25.grid(column=3, row=1)
lbl26 = Label(tab2, text='6 column=0, row=2', relief=GROOVE)
lbl26.grid(column=0, row=2)
lbl27 = Label(tab2, text='7 column=1, row=2', relief=GROOVE)
lbl27.grid(column=1, row=2)
lbl28 = Label(tab2, text='8 column=2, row=2', relief=GROOVE)
lbl28.grid(column=2, row=2)
lbl29 = Label(tab2, text='9 column=3, row=2', relief=GROOVE)
lbl29.grid(column=3, row=2)
lbl20 = Label(tab2, text='10 column=0, row=3, columnspan=2, sticky=E', relief=GROOVE)
lbl20.grid(column=0, row=3, columnspan=2,  sticky=E)

# виджеты вкладки 3
lbl31 = Label(tab3, text='1 абсолютные координаты\nx=20,y=60')  # абсолютные координаты
lbl31.place(x=20, y=60)
lbl32 = Label(tab3, text='2 абсолютные координаты\nx=20,y=100')  # абсолютные координаты
                                                      # при Label выравнивание строк текста внутри виджета по центру
lbl32.place(x=20, y=100)
lbl33 = ttk.Label(tab3, text='3 абсолютные координаты\nx=20,y=140')  # абсолютные координаты,
                                             # при ttk.Label выравнивание строк текста внутри виджета по левому краю
lbl33.place(x=20, y=140)
lbl34 = Label(tab3, text='относительные координаты\n relx=0.75, rely=0.25, anchor=CENTER)')
lbl34.place(relx=0.75, rely=0.25, anchor=CENTER)  # относительные координаты, при развертывании окна смещаются
lbl35 = Label(tab3, text='относительные координаты\n relx=0.25, rely=0.75 anchor не указан')  # относительные координаты
lbl35.place(relx=0.25, rely=0.75)
lbl36 = Label(tab3, text='относительные координаты\n relx=0.75, rely=0.75, anchor=CENTER)')  # относительные координаты
lbl36.place(relx=0.75, rely=0.75, anchor=CENTER)
lbl37 = Label(tab3, text='относительные координаты\nrelx=0.5, rely=0.5, anchor=CENTER')  # относительные координаты
lbl37.place(relx=0.5, rely=0.5, anchor=CENTER)  # anchor показывает как текст привязан к указанной точке
# привязан центромк относительной точке relx=0.5, rely=0.5
lblNW = Label(tab3, text='относительные координаты\n relx=0, rely=0\nanchor не указан')  # относительные координаты
lblNW.place(relx=0, rely=0)  # по умолчанию привязан левым верхним углом к относительной точке 0, 0
lblSE = Label(tab3, text='относительные координаты\n relx=1, rely=1, anchor=SE')  # относительные координаты
lblSE.place(relx=1, rely=1, anchor=SE)  # привязан правым нижним углом к относительной точке 1, 1
lblNE = Label(tab3, text='относительные координаты\n relx=1, rely=0, anchor=NE')  # относительные координаты
lblNE.place(relx=1, rely=0, anchor=NE)  # привязан правым верхним углом к относительной точке 1, 0
lblSW = Label(tab3, text='относительные координаты\n relx=0, rely=1, anchor=SW')  # относительные координаты
lblSW.place(relx=0, rely=1, anchor=SW)  # привязан левым нижним углом к относительной точке 0, 1
lblN = Label(tab3, text='относительные координаты\n relx=0.5, rely=0, anchor=N')  # относительные координаты
lblN.place(relx=0.5, rely=0, anchor=N)
lblS = Label(tab3, text='относительные координаты\n relx=0.5, rely=1, anchor=S')  # относительные координаты
lblS.place(relx=0.5, rely=1, anchor=S)
lblW = Label(tab3, text='относительные координаты\n relx=0, rely=0.5, anchor=W')  # относительные координаты
lblW.place(relx=0, rely=0.5, anchor=W)
lblE = Label(tab3, text='относительные координаты\n relx=1, rely=0.5, anchor=E')  # относительные координаты
lblE.place(relx=1, rely=0.5, anchor=E)
# виджеты вкладки 4


class WebOpen:
    def __init__(self):
        self.A = "https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_" \
                 "%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_" \
                 "%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_Python#%D0%92%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5"
        self.B = "https://ru.wikibooks.org/wiki/GUI_Help/Tkinter_book#%D0%9E%D0%B1%D1%89%D0%B8%D0%B9_" \
             "%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC"

    def open(self):
        webbrowser.open_new(self.A)
        webbrowser.open(self.B)


test = WebOpen()
b1 = Button(tab4, text="Tkinter\nWEB", command=test.open)
b1.pack()


tab_control.pack(expand=1, fill='both')   # запаковывает элемент управления вкладками
tablo.mainloop()
