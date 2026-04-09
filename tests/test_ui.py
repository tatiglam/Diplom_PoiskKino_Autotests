import pytest
import allure
from pages.imdb_page import IMDbPage


@pytest.mark.ui
@allure.feature("UI тесты IMDb")
@allure.story("Поиск и карточки фильмов")
class TestIMDbUI:

    @allure.title("Поиск фильма по названию")
    def test_search_movie(self, driver):
        with allure.step("Открыть главную страницу IMDb"):
            driver.get("https://www.imdb.com")

        page = IMDbPage(driver)

        with allure.step("Выполнить поиск фильма 'Inception'"):
            page.search_movie("Inception")

        with allure.step(
            "Проверить, что в результатах есть фильм 'Inception'"
        ):
            first_title = page.get_first_movie_title()
            assert "Inception" in first_title or \
                   "Начало" in first_title

    @allure.title("Открытие карточки фильма из поиска")
    def test_open_movie_card(self, driver):
        with allure.step("Открыть главную страницу IMDb"):
            driver.get("https://www.imdb.com")

        page = IMDbPage(driver)

        with allure.step("Выполнить поиск фильма 'The Matrix'"):
            page.search_movie("The Matrix")

        with allure.step("Открыть первый фильм в результатах"):
            page.open_first_movie()

        with allure.step("Проверить название открытого фильма"):
            title = page.get_movie_title()
            assert "Matrix" in title or "Матрица" in title

    @allure.title("Проверка наличия рейтинга")
    def test_movie_rating_exists(self, driver):
        with allure.step("Открыть главную страницу IMDb"):
            driver.get("https://www.imdb.com")

        page = IMDbPage(driver)

        with allure.step(
            "Выполнить поиск фильма 'The Shawshank Redemption'"
        ):
            page.search_movie("The Shawshank Redemption")

        with allure.step("Открыть первый фильм в результатах"):
            page.open_first_movie()

        with allure.step("Получить рейтинг фильма"):
            rating = page.get_rating()

        with allure.step("Проверить, что рейтинг не пустой"):
            assert rating is not None and rating != ""

    @allure.title("Поиск фильма по году выпуска")
    def test_search_by_year(self, driver):
        with allure.step("Открыть главную страницу IMDb"):
            driver.get("https://www.imdb.com")

        page = IMDbPage(driver)

        with allure.step("Выполнить поиск по году '1994'"):
            page.search_movie("1994")

        with allure.step(
            "Проверить, что результаты поиска загрузились"
        ):
            first_title = page.get_first_movie_title()
            assert first_title is not None

    @allure.title("Проверка жанра фильма")
    def test_movie_genre_exists(self, driver):
        with allure.step("Открыть главную страницу IMDb"):
            driver.get("https://www.imdb.com")

        page = IMDbPage(driver)

        with allure.step("Выполнить поиск фильма 'The Godfather'"):
            page.search_movie("The Godfather")

        with allure.step("Открыть первый фильм в результатах"):
            page.open_first_movie()

        with allure.step(
            "Проверить наличие жанра 'Drama' на странице"
        ):
            genre = page.get_genre()
            assert "Drama" in genre or "драма" in genre
