import pytest
import requests
import allure
from config.settings import BASE_URL_API, API_KEY


@pytest.mark.api
@allure.feature("API тесты PoiskKino")
@allure.story("Позитивные и негативные сценарии")
class TestPoiskKinoAPI:

    HEADERS = {"X-API-KEY": API_KEY}

    @allure.title("Успешный поиск фильмов по году и жанру")
    @allure.story("Позитивные тесты")
    def test_search_movies_by_year_and_genre(self):
        response = requests.get(
            f"{BASE_URL_API}/movie",
            headers=self.HEADERS,
            params={
                "year": 2023,
                "genres.name": "+криминал"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) > 0

    @allure.title("Успешный поиск с фильтрацией по рейтингу (диапазон)")
    @allure.story("Позитивные тесты")
    def test_search_movies_by_rating_range(self):
        response = requests.get(
            f"{BASE_URL_API}/movie",
            headers=self.HEADERS,
            params={
                "rating.kp": "7-10",
                "limit": 3
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "docs" in data
        assert len(data["docs"]) <= 3

    @allure.title("Запрос без обязательного заголовка X-API-KEY")
    @allure.story("Негативные тесты")
    def test_no_api_key(self):
        response = requests.get(
            f"{BASE_URL_API}/movie",
            params={"year": 2023}
        )
        assert response.status_code == 401
        data = response.json()
        assert "message" in data
        assert "токен" in data["message"]

    @allure.title("Запрос информации о несуществующем фильме")
    @allure.story("Негативные тесты")
    def test_movie_not_found(self):
        response = requests.get(
            f"{BASE_URL_API}/movie/9999999",
            headers=self.HEADERS
        )
        assert response.status_code == 404
        data = response.json()
        assert "message" in data
        assert "ничего не найдено" in data["message"]

    @allure.title("Использование некорректного формата даты в параметре")
    @allure.story("Негативные тесты")
    def test_invalid_date_format(self):
        response = requests.get(
            f"{BASE_URL_API}/movie",
            headers=self.HEADERS,
            params={"premiere.russia": "2023-01-01"}
        )
        assert response.status_code == 400
