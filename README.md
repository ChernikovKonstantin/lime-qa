Используется тестовый фраймворк [selene](https://github.com/yashaka/selene) (python selenium wrapper)

# Предусловия

Установите локально:

- [Python 3.9](https://www.python.org/)
- Бразуер [Chrome](https://www.google.com/chrome/)
- [Allure CLI](https://github.com/allure-framework/allure2)

# Уставновка

`pip install requests

# Запуск тестов

`pytest tests/`

# Allure репорт

Репорт генерится по умолчанию в `tests/allure-results`

Чтобы сгенерить репорт выполните:

`cd tests/allure-results`

`allure serve .`

Запуск тестов по маркерам:
аннотация `@pytest.mark.order(#)`
терминальный запуск `pytest -m order` 


