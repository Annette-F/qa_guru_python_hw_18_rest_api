from selene import browser, have
import requests
import allure
import pytest
from allure_commons.types import AttachmentType
from utils import attach
from dotenv import load_dotenv
import os

URL = 'https://demowebshop.tricentis.com'


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def authorization_with_api():
    with allure.step('Login with API'):
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        result_auth = requests.post(
            url=URL + '/login',
            data={'Email': {login}, 'Password': {password}, 'RememberMe': False},
            allow_redirects=False
        )
        allure.attach(body=result_auth.text, name='Response', attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=str(result_auth.cookies), name='Cookies', attachment_type=AttachmentType.TEXT,
                      extension='txt')
    with allure.step('Get cookie from API'):
        cookie = result_auth.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Set cookie from API'):
        browser.open(URL)
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open(URL)
        cookie = result_auth.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.text(login))

    return cookie


def add_product_to_cart(Add_product_to_cart, cookie):
    result_cart = requests.post(
        url=URL + Add_product_to_cart,
        cookies={'NOPCOMMERCE.AUTH': cookie}
    )
    allure.attach(body=result_cart.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
    allure.attach(body=str(result_cart.status_code), name='Response', attachment_type=AttachmentType.TEXT,
                  extension='.txt')
    allure.attach(body=str(result_cart.request.headers), name='Response', attachment_type=AttachmentType.TEXT,
                  extension='.txt')
    allure.attach(body=result_cart.url, name='Response', attachment_type=AttachmentType.TEXT,
                  extension='.txt')

    return result_cart.status_code


def clear_cart():
    browser.open('https://demowebshop.tricentis.com/cart')
    browser.element('.qty-input').set_value('0').press_enter()


@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    browser.config.base_url = URL
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
