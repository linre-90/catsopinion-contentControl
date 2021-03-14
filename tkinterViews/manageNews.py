import tkinter as tk
from datetime import date
import news
import tkinter.ttk as tt
from tkinter.messagebox import showerror, showinfo, askyesno


class ManageNews(tk.Frame):
    def __init__(self, master=None):
        self.padding_for_x = 30
        self.padding_for_y = 30
        self.news_handler = news.News()
        super().__init__(master)
        # lang
        self.languages = ["fi", "en"]
        self.selected = tk.StringVar()
        self.language_label = tk.Label(self)
        self.language_select = tt.Combobox(self, textvariable=self.selected, values=self.languages)
        self.build_language_field()
        # hint labels:
        self.remove_hint = tk.Label(self)
        self.add_new_hint = tk.Label(self)
        # lists all current news
        self.list_of_news = tk.Listbox(self)
        self.fill_list_view(self.news_handler.get_news())
        # delete from db button
        self.delete_from_db = tk.Button(self)
        # create new: headline field
        self.headline_label = tk.Label(self)
        self.headline = tk.Text(self)
        # create new: message field
        self.message_label = tk.Label(self)
        self.message = tk.Text(self)
        # create new: date
        self.date_label = tk.Label(self)
        self.news_date = tk.Entry(self)
        # create new: push to db
        self.add_news = tk.Button(self)
        self.master = master
        self.pack()
        self.create_hint_headers()
        self.create_list_view()
        self.create_delete_from_db_btn()
        self.create_new_news_components()
        self.winfo_toplevel().title("Cats opinion admin panel - Edit news")

    def build_language_field(self):
        self.selected.set(self.languages[0])
        self.language_label["text"] = "Select language"
        self.language_label.grid(row=7, column=2, padx=(self.padding_for_x, 0))
        self.language_select.grid(row=8, column=2, padx=(self.padding_for_x, 0))

    def create_hint_headers(self):
        self.remove_hint["text"] = "Remove existing news"
        self.add_new_hint["text"] = "Save new news to database"
        self.remove_hint.config(font=("Courier", 16))
        self.add_new_hint.config(font=("Courier", 16))
        self.remove_hint.grid(row=0, column=0, padx=(0, self.padding_for_x), pady=(0, self.padding_for_y))
        self.add_new_hint.grid(row=0, column=2, pady=(0, self.padding_for_y))

    def create_list_view(self):
        self.list_of_news["width"] = 70
        self.list_of_news.grid(row=1, column=0, padx=(0, self.padding_for_x))

    def create_delete_from_db_btn(self):
        self.delete_from_db["text"] = "Delete selected"
        self.delete_from_db["command"] = self.delete_trigger
        self.delete_from_db["bg"] = "red"
        self.delete_from_db["fg"] = "black"
        self.delete_from_db["padx"] = 10
        self.delete_from_db["pady"] = 10
        self.delete_from_db.grid(row=2, column=0, padx=(0, self.padding_for_x))

    def create_new_news_components(self):
        # headline
        self.headline_label["text"] = "Insert headline"
        self.headline_label.grid(row=1, column=2, padx=(self.padding_for_x, 0))
        self.headline["height"] = 2
        self.headline["width"] = 50
        self.headline.grid(row=2, column=2, padx=(self.padding_for_x, 0))
        # message
        self.message_label["text"] = "Insert message"
        self.message_label.grid(row=3, column=2, padx=(self.padding_for_x, 0))
        self.message["height"] = 2
        self.message["width"] = 50
        self.message.grid(row=4, column=2, padx=(self.padding_for_x, 0))
        # date
        self.date_label["text"] = "Current date"
        self.date_label.grid(row=5, column=2, padx=(self.padding_for_x, 0))
        self.news_date.insert(0, date.today().strftime("%d.%m.%Y"))
        self.news_date.grid(row=6, column=2, padx=(self.padding_for_x, 0))
        # button
        self.add_news["text"] = "Save"
        self.add_news["command"] = self.save_to_db
        self.add_news["bg"] = "green"
        self.add_news["fg"] = "white"
        self.add_news["padx"] = 10
        self.add_news["pady"] = 10
        self.add_news.grid(row=9, column=2, padx=(self.padding_for_x, 0))

    def fill_list_view(self, data):
        self.list_of_news.delete(0, tk.END)
        if data[0] == "error":
            self.create_alert(data[1])
        else:
            index = 0
            for new in data:
                self.list_of_news.insert(index, new)
                index += 1
            self.list_of_news.selection_set(first=0)

    def delete_trigger(self):
        deleting = askyesno("Deleting", "Are you sure you want to delete?", parent=self.master)
        if deleting:
            response = self.news_handler.delete_one(self.list_of_news.get(tk.ACTIVE))
            if response[0] == "error":
                self.create_alert(response[1])
            else:
                showinfo("Removed", "News item removed successfully", parent=self.master)
            self.fill_list_view(self.news_handler.get_news())

    def save_to_db(self):
        saving = askyesno("Saving", "Are you sure you want to save?", parent=self.master)
        if saving:
            data = {
                "headline": self.headline.get("1.0", "end-1c"),
                "message": self.message.get("1.0", "end-1c"),
                "date": self.news_date.get(),
                "locale": self.language_select.get()
            }
            response = self.news_handler.insert_new(data, self.language_select.get())
            if response[0] == "error":
                self.create_alert(response[1])
            else:
                showinfo("Saved", "Succesfully saved", parent=self.master)
                self.fill_list_view(self.news_handler.get_news())

    def create_alert(self, message):
        showerror("Error", message, parent=self.master)
