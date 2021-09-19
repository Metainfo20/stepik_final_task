from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.NAME, "login-username")
    LOGIN_PASS = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REGISTER_EMAIL = (By.NAME, "registration-email")
    REGISTER_PASS = (By.NAME, "registration-password1")
    REGISTER_PASS_COMFIRM = (By.NAME, "registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    
