from selenium import webdriver
import random
from login_page import LoginPage

def test_new_user_with_unique_email_can_register(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/";
    main_page = LoginPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    random_number = str(random.random())
    email = 'aaa' + random_number + '@aaa.aa'
    password = 'secret123!'
    login_page.registration(email, password)
    login_page.should_be_successful_message()




