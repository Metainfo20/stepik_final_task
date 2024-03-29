from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "col-sm-6.login_form")
    REGISTER_FORM = (By.CLASS_NAME, "col-sm-6.register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    BASKET = (By.CLASS_NAME, "not_exist")
