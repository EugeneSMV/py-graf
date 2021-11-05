from tkinter import *
from tkinter.ttk import *

root_window = Tk()
root_window.title("Виды разметок виджетов PythonRu")
root_window.geometry('800x600')


estyle = Style()
estyle.element_create("plain.field", "from", "clam")
estyle.layout("EntryStyle.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])

estyle.configure("EntryStyle.TEntry",
                 foreground="dark blue",
                 fieldbackground="light blue")           # Set color here

entry = Entry(root_window, style="EntryStyle.TEntry")
entry.pack(padx=10, pady=10)

root_window.mainloop()