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
`Запуск тестов по маркерам:
аннотация `@pytest.mark.order(#)`
терминальный запуск по маркеру `pytest -m order`
запуск теста по имени `pytest -m order -k name_test`
запуск с перезапуском упавших `pytest -m smoked44 --reruns 1 test_smoke.py`

# Тестовые данные

`чистый профиль пользователя`

`добавить достаточное количество товара в CatalogPage для:
choose_a_product_1399
choose_a_product_loafers`

`необходимый лимит по подарочной карте и пин в:
payment_bonus_card
payment_bonus_card_no_many`

# Allure репорт

Репорт генерится по умолчанию в `tests/allure-results`

Чтобы сгенерить репорт выполните:

`cd tests/allure-results`

`allure serve .`









