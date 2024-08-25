from selene import browser, have
import requests
import allure
from allure_commons.types import AttachmentType
import os


def authorization_with_api():
    with allure.step('Login with API'):
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        result_auth = requests.post(
            url=os.getenv('URL') + '/login',
            data={'Email': {login}, 'Password': {password}, 'RememberMe': False},
            allow_redirects=False
        )
        assert result_auth
        allure.attach(body=result_auth.text, name='Response', attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=str(result_auth.cookies), name='Cookies', attachment_type=AttachmentType.TEXT,
                      extension='txt')
    with allure.step('Get cookie from API'):
        cookie = result_auth.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Set cookie from API'):
        browser.open(os.getenv('URL'))
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open(os.getenv('URL'))
        cookie = result_auth.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Verify successful authorization'):
        browser.element('.account').should(have.text(login))

    return cookie