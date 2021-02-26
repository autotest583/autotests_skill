from selenium import webdriver
import time

try:
    browser = webdriver.Safari()
    browser.maximize_window()
    browser.implicitly_wait(3)

    # переход к стенду stage
    browser.get("https://gostage.skillbox.ru")

    # авторизация в LMS
    browser.find_element_by_css_selector('svg-icon[name="close"]').click()
    email = browser.find_element_by_css_selector('input[inputmode="email"]')
    email.send_keys("testcontent10@skillbox.ru")
    password = browser.find_element_by_css_selector('input[type="password"]')
    password.send_keys("1234567m")
    browser.find_element_by_tag_name('button').click()

    # переход к разделу Сертификаты и Дипломы
    caption = browser.find_element_by_link_text('Мое обучение')
    assert "Мое обучение" in caption.text
    caption2 = browser.find_element_by_css_selector('a[data-e2e="quick-menu__staff"]')
    assert "Для персонала" in caption2.text
    caption2.click()
    browser.find_element_by_link_text('Контент').click()
    browser.find_element_by_link_text('Сертификаты и дипломы').click()

    # создание шаблона диплома
    browser.find_element_by_link_text('Дипломы').click()
    browser.find_element_by_xpath("//button[contains(text(),'Создать шаблон диплома')]").click()
    course = browser.find_element_by_css_selector('input[data-placeholder="Начните вводить название"]')
    course.send_keys("Дипломный проект Sound-дизайн")
    browser.find_element_by_xpath("//span[contains(text(),'Дипломный проект Sound-дизайн')]").click()
    editor = browser.find_element_by_class_name('editor')
    editor.click()
    editor.send_keys("mxcvnxcv")
    browser.find_element_by_xpath("//button[contains(text(),'Сохранить')]").click()
    popup = browser.find_element_by_xpath("//*[contains(text(),'Изменения успешно сохранены!')]")
    assert "Изменения успешно сохранены!" in popup.text

finally:
    browser.quit()