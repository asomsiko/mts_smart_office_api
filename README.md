# mtc_smart_office_api
API для системы умного оффиса. Написано на Flask.
## Установка
1. Клонирование репозитория:
`git clone https://github.com/muzzy-afk/mtc_smart_office_api`

2. Установка зависимостей:
`pip install -r requirements.txt`

3. Инициализация базы данных:
`flask db init && flask db migrate && flask db upgrade`
## Использование
### Запуск:
`python3 run.py`
### Роуты:
#### [Аутентификация](https://github.com/muzzy-afk/mtc_smart_office_api/blob/main/app/auth_routes.py)
* /login
* /signup

#### [Личный кабинет](https://github.com/muzzy-afk/mtc_smart_office_api/blob/main/app/user_profile_routes.py)
* /user-profile
* /user-profile/reminders
* /user-profile/achivements
* /user-profile/orders
* /user-profile/tasks
* /user-profile/settings

#### [Сервисы](https://github.com/muzzy-afk/mtc_smart_office_api/blob/main/app/main_page_routes.py)
* /services/gpt **(в разработке)**
* /services/mts-services **(в разработке)**
* /services/yandex-services **(в разработке)**
* /services/service-order **(в разработке)**
* /services/complaint
* /services/office-devices **(в разработке)**
* /services/office-map **(в разработке)**
* /services/schedule **(в разработке)**

#### [Запросы к базе данных (геттеры)](https://github.com/muzzy-afk/mtc_smart_office_api/blob/main/app/getter_routes.py)
* /sorted-achivements
* /filtered-achivements
* /work-rooms
* /relax-rooms
* /complaints/<string:state>
* /wishes
* /sorted-orders
* /filtered-orders
* /sorted-devices
* /filtered-devices
* /sorted-reminders
* /filtered-reminders
* /sorted-advertisements
* /filtered-advertisements
* /states
* /filtered-rooms
* /sorted-rooms
* /sorted-users
* /filtered-users