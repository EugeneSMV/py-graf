from tkinter import *
from tkinter import ttk  # импорт модуля ttk с классами виджетов
import webbrowser   # для вкладки 4

tablo = Tk()   # создание окна
tablo.title("Упаковщики виджетов tkinter")
tablo.geometry('800x600')

tab_control = ttk.Notebook(tablo)  # класс Notebook, создание элеемента управления вкладкой

tab1 = Frame(tab_control)   # класс frame, создание вклажки 1 нет необходимости импорта в виде <ttk.Frame>
tab2 = Frame(tab_control)   # класс frame, создание вклажки 2
tab3 = Frame(tab_control)   # класс frame, создание вклажки 3
tab4 = Frame(tab_control)   # класс frame, создание вклажки 4
tab_control.add(tab1, text='Разметка Pack')   # добавление вкладки 1 в элемент управления вкладками
tab_control.add(tab2, text='Разметка Grid')    # добавление вкладки 2 в элемент управления вкладками
tab_control.add(tab3, text='Разметка Place')    # добавление вкладки 3 в элемент управления вкладками
tab_control.add(tab4, text='Открыть страницу Google')    # добавление вкладки 4 в элемент управления вкладками

# виджеты вкладки 1
lbl11 = Label(tab1, text='1 left 1')
lbl11.pack(side='left')
lbl13 = Label(tab1, text='2 top 1')
lbl13.pack(side='top')
lbl12 = Label(tab1, text='3 left 2')
lbl12.pack(side='left')
lbl14 = Label(tab1, text='4 top 2')
lbl14.pack(side='top')
lbl15 = Label(tab1, text='5 top 3')
lbl15.pack(side='top')
lbl16 = Label(tab1, text='6 left 1')
lbl16.pack(side='left')
lbl17 = Label(tab1, text='7 right 1')
lbl17.pack(side='right')
lbl18 = Label(tab1, text='8 right 2')
lbl18.pack(side='right')
lbl19 = Label(tab1, text='9 bottom 1')
lbl19.pack(side='bottom')
lbl10 = Label(tab1, text='10 bottom 2')
lbl10.pack(side='bottom')

# виджеты вкладки 2
lbl21 = Label(tab2, text='1 column=0, row=0, columnspan=3')
lbl21.grid(column=0, row=0, columnspan=3, sticky=E)
lbl22 = Label(tab2, text='2 column=0, row=1')
lbl22.grid(column=0, row=1)
lbl23 = Label(tab2, text='3 column=1, row=1')
lbl23.grid(column=1, row=1)
lbl24 = Label(tab2, text='4 column=2, row=1')
lbl24.grid(column=2, row=1)
lbl25 = Label(tab2, text='5 column=3, row=1')
lbl25.grid(column=3, row=1)
lbl26 = Label(tab2, text='6 column=0, row=2')
lbl26.grid(column=0, row=2)
lbl27 = Label(tab2, text='7 column=1, row=2')
lbl27.grid(column=1, row=2)
lbl28 = Label(tab2, text='8 column=2, row=2')
lbl28.grid(column=2, row=2)
lbl29 = Label(tab2, text='9 column=3, row=2')
lbl29.grid(column=3, row=2)
lbl20 = Label(tab2, text='10 column=0, row=3, columnspan=2')
lbl20.grid(column=0, row=3, columnspan=2,  sticky=E)

# виджеты вкладки 3
lbl31 = Label(tab3, text='1 x=20,y=20')  # абсолютные координаты
lbl31.place(x=20, y=20)
lbl32 = Label(tab3, text='2 x=20,y=40')  # абсолютные координаты
lbl32.place(x=20, y=40)
lbl33 = Label(tab3, text='3 x=20,y=60')  # абсолютные координаты
lbl33.place(x=20, y=60)
lbl34 = Label(tab3, text='4 relx=0.75, rely=0.25')
lbl34.place(relx=0.75, rely=0.25)  # относительные координаты, при развертывании окна смещаются
lbl35 = Label(tab3, text='5 relx=0.25, rely=0.75')  # относительные координаты
lbl35.place(relx=0.25, rely=0.75)
lbl36 = Label(tab3, text='6 relx=0.75, rely=0.75')  # относительные координаты
lbl36.place(relx=0.75, rely=0.75)
lbl37 = Label(tab3, text='7 SE')  # относительные координаты
lbl37.place(relx=0.5, rely=0.5, anchor=SE)  # anchor показывает каким углом текст привязан к заданной точке
lbl38 = Label(tab3, text='8 SW')  # относительные координаты
lbl38.place(relx=0.5, rely=0.5, anchor=SW)
lbl39 = Label(tab3, text='9 NE')  # относительные координаты
lbl39.place(relx=0.5, rely=0.5, anchor=NE)
lbl30 = Label(tab3, text='10 NW')  # относительные координаты
lbl30.place(relx=0.5, rely=0.5, anchor=NW)
lblNW = Label(tab3, text='NW')  # относительные координаты
lblNW.place(relx=0, rely=0)  # по умолчанию привязан левым верхним углом к относительной точке 0, 0
lblSE = Label(tab3, text='SE')  # относительные координаты
lblSE.place(relx=1, rely=1, anchor=SE)  # привязан правым нижним углом к относительной точке 1, 1
lblNE = Label(tab3, text='NE')  # относительные координаты
lblNE.place(relx=1, rely=0, anchor=NE)  # привязан правым верхним углом к относительной точке 1, 0
lblSW = Label(tab3, text='SW')  # относительные координаты
lblSW.place(relx=0, rely=1, anchor=SW)  # привязан левым нижним углом к относительной точке 0, 1
lblN = Label(tab3, text='N')  # относительные координаты
lblN.place(relx=0.5, rely=0, anchor=N)
lblS = Label(tab3, text='S')  # относительные координаты
lblS.place(relx=0.5, rely=1, anchor=S)
lblW = Label(tab3, text='W')  # относительные координаты
lblW.place(relx=0, rely=0.5, anchor=W)
lblE = Label(tab3, text='E')  # относительные координаты
lblE.place(relx=1, rely=0.5, anchor=E)
# виджеты вкладки 4


class WebOpen3:
    def __init__(self):
        self.A = "https://ru.wikiversity.org/wiki/%D0%9A%D1%83%D1%80%D1%81_%D0%BF%D0%BE_" \
                 "%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B5_Tkinter_" \
                 "%D1%8F%D0%B7%D1%8B%D0%BA%D0%B0_" \
                 "Python#%D0%A3%D0%BF%D0%B0%D0%BA%D0%BE%D0%B2%D1%89%D0%B8%D0%BA%D0%B8"

    def open(self):
        webbrowser.open_new(self.A)


test = WebOpen3()
b1 = Button(tab4, text="Tkinter", command=test.open)
b1.pack()
tab_control.pack(expand=1, fill='both')   # запаковывает элемент управления вкладками
tablo.mainloop()
