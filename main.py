import firebaseapp
import tkinter as tk
from tkinterViews import mainWindow as mainWindow


firebaseapp.FirebaseWizard()
root = tk.Tk()
root.geometry("1280x720")
app = mainWindow.Application(master=root)
app.mainloop()
