from selenium.common.exceptions import NoSuchElementException

class BasePage(): # метод-конструктор, который вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=4):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what): # метод реализует перехват исключения
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self): # метод реализует открытие страницы
        self.browser.get(self.url)