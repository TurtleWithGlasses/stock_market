import customtkinter as ctk
from settings import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_COLOR)
        self.geometry("900x800")
        self.title("Stock Market")

        self.mainloop()

App()