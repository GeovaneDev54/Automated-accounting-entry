from selenium.webdriver import ChromeOptions, ChromeService, Chrome
from selenium.webdriver import EdgeOptions, EdgeService, Edge
from selenium.webdriver import IeOptions, IeService, Ie
from selenium.webdriver import FirefoxOptions, FirefoxService, Firefox

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def select_browser(browser:str='chrome'):
    if browser == 'chrome':
        return {'options': ChromeOptions, 'service': ChromeService, 'webdriver': ChromeDriverManager, 'driver': Chrome}
    elif browser == 'edge':
        return {'options': EdgeOptions, 'service': EdgeService, 'webdriver': EdgeChromiumDriverManager, 'driver': Edge}
    elif browser == 'ie':
        return {'options': IeOptions, 'service': IeService, 'webdriver': IEDriverManager, 'driver': Ie}
    elif browser == 'firefox':
        return {'options': FirefoxOptions, 'service': FirefoxService, 'webdriver': GeckoDriverManager, 'driver': Firefox}

class Bot:
    def __init__(self, browser:str='chrome', *options:str):
        self.browser = select_browser(browser)
        self.webdriver = self.browser['webdriver']()
        self.options = self.browser['options']()

        for option in options:
            self.options.add_argument(option)

        self.service = self.browser['service'](self.webdriver.install())
        self.driver = self.browser['driver'](self.options, self.service)

    def open_url(self, url:str='https://cadastro-produtos-devaprender.netlify.app/'):
        self.driver.get(url)

    def step_1(self, name:str, description:str, category:str, code:str, weight:str|int|float, dimensions:str):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'product_name'))).send_keys(name)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'description'))).send_keys(description)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'category'))).send_keys(category)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'product_code'))).send_keys(code)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'weight'))).send_keys(weight)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'dimensions'))).send_keys(dimensions)

    def step_2(self, price:str|int|float, stock:str|int, expiration_date:str, color:str, size:str, material:str):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'price'))).send_keys(price)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'stock'))).send_keys(stock)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'expiry_date'))).send_keys(expiration_date)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'color'))).send_keys(color)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'size'))).send_keys(size)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'material'))).send_keys(material)

    def step_3(self, manufacturer:str, country:str, remarks:str, barcode:str|int, warehouse_location:str):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'manufacturer'))).send_keys(manufacturer)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'country'))).send_keys(country)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'remarks'))).send_keys(remarks)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'barcode'))).send_keys(barcode)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, 'warehouse_location'))).send_keys(warehouse_location)

    def register_product(self, name:str, description:str, category:str, code:str, weight:str|int|float, dimensions:str, price:str|int|float, stock:str|int, expiration_date:str, color:str, size:str, material:str, manufacturer:str, country:str, remarks:str, barcode:str|int, warehouse_location:str):
        try:
            self.step_1(name, description, category, code, weight, dimensions)
            self.next()

            self.step_2(price, stock, expiration_date, color, size, material)
            self.next()

            self.step_3(manufacturer, country, remarks, barcode, warehouse_location)
            self.register()
        except TimeoutException as error:
            print('Você está sem internet ou sua internet está muito lenta.')

    def next(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Próximo"]'))).click()

    def register(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//button[text()="Concluir"]'))).click()
        WebDriverWait(self.driver, 30).until(EC.alert_is_present()).accept()
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary'))).click()

    def quit(self):
        self.driver.quit()