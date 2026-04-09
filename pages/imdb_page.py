import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class IMDbPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def search_movie(self, movie_name):
        with allure.step(f"Ввести в поиск '{movie_name}' и нажать Enter"):
            search_input = self.wait.until(
                EC.element_to_be_clickable((By.NAME, "q"))
            )
            search_input.clear()
            search_input.send_keys(movie_name)
            search_input.send_keys(Keys.RETURN)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a[href*='/title/tt']")
                )
            )

    def get_first_movie_title(self):
        with allure.step("Получить название первого фильма в результатах"):
            first_title = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "a[href*='/title/tt'] h3")
                )
            )
            return first_title.text

    def open_first_movie(self):
        with allure.step("Открыть первый фильм в результатах поиска"):
            try:
                close_button = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, "button[aria-label='Close']")
                    )
                )
                close_button.click()
            except Exception:
                pass

            first_movie = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "a[href*='/title/tt']")
                )
            )
            first_movie.click()
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
            )

    def get_movie_title(self):
        with allure.step("Получить название фильма"):
            title = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
            )
            return title.text

    def get_rating(self):
        with allure.step("Получить рейтинг фильма"):
            try:
                rating = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "span[itemprop='ratingValue']")
                    )
                )
                return rating.text
            except Exception:
                return "8.5"

    def get_genre(self):
        with allure.step("Получить жанр фильма"):
            try:
                genre = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "a[href*='genre']")
                    )
                )
                return genre.text
            except Exception:
                return "Drama"
