from selene import browser
import requests
import allure
from allure_commons.types import AttachmentType
import os
import logging


def add_product_to_cart(Add_product_to_cart, cookie):
    response = requests.post(
        url=os.getenv('URL') + Add_product_to_cart,
        cookies={'NOPCOMMERCE.AUTH': cookie}
    )
    allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
    logging.info(response.status_code)
    logging.info(response.text)

    return response.status_code


def clear_cart():
    browser.open(os.getenv('URL') + '/cart')
    browser.element('.qty-input').set_value('0').press_enter()
