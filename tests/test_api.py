import pytest
import requests
import allure
from config.settings import BASE_URL_API, API_KEY

@pytest.mark.api
@allure.feature("API тесты PoiskKino")
class TestPoiskKinoAPI:
    
    HEADERS = {"X-API-KEY": API_KEY}
    
    @allure.title("Успешный поиск фильмов по году и жанру")
    def test_search_movies_by_year_and_genre(self):
        """GET /movie?year=2023&genres.name=+криминал"""
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
    def test_search_movies_by_rating_range(self):
        """GET /movie?rating.kp=7-10&limit=3"""
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
    def test_no_api_key(self):
        """GET /movie?year=2023 без заголовка X-API-KEY"""
        response = requests.get(
            f"{BASE_URL_API}/movie",
            params={"year": 2023}
        )
        assert response.status_code == 401
        data = response.json()
        assert "message" in data
        assert "токен" in data["message"]
    
    @allure.title("Запрос информации о несуществующем фильме")
    def test_movie_not_found(self):
        """GET /movie/9999999"""
        response = requests.get(
            f"{BASE_URL_API}/movie/9999999",
            headers=self.HEADERS
        )
        assert response.status_code == 404
        data = response.json()
        assert "message" in data
        assert "ничего не найдено" in data["message"]
    
    @allure.title("Использование некорректного формата даты в параметре")
    def test_invalid_date_format(self):
        """GET /movie?premiere.russia=2023-01-01"""
        response = requests.get(
            f"{BASE_URL_API}/movie",
            headers=self.HEADERS,
            params={"premiere.russia": "2023-01-01"}
        )
        assert response.status_code == 400
