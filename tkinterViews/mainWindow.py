import tkinter as tk
from tkinterViews import manageNews as newsManager
from tkinterViews import readMessages as Rm
from tkinterViews import insertBlogPost as Ib


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.create_post = tk.Button(self)
        self.manage_news = tk.Button(self)
        self.messages = tk.Button(self)
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
        self.messages["text"] = "Messages"
        self.messages["command"] = self.move_to_message_manager
        self.messages.pack(side="left", padx=25)

    def move_to_blog_manager(self):
        # TODO read from config file
        series = ["personal", "what is my cat?"]
        manage_blog = tk.Tk()
        manage_blog.geometry("1280x720")
        Ib.InsertBlog(master=manage_blog, series_list=series).mainloop()


    def move_to_message_manager(self):
        # TODO read messages from db
        dummy_messages = [
            {"uid": "123", "headline": "asdasd", "date": "12/3/2021", "message": "test messagedasdajsdkjasdaksjhdkasjdalsjdhlaksjdhalksjdhalskjdhalsjdhaksjdhlasjdhalksjhdklasjhdjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", "name": "", "type": "question", "email":""},
            {"uid": "321", "headline": "dsadsa", "date": "10/3/2021", "message": "test message", "name": "", "type": "question", "email": "asd@asd.com"},
            {"uid": "777", "headline": "teststststs", "date": "11/3/2021", "message": "test message", "name": "", "type": "question", "email": ""}
        ]
        message_root = tk.Tk()
        message_root.geometry("1280x720")
        Rm.ReadMessages(master=message_root, messages=dummy_messages).mainloop()

    def move_to_news_manager(self):
        manage_root = tk.Tk()
        manage_root.geometry("1280x720")
        newsManager.ManageNews(master=manage_root).mainloop()
