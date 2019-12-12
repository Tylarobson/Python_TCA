from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        self.title("Currency Converter")
        self.configure(bg="#ffe8e8", height=220, width =360, pady=10)
        
        self.__add_outer_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_amount_entry()
        self.__add_clear_button()
        self.__add_convert_button()

    def __add_outer_frame(self):
        self.outer_frame = Frame()
        self.outer_frame.grid(row=0, column=0)

    def __add_heading_label(self):
        self.heading_label = Label(self.outer_frame)
        self.heading_label.grid(row=0, column=0,columnspan=2)
        self.heading_label.configure(  bg="#eee", 
                                        font="Arial 14",
                                        justify=RIGHT,
                                        text="Currency Converter")
        
    def __add_instruction_label(self):
        self.instruction_label = Label(self.outer_frame)
        self.instruction_label.grid(row=1, column=0,columnspan=2, sticky=W)
        self.instruction_label.configure (bg="#eee",
                                            pady=10,
                                            text="Amount")

    def __add_amount_entry(self):
        self.amount_entry = Entry(self.outer_frame)
        self.amount_entry.grid(row=2, column=0, columnspan=2)
        self.amount_entry.configure(width=30)
        
    def __add_clear_button(self):
        self.clear_button = Button(self.outer_frame)
        self.clear_button.grid(row=3, column=0, sticky=E)
        self.clear_button.configure(bg="#fee", 
                                            text="Clear",
                                            width=10)

    def __add_convert_button(self):
        self.convert_button = Button(self.outer_frame)
        self.convert_button.grid(row=3, column=1, sticky=W)
        self.convert_button.configure(bg="#fee", 
                                            text="Convert",
                                            width=10)


my_gui = Gui()
my_gui.mainloop()