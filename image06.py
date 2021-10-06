import tkinter as tk


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):    # В Python  метод __init__() играет роль конструктора класса.
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # GUI starts here
        self.label = tk.Label(parent, text="Give values")
        self.label.grid(row=1)

        # creating all the variables
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()

        # creating all the entry widgets
        tk.Entry(self, textvariable=self.var1).grid(row=3, column=1, padx=5)
        tk.Entry(self, textvariable=self.var2).grid(row=3, column=2, padx=5)
        tk.Entry(self, textvariable=self.var3).grid(row=3, column=3, padx=5)
        tk.Entry(self, textvariable=self.var4).grid(row=3, column=4, padx=5)
        tk.Entry(self, textvariable=self.var5).grid(row=3, column=5, padx=5)

        # creating all the labels
        self.l1 = tk.Label(self, width=17, borderwidth=2, relief="groove")
        self.l1.grid(row=4, column=1, pady=10)

        self.l2 = tk.Label(self, width=17, borderwidth=2, relief="groove")
        self.l2.grid(row=4, column=2, pady=10)

        self.l3 = tk.Label(self, width=17, borderwidth=2, relief="groove")
        self.l3.grid(row=4, column=3, pady=10)

        self.l4 = tk.Label(self, width=17, borderwidth=2, relief="groove")
        self.l4.grid(row=4, column=4, pady=10)

        self.l5 = tk.Label(self, width=17, borderwidth=2, relief="groove")
        self.l5.grid(row=4, column=5, pady=10)

        # tracing all the variables
        self.var1.trace('w', self.process)
        self.var2.trace('w', self.process)
        self.var3.trace('w', self.process)
        self.var4.trace('w', self.process)
        self.var5.trace('w', self.process)

    # the function to be called each time an entry is changed
    def process(self, *args):
        # assigning new value of entry onto the label
        self.l1['text'] = self.var1.get()
        self.l2['text'] = self.var2.get()
        self.l3['text'] = self.var3.get()
        self.l4['text'] = self.var4.get()
        self.l5['text'] = self.var5.get()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x800")
    MainApplication(root).grid()
    root.mainloop()