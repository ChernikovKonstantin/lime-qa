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


# Проблемы о состоянию 25.05.2023

Test main screen bunners
не выполняется возврат из каталога к хедеру лендинга

test search
test main menu search
в двнный момент модуль поиска не работает

test payment card order 6000
баг с применением скидки 5% на заказы более 6000

test_burger_menu
необходимо добавить разделы во вкладку Дополнительно

test card product 
в слайдере есть не вертикальные изображения

test card bonus card self provo
test card bonus card self provo pick point
не верно читается сумма в строке итого после применения промокода


Актуализация 18.07.2023

test_main_screen_banners
https://lmdev.testrail.io/index.php?/cases/view/849
Не выполняется: на основном экране при возврате отображается первый баннер в хедере сайта

test_burger_menu_check_products
https://lmdev.testrail.io/index.php?/cases/view/890&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=130
Не выполняется: 2.Выберите раздел, не имеющий подразделов, например, сумки 
нужно добавить раздел в админке

test_profile_order
https://lmdev.testrail.io/index.php?/cases/view/880
Не выполняется: Отображаются история покупок

test_search
https://lmdev.testrail.io/index.php?/suites/view/2&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=123
Не выполняется:Появляются карточки товаров, релевантные запросу 1418-888

test_payment_cart_order_more_6000
https://lmdev.testrail.io/index.php?/cases/view/906&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=124"
баг

test_profile_order
https://lmdev.testrail.io/index.php?/cases/view/880
баг, разные номера заказов в сообщение после заказа и в ЛК















