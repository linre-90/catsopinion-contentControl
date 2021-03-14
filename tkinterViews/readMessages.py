import ast
import json
import tkinter as tk
import message as mg
from tkinter.messagebox import showerror, showinfo, askyesno


class ReadMessages(tk.Frame):
    def __init__(self, master=None):
        self.message_handler = mg.Message()
        super().__init__(master)
        self.scroll = tk.Scrollbar(self, orient="vertical")
        self.scroll_hor = tk.Scrollbar(self, orient="horizontal")
        self.scroll.pack(side="right", fill="y")
        self.scroll_hor.pack(side="bottom", fill="x")
        self.list = tk.Listbox(self, height=20, width=100, font=("Times", 12))
        self.populate_messages_listbox()
        self.master = master
        self.scroll.config(command=self.list.yview)
        self.scroll_hor.config(command=self.list.xview)
        self.delete_btn = tk.Button(self, bg="red", text="Delete", padx=5, pady=5, command=self.delete_message)
        self.read_btn = tk.Button(self, text="Read message", padx=5, pady=5, command=self.read_message)
        self.list.pack()
        self.delete_btn.pack()
        self.read_btn.pack()
        self.pack()
        self.winfo_toplevel().title("Cats opinion admin panel - Messages")

    def populate_messages_listbox(self):
        self.list.delete(0, tk.END)
        index = 0
        for message in self.message_handler.get_messages():
            self.list.insert(index, message)
            index += 1
            self.list.insert(index, "----*****----")
            index += 1

    def delete_message(self):
        are_you_sure = askyesno("Confirmation", "Are you sure you want to delete?", parent=self.master)
        if are_you_sure:
            try:
                response = self.message_handler.delete_message_from_db(ast.literal_eval(self.list.get(tk.ACTIVE))["uid"])
                if response[0] == "error":
                    showerror("Error", "unable to delete", parent=self.master)
                elif response[0] == "ok":
                    showinfo("Deleted", "Entry removed", parent=self.master)
                self.populate_messages_listbox()
            except SyntaxError:
                showerror("Error", "message you are deleting is decoration!", parent=self.master)

    def read_message(self):
        dic_message = ast.literal_eval(self.list.get(tk.ACTIVE))
        info_header = "Headline: "+dic_message["headline"]
        info_message = "type: "  + dic_message["type"] + "\n\n" +"Message: " + dic_message["message"] + "\n\n" + "Sender: " + dic_message["email"] + "\n\n" + "id: " + dic_message["uid"]
        showinfo(info_header, info_message, parent=self.master)
