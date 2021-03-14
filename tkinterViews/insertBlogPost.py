import tkinter as tk
import tkinter.ttk as tt
import blog as blg
from tkinter.messagebox import askyesno


class InsertBlog(tk.Frame):
    def __init__(self, master=None):
        self.blog_handler = blg.Blog()
        super().__init__(master)
        # languages
        self.languages = ["fi", "en"]
        self.selected = tk.StringVar()
        self.language_label = tk.Label(self)
        self.language_select = tt.Combobox(self, textvariable=self.selected, values=self.languages)
        self.build_language_field()
        # date
        self.date_label = tk.Label(self)
        self.date_input = tk.Text(self)
        self.build_date_fields()
        # description
        self.description_label = tk.Label(self)
        self.description_input = tk.Text(self)
        self.build_description_fields()
        # series
        self.series_selected = tk.StringVar()
        self.series_selected.set(self.blog_handler.get_series()[0])
        self.series_label = tk.Label(self)
        self.series_select = tt.Combobox(self, textvariable=self.series_selected, values=self.blog_handler.get_series())
        self.build_series_field()
        # header img
        self.headerIMG_label = tk.Label(self)
        self.headerIMG_input = tk.Text(self)
        self.build_headerIMG_fields()
        # title
        self.title_label = tk.Label(self)
        self.title_input = tk.Text(self)
        self.build_title_fields()
        # view
        self.view_label = tk.Label(self)
        self.view_input = tk.Text(self)
        self.build_view_fields()
        # save
        self.save_btn = tk.Button(self)
        self.build_save_button()
        # master
        self.master = master
        self.pack()
        self.winfo_toplevel().title("Cats opinion admin panel - Insert blog post")

    def build_language_field(self):
        self.selected.set(self.languages[0])
        self.language_label["text"] = "Select language"
        self.language_label.pack()
        self.language_select.pack()

    def build_date_fields(self):
        self.date_label["text"] = "Insert date: (format: dd/mm/yyyy)"
        self.date_input["wrap"] = "none"
        self.date_input["height"] = 1
        self.date_label.pack()
        self.date_input.pack()

    def build_description_fields(self):
        self.description_label["text"] = "Enter description:"
        self.description_input["height"] = 3
        self.description_label.pack()
        self.description_input.pack()

    def build_series_field(self):

        self.series_label["text"] = "Select series"
        self.series_label.pack()
        self.series_select.pack()

    def build_headerIMG_fields(self):
        self.headerIMG_label["text"] = "Insert header img url:"
        self.headerIMG_input["height"] = 1
        self.headerIMG_label.pack()
        self.headerIMG_input.pack()

    def build_title_fields(self):
        self.title_label["text"] = "Insert title:"
        self.title_input["height"] = 2
        self.title_label.pack()
        self.title_input.pack()

    def build_view_fields(self):
        self.view_label["text"] = "Insert view (html):"
        self.view_input["height"] = 2
        self.view_label.pack()
        self.view_input.pack()

    def build_save_button(self):
        self.save_btn["text"] = "Save"
        self.save_btn["bg"] = "green"
        self.save_btn["command"] = self.trigger_saving
        self.save_btn.pack()

    def trigger_saving(self):
        saving = askyesno("Saving", "Are you sure you want to save new blog post?", parent=self.master)
        if saving:
            data = {
                "date": self.date_input.get("1.0", "end-1c"),
                "description": self.description_input.get("1.0", "end-1c"),
                "dislikes": 0,
                "headerIMG": self.headerIMG_input.get("1.0", "end-1c"),
                "likes": 0,
                "locale": self.language_select.get(),
                "series": self.series_select.get(),
                "title": self.title_input.get("1.0", "end-1c"),
                "view": self.view_input.get("1.0", "end-1c")
            }
            self.blog_handler.save_blog_post(data, self.language_select.get())
