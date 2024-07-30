import openpyxl

class File:
    def __init__(self, file:str):
        self.products = {}
        self.workbook = openpyxl.load_workbook(file)
        self.sheet_products = self.workbook['Produtos']

    def get_products(self):
        for row in self.sheet_products.iter_rows(min_row=2):
            product = []

            for column in range(0, 17):
                product.append(row[column].value)
                self.products[column] = product

        return self.products