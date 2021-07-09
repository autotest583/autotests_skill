from selenium.webdriver.common.by import By

class MainPageLocators(): # класс описывает локаторы страницы авторизации
    login_button = (By.CSS_SELECTOR, 'button[class="el-button el-button--primary el-button--medium"]') # кнопка "Login"

class EventsPageLocators(): # класс описывает локаторы страницы "События"
    event_name = (By.CSS_SELECTOR, 'input[placeholder="Название"]') # фильтр "Название"
    status = (By.CSS_SELECTOR, 'input[placeholder="Статус"]') # фильтр "Статус"
    filter_id = (By.CSS_SELECTOR, 'span[class="el-checkbox__input"]') # фильтр "ID"
    add_button = (By.CSS_SELECTOR, 'button[class="el-button filter-item el-button--primary el-button--medium"]') # кнопка "Добавить"
    table = (By.CSS_SELECTOR,
             'div[class="el-table el-table--fit el-table--border el-table--enable-row-hover '
             'el-table--enable-row-transition el-table--medium"]') # таблица