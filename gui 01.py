import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ttk Notebook")

        todos = {
            "Дом": ["Постирать", "Сходить за продуктами"],
            "Работа": ["Установить Python", "Учить Tkinter", "Разобрать почту"],
            "Отпуск": ["Отдых!"]
        }

        self.notebook = ttk.Notebook(self, width=800, height=600, padding=5)
        for key, value in todos.items():
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=key, underline=0,
                              sticky=tk.NE + tk.SW)
            for text in value:
                ttk.Label(frame, text=text).pack(anchor=tk.W)
        self.label = ttk.Label(self)

        self.notebook.pack()
        self.label.pack(anchor=tk.W)
        self.notebook.enable_traversal()
        self.notebook.bind("<<NotebookTabChanged>>", self.select_tab)

    def select_tab(self, event):
        tab_id = self.notebook.select()
        tab_name = self.notebook.tab(tab_id, "text")
        text = "Ваш текущий выбор: {}".format(tab_name)
        self.label.config(text=text)

if __name__ == "__main__":
    app = App()
    app.mainloop()