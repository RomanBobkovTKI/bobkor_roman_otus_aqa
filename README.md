## Тест для веб-приложения Presta Shop

1. Установить python версии не ниже Python 3.13.7 
2. Установить pip
3. Установить зависимости:

```commandline
pip install -r requirements.txt
```

4. Заполнить env при необходимости
5. Запуск тестов:

```commandline
pytest
```

5. Возможные флаги:

```commandline
--browser: выбора браузера для запуска[chrome, firefox, safari]
-- url: ссылка на каком окружении запускать
--headless: режим прогона без запуска браузера
```

## Генериция отчета:

Генерация отчёта из папки с данными
```commandline
allure generate allure-results -o allure-report --clean
```

Запуск локального сервера (откроется в браузере)
```commandline
allure open allure-report
```