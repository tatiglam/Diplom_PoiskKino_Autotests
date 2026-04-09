import pytest
import allure
import requests
from config.settings import BASE_URL_API, API_KEY


@pytest.mark.api
@allure.feature("API тесты PoiskKino")
@allure.story("Позитивные и негативные сценарии")
class TestPoiskKinoAPI:

    HEADERS = {"X-API-Key": API_KEY} if API_KEY else {}

    @allure.title("GET /movie - получение списка фильмов с валидным ключом")
    def test_get_movies_success(self):
        with allure.step("Выполнить GET запрос /movie с валидным API-ключом"):
            url = f"{BASE_URL_API}/movie"
            response = requests.get(url, headers=self.HEADERS)

        with allure.step("Проверить, что статус-код равен 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что в ответе есть данные"):
            data = response.json()
            assert data is not None

    @allure.title("GET /movie - запрос без API-ключа")
    def test_get_movies_no_key(self):
        with allure.step("Выполнить GET запрос /movie без API-ключа"):
            url = f"{BASE_URL_API}/movie"
            response = requests.get(url)

        with allure.step("Проверить, что статус-код равен 401"):
            assert response.status_code == 401

    @allure.title("GET /movie - запрос с неверным API-ключом")
    def test_get_movies_invalid_key(self):
        with allure.step("Выполнить GET запрос /movie с неверным API-ключом"):
            url = f"{BASE_URL_API}/movie"
            headers = {"X-API-Key": "INVALID_KEY_123"}
            response = requests.get(url, headers=headers)

        with allure.step("Проверить, что статус-код равен 401"):
            assert response.status_code == 401

    @allure.title("GET /movie - проверка пагинации (limit=5)")
    def test_get_movies_pagination(self):
        with allure.step("Выполнить GET запрос /movie с параметром limit=5"):
            url = f"{BASE_URL_API}/movie"
            params = {"limit": 5}
            response = requests.get(url, headers=self.HEADERS, params=params)

        with allure.step("Проверить, что статус-код равен 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что вернулось не более 5 элементов"):
            data = response.json()
            if isinstance(data, list):
                assert len(data) <= 5

    @allure.title("GET /movie - поиск по году")
    def test_get_movies_by_year(self):
        with allure.step("Выполнить GET запрос /movie с параметром year=2024"):
            url = f"{BASE_URL_API}/movie"
            params = {"year": 2024}
            response = requests.get(url, headers=self.HEADERS, params=params)

        with allure.step("Проверить, что статус-код равен 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что данные получены"):
            data = response.json()
            assert data is not None
