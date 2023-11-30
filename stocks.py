import customtkinter as ctk
from settings import *
import yfinance as yf
from datetime import datetime

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=BG_COLOR)
        self.geometry("900x800")
        self.title("Stock Market")

        # data
        self.input_string = ctk.StringVar(value="AAPL")
        self.time_string = ctk.StringVar(value=TIME_OPTIONS[0])

        # widgets
        InputPanel(self,self.input_string,self.time_string)

        self.bind("<Return>",self.input_handler)

        self.mainloop()

    def input_handler(self,event=None):
            ticker = yf.Ticker(self.input_string.get())
            start = datetime(1959,1,1)
            end = datetime.today()

            self.max = ticker.history(start=start,end=end,period="1d")
            self.year = self.max.iloc[-260:]
            self.six_months = self.max.iloc[-130:]
            self.one_month = self.max.iloc[-22:]
            self.one_week = self.max.iloc[-5:]
            
            

class InputPanel(ctk.CTkFrame):
    def __init__(self,parent,input_string,time_string):
        super().__init__(parent,fg_color=INPUT_BG_COLOR,corner_radius=0)
        self.pack(fill="both",side="bottom")

        # widgets
        ctk.CTkEntry(self,
                     textvariable=input_string,
                     fg_color=BG_COLOR,
                     border_color=TEXT_COLOR,
                     border_width=1,
                     text_color="white").pack(side="left",padx=10,pady=10)
        
        self.buttons = [TextButton(self,text,time_string) for text in TIME_OPTIONS]

        time_string.trace("w",self.unselect_all_buttons)
    
    def unselect_all_buttons(self,*args):
        for button in self.buttons:
            button.unselect()

class TextButton(ctk.CTkLabel):
    def __init__(self,parent,text,time_string):
        super().__init__(parent,text=text,text_color=TEXT_COLOR)
        self.pack(side="right",padx=10,pady=10)

        self.bind("<Button>",self.select_handler)

        self.time_string = time_string
        self.text = text

        if time_string.get() == text:
            self.select_handler()
    
    def select_handler(self,event=None):
        self.time_string.set(self.text)
        self.configure(text_color=HIGHLIGHT_COLOR)
    
    def unselect(self):
        self.configure(text_color=TEXT_COLOR)


App()