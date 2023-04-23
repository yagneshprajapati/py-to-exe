import tkinter as tk
from tkinter import filedialog
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

        
        
        
    def create_widgets(self):
        self.select_file_button = tk.Button(self)
        self.select_file_button["text"] = "Select Python File"
        self.select_file_button["command"] = self.select_file
        self.select_file_button.pack(side="top")

        self.convert_button = tk.Button(self)
        self.convert_button["text"] = "Convert to Executable"
        self.convert_button["command"] = self.convert_file
        self.convert_button.pack(side="bottom")

        self.quit_button = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit_button.pack(side="bottom")

        
        
    def select_file(self):
        self.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Python files","*.py"),("all files","*.*")))
        print(self.filename)

    def convert_file(self):
        if hasattr(self, 'filename'):
            os.system(f'pyinstaller --onefile "{self.filename}"')
            print("File converted to executable")
        else:
            print("Please select a Python file first")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
