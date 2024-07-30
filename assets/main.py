import customtkinter as ctk
from utils.file import File
from utils.bot import Bot

class GUI(ctk.CTk):
    def __init__(self, width:int=500, height:int=500):
        super().__init__()
        x = int((self.winfo_screenwidth() - width) / 2)
        y = int((self.winfo_screenheight() - height) / 2)

        self.title('Automated Accounting Entry')
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(False, False)

    def start(self):
        self.mainloop()



if __name__ == '__main__':
    main = GUI()
    main.start()