from selene import browser
import requests
import allure
from allure_commons.types import AttachmentType
import os


def add_product_to_cart(Add_product_to_cart, cookie):
    result_cart = requests.post(
        url=os.getenv('URL') + Add_product_to_cart,
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
    browser.open(os.getenv('URL') + '/cart')
    browser.element('.qty-input').set_value('0').press_enter()
