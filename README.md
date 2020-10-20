## API для работы с данными игроков.

Для начала работы, потребуется:

* Клонировать репозиторий на локальную машину
* Открыть проект в IDE
* Установить связи:
```python
pip install -r requirements.txt
```
* Провести миграцию базы данных:
```python
python manage.py migrate
```
* Запустить проект:
```python
python manage.py runserver
```

* Данные суперпользователя для панели администратора:\
login: adminx5 \
password: 123456qQ

Основная ссылка для работы с API: http://127.0.0.1:8000/automatic_api/players/