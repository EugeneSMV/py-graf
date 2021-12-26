from tkinter import *
from tkinter import ttk

tablo = Tk()
tablo.title("Графическая часть Python")
tablo.geometry('700x400+100+50')

res = 'dfghjk'

def clicked():          # выполняемая функция при нажатии кнопки Next, Всталяет текст из поля Entry  в поле lbl13
    global res

    res = "{}".format(txt.get())
    lbl0.configure(text=res)
    lbl1['text'] = txt.get()
    return res

txt = Entry(tablo, width=20, borderwidth=3)
txt.place(relx=0.2, rely=0.25)



btn = Button(tablo, text="Next", command=clicked)
btn.place(relx=0.05, rely=0.6)

lbl0 = ttk.Label(tablo, text='yyyyyyyyyyyyyyy')
lbl0.place(relx=0.2, rely=0.05)

lbl1 = ttk.Label(tablo, text=res)
lbl1.place(relx=0.2, rely=0.15)

lbl2 = ttk.Label(tablo, text='444')
lbl2.place(relx=0.2, rely=0.20)



tablo.mainloop()

