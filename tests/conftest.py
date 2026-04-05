import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(60)  # Увеличил таймаут загрузки страницы
    driver.implicitly_wait(30)  # Неявное ожидание элементов
    
    yield driver
    driver.quit()
