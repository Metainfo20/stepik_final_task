from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def can_add_product_to_basket(self):
        self.should_be_add_to_backet_button()
        self.should_be_add_product_to_backet()
        #self.should_be_register_form()
        self.solve_quiz()


    def should_be_add_to_backet_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to backet button is not presented"


    def should_be_add_product_to_backet(self):
        add_to_backet = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_backet.click()


    def solve_quiz(self):
        BasePage.solve_quiz_and_get_code(self)