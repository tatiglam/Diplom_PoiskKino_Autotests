# Diplom_PoiskKino_Autotests

## Проект
- **UI тесты (5 шт.)** — IMDb (themoviedb.org)
- **API тесты (5 шт.)** — PoiskKino API

## Установка и запуск
```bash
pip install -r requirements.txt

# Только UI тесты
pytest -m ui

# Только API тесты
pytest -m api

# Все тесты
pytest