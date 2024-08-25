from selene import browser, have
from selene.support.conditions import have
import allure
from allure_commons.types import Severity
from utils.authoriaztion import authorization_with_api
from utils.cart import add_product_to_cart, clear_cart


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Add product to empty cart')
@allure.story('Cart')
@allure.link('https://demowebshop.tricentis.com', name='demowebshop')
def test_add_product_to_cart():
    with allure.step('Authorization from API'):
        cookie = authorization_with_api()
    with allure.step('Open main page Demowebshop'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('/')
    with allure.step('Add product to cart from API'):
        result_cart = add_product_to_cart(Add_product_to_cart='/addproducttocart/catalog/31/1/1', cookie=cookie)
    with allure.step('Verify cart'):
        browser.element('.ico-cart .cart-label').click()
        browser.element('.product-name').should(have.text('14.1-inch Laptop'))
    with allure.step('Clear cart'):
        clear_cart()


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Annette-F')
@allure.feature('Add digital downloads to cart')
@allure.story('Cart')
@allure.link('https://demowebshop.tricentis.com', name='demowebshop')
def test_add_digital_downloads_to_cart():
    with allure.step('Authorization from API'):
        cookie = authorization_with_api()
    with allure.step('Open main page Demowebshop'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open('/')
    with allure.step('Add product to cart from API'):
        result_cart = add_product_to_cart(Add_product_to_cart='/addproducttocart/catalog/52/1/1', cookie=cookie)
    with allure.step('Verify cart'):
        browser.element('.ico-cart .cart-label').click()
        browser.element('.product-name').should(have.text('Music 2'))
    with allure.step('Clear cart'):
        clear_cart()