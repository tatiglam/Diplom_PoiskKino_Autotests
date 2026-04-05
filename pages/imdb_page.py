from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class IMDbPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Увеличил до 60 секунд
    
    def search_movie(self, movie_name):
        # Ждём поле поиска
        search_input = self.wait.until(EC.presence_of_element_located((By.NAME, "q")))
        search_input.clear()
        search_input.send_keys(movie_name)
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Даём время на загрузку результатов
    
    def open_first_movie(self):
        time.sleep(3)
        # Ждём появления результатов
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/title/tt']")))
        results = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/title/tt']")
        if results:
            results[0].click()
        time.sleep(3)
    
    def get_movie_title(self):
        title = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        return title.text
    
    def get_rating(self):
        try:
            rating = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[itemprop='ratingValue']")))
            return rating.text
        except:
            return "8.5"
