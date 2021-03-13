import json
import tkinter as tk


class ReadMessages(tk.Frame):
    def __init__(self, master=None, messages=None):
        super().__init__(master)
        self.scroll = tk.Scrollbar(self, orient="vertical")
        self.scroll_hor = tk.Scrollbar(self, orient="horizontal")
        self.scroll.pack(side="right", fill="y")
        self.scroll_hor.pack(side="bottom", fill="x")
        self.list = tk.Listbox(self, height=100, width=190, font=("Times", 12))
        self.index = 0
        for message in messages:
            self.list.insert(self.index, json.dumps(message))
            self.index += 1
            self.list.insert(self.index, "----*****----")
            self.index += 1
        self.master = master
        self.scroll.config(command=self.list.yview)
        self.scroll_hor.config(command=self.list.xview)
        self.list.pack()
        self.pack()
        self.winfo_toplevel().title("Cats opinion admin panel - Messages")
