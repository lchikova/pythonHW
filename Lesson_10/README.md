# Проект автоматизированного тестирования с Allure

## Описание проекта 
Проект содержит автотесты для двух приложений: 1. Медленного калькулятора (https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html) 2. Демо-версии интернет-магазина SauceDemo (https://www.saucedemo.com/). Реализовано на Python с использованием: Selenium WebDriver для автоматизации браузера, pytest как тестового фреймворка, Allure для генерации отчетов, Page Object Pattern для структурирования кода.

## Установка зависимостей 
Перед запуском тестов установите необходимые пакеты: ```bash pip install pytest selenium allure-pytest pytest-xdist ```

## Запуск тестов 
Основные команды: - Все тесты: ```bash pytest lesson_10/tests/ --alluredir=allure-results ``` - Только калькулятор: ```bash pytest lesson_10/tests/test_calculator.py --alluredir=allure-results ``` - Только SauceDemo: ```bash pytest lesson_10/tests/test_saucedemo.py --alluredir=allure-results ``` - Параллельный запуск: ```bash pytest -n auto lesson_10/tests/ --alluredir=allure-results ```

## Работа с Allure 
1. Генерация отчета: ```bash allure generate allure-results -o allure-report --clean ``` 2. Просмотр отчета: ```bash allure open allure-report ``` Или одной командой: ```bash allure serve allure-results ```

## Дополнительные возможности 
Скриншоты автоматически создаются при падении тестов и добавляются в отчет Allure. Тесты размечены с помощью: @allure.feature - функциональная группа @allure.severity - уровень важности @allure.step - шаги выполнения @allure.title - понятное название теста @allure.description - описание теста

## Требования 
- Python 3.7+ - Установленные браузеры (Chrome, Firefox) - Браузерные драйверы (chromedriver, geckodriver)