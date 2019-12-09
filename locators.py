from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    SEARCH_INPUT = (By.ID, "id_q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.btn")

class LoginPageLocators():
     email_input = (By.CSS_SELECTOR, 'input[name="registration-email"]')
     pass_input = (By.ID, 'id_registration-password1')
     pass_second_input = (By.ID, 'id_registration-password2')
     submit_button = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')
     successful_msg = (By.CSS_SELECTOR, 'div.alertinner')
