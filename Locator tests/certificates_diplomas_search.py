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

    # проверка поиска во вкладке Дипломы
    browser.find_element_by_link_text('Дипломы').click()
    search = browser.find_element_by_css_selector('input[inputmode="text"]')
    search.send_keys("saf")
    msg = browser.find_element_by_xpath("//span[contains(text(),'Сертификаты не найдены')]")
    assert "Сертификаты не найдены" in msg.text
    search.clear()
    search.send_keys("НТВ")
    crs = browser.find_element_by_xpath("//*[contains(text(),'Дипломный проект «НТВ ПЛЮС»')]")
    assert "Дипломный проект «НТВ ПЛЮС»" in crs.text
    search.clear()
    search.send_keys("sdkcnvbfhrgkldnfksdnfksndflknsdklfnlks"
                     "dnfklsndflksdnfsdlbvsdjbjsdbvsdbvsjewfwefwefwefwefw"
                     "efweklfweklfnlkwenffd"
                     "vbsdjvbjksdbvjksdvewkfklwenfklwnekfnwklenfklen"
                     "fklwenfklnweklfnklwenfklwenfklnweklfn"
                     "weklnfklwekwengkwnelgknwlekgnwlekgnlwkegnlkwegnkwen"
                     "gklwengklweg")
    err = browser.find_element_by_xpath("//*[contains(text(),'Не более 255 символов')]")
    assert "Не более 255 символов" in err.text

finally:
    browser.quit()