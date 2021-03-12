import tkinter as tk
from tkinterViews import manageNews as newsManager


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_post = tk.Button(self)
        self.manage_news = tk.Button(self)
        self.master = master
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.create_widgets()
        self.winfo_toplevel().title("Cats opinion admin panel - Central area")

    def create_widgets(self):
        self.create_post["text"] = "Add blogpost"
        self.create_post["command"] = self.move_to_blog_manager
        self.create_post.pack(side="left", padx=25)
        self.manage_news["text"] = "Manage news"
        self.manage_news["command"] = self.move_to_news_manager
        self.manage_news.pack(side="left", padx=25)

    def move_to_blog_manager(self):
        print("opening blog manager")

    def move_to_news_manager(self):
        manage_root = tk.Tk()
        manage_root.geometry("1280x720")
        newsManager.ManageNews(master=manage_root).mainloop()
