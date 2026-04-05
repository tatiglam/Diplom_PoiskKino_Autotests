import pytest
import allure
from pages.imdb_page import IMDbPage

@pytest.mark.ui
@allure.feature("UI тесты IMDb")
class TestIMDbUI:
    
    @allure.title("Поиск фильма по названию")
    def test_search_movie(self, driver):
        driver.get("https://www.imdb.com")
        page = IMDbPage(driver)
        page.search_movie("Inception")
        assert "Inception" in driver.page_source
    
    @allure.title("Открытие карточки фильма из поиска")
    def test_open_movie_card(self, driver):
        driver.get("https://www.imdb.com")
        page = IMDbPage(driver)
        page.search_movie("The Matrix")
        page.open_first_movie()
        title = page.get_movie_title()
        assert "Matrix" in title or "Матрица" in title
    
    @allure.title("Проверка наличия рейтинга")
    def test_movie_rating_exists(self, driver):
        driver.get("https://www.imdb.com")
        page = IMDbPage(driver)
        page.search_movie("The Shawshank Redemption")
        page.open_first_movie()
        rating = page.get_rating()
        assert rating is not None and rating != ""
    
    @allure.title("Поиск фильма по году выпуска")
    def test_search_by_year(self, driver):
        driver.get("https://www.imdb.com")
        page = IMDbPage(driver)
        page.search_movie("1994")
        assert "1994" in driver.page_source
    
    @allure.title("Проверка жанра фильма")
    def test_movie_genre_exists(self, driver):
        driver.get("https://www.imdb.com")
        page = IMDbPage(driver)
        page.search_movie("The Godfather")
        page.open_first_movie()
        assert "Drama" in driver.page_source or "драма" in driver.page_source
