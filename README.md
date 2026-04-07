# Diplom_PoiskKino_Autotests

## О проекте

Проект содержит автоматизированные тесты для PoiskKino API (аналог Кинопоиска) и UI-тесты для страницы документации https://api.poiskkino.dev.

Стек: Python + pytest + Selenium + requests + Allure.

Проект создан на основе финальной работы по ручному тестированию «От Кинопоиска к PoiskKino API». В ручной работе тестировался только API. В этой дипломной работе добавлены UI-тесты на страницу документации PoiskKino.

## Установка и настройка

1. Клонировать репозиторий:

   git clone https://github.com/tatiglam/Diplom_PoiskKino_Autotests.git
   cd Diplom_PoiskKino_Autotests

2. Установить зависимости:

   pip install -r requirements.txt

3. Настройка API-ключа

Где взять ключ: Ключ указан в финальном проекте по ручному тестированию в разделе 1.5 «Данные для тестирования API»: HW01WCP-0FY4TBZ-QVCKJNC-NN46R8M

Куда вставлять: Создайте в корне проекта файл .env с содержимым:

BASE_URL=https://api.poiskkino.dev/v1.4
API_KEY=HW01WCP-0FY4TBZ-QVCKJNC-NN46R8M

Файл .env добавлен в .gitignore, поэтому ключ не попадёт в репозиторий.

## Запуск тестов

Все тесты (UI + API): pytest

Только UI-тесты: pytest -m ui

Только API-тесты: pytest -m api

## Запуск с Allure-отчётом

1. Запустить тесты с сохранением результатов:

   pytest --alluredir=allure-results

2. Сгенерировать отчёт:

   allure generate allure-results -o allure-report --clean

3. Открыть отчёт:

   allure open allure-report

## Ссылка на финальный проект по ручному тестированию

https://tatiglam.yonote.ru/share/bcc9a568-dd96-4a2c-be8d-8197a8c35a91
