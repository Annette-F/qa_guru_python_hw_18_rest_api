from selene import browser
import pytest
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setting_browser(request):
    browser.config.base_url = os.getenv('URL')
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
