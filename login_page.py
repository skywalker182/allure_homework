from base_page import BasePage
from locators import LoginPageLocators, MainPageLocators

class LoginPage(BasePage):
    def registration(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.email_input)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.pass_input)
        pass_input.send_keys(password)
        pass_input = self.browser.find_element(*LoginPageLocators.pass_second_input)
        pass_input.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.submit_button)
        submit_button.click()

    def should_be_successful_message(self):
        success = self.browser.find_element(*LoginPageLocators.successful_msg).text
        assert success == 'Спасибо за регистрацию!'

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()