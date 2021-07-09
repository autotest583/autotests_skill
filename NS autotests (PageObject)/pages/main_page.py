from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators

class MainPage(BasePage):
    def go_to_campaigns_page(self): # метод реализует авторизацию и переход к странице "Кампании"
        login = self.browser.find_element(*MainPageLocators.login_button)
        login.click()