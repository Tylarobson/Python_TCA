from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.configure(bg="#fffbce, height=220, width =360, pady=10)
        
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_amount_entry()
        self.__add_clear_button()
        self.__add_convert_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.place (x=10, y=10, relheight = 0.84, relwidth=0.94)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.place(x=10, y=43)
        self.heading_label.configure(  bg="#eee", 
                                        font="Arial 14", 
                                        text="Currency Converter")
        
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.place(x=10, y=43)
        self.instruction_label.configure (bg="#eee",
                                            justify=LEFT,
                                            pady=10,
                                            text="Amount")

    def __add_amount_entry(self):
        self.amount_entry = Entry(self.outer_frame)
        self.amount_entry.place(x=60, y=102)
        self.amount_entry.configure(width=30)
        
    def __add_clear_button(self):
        self.clear_button = Button(self.outer_frame)
        self.convert_button.grid(x=0, y=140)
        self.subscribe_button.configure(bg="#fee", 
                                            text="Clear",
                                            width=47)

    def __add_convert_button(self):
        self.convert_button = Button(self.outer_frame)
        self.convert_button.grid(x=0, y=140)
        self.subscribe_button.configure(bg="#fee", 
                                            text="Convert",
                                            width=47)