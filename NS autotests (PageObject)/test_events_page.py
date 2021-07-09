from pages.main_page import MainPage
from pages.events_page import EventsPage
import time

def test_elements_events_page(browser):
    url_login = "https://nsstage.skillbox.ru/#/login?redirect=%2Fcampaigns%2Findex"
    page_home = MainPage(browser, url_login) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_home.open()  # открываем страницу авторизации
    page_home.go_to_campaigns_page() # выполняем метод страницы — переходим на страницу кампаний
    url_events = "https://nsstage.skillbox.ru/#/events/index"
    page_events = EventsPage(browser, url_events) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
    page_events.open() # открываем страницу событий
    page_events.assert_event_name() # проверяем, что на странице присутствует фильтр "Название"
    page_events.assert_status() # проверяем, что на странице присутствует фильтр по статусу
    page_events.assert_filter_id() # проверяем, что на странице присутствует фильтр по id
    page_events.assert_button() # проверяем, что на странице присутствует кнопка "Добавить"
    page_events.assert_table() # проверяем, что на странице присутствует таблица
    time.sleep(3)