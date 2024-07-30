import customtkinter as ctk
from customtkinter import filedialog
from utils.file import File
from utils.bot import Bot
import sys

class GUI(ctk.CTk):
    def __init__(self, width:int=350, height:int=325):
        super().__init__()
        self.filename = None
        self.browser = 'chrome'
        self.file = None
        self.bot = None
        x = int((self.winfo_screenwidth() - width) / 2)
        y = int((self.winfo_screenheight() - height) / 2)

        self.title('Automated Accounting Entry')
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.resizable(False, False)

    def get_filename(self):
        self.filename = filedialog.askopenfilename()

    def get_browser_selected(self):
        self.browser = self.browser_var.get()

    def submit(self):
        if self.filename is not None:
            self.file = File(self.filename)
            self.bot = Bot(self.browser, '--headless')
            products = self.file.get_products()

            for product in products.values():
                self.bot.open_url()
                self.bot.register_product(*product)
            self.bot.quit()
            self.quit()
            sys.exit()

    def header(self):
        self.title = ctk.CTkLabel(self, 500, text='Automated Accounting Entry', font=('Arial Black', 24))
        self.title.pack(pady=3)

    def body(self):
        ctk.CTkLabel(self, text='Select your browser:', font=('Arial', 16)).pack()

        self.browser_var = ctk.StringVar(self, 'chrome')
        ctk.CTkRadioButton(self, text='Chrome', variable=self.browser_var, value='chrome', command=self.get_browser_selected).pack(pady=3)
        ctk.CTkRadioButton(self, text='Edge', variable=self.browser_var, value='edge', command=self.get_browser_selected).pack()
        ctk.CTkRadioButton(self, text='Ie', variable=self.browser_var, value='ie', command=self.get_browser_selected).pack(pady=3)
        ctk.CTkRadioButton(self, text='Firefox', variable=self.browser_var, value='firefox', command=self.get_browser_selected).pack()

        ctk.CTkButton(self, 250, 50, text='Select file', font=('Arial', 24), command=self.get_filename).pack(pady=10)
        ctk.CTkButton(self, 250, 50, text='Submit', font=('Arial', 24), command=self.submit).pack()

    def footer(self):
        ctk.CTkLabel(self, text='By: GeovaneDev54', font=('Arial Black', 16)).pack(pady=10)

    def start(self):
        self.header()
        self.body()
        self.footer()
        self.mainloop()



if __name__ == '__main__':
    main = GUI()
    main.start()