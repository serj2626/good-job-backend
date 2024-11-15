# API для проекта "Поиск работы для программистов"

## Требования

- Python 3.12

## Скачать

```bash
git clone https://github.com/serj2626/good-job-backend
```

## Перейти в директорию

```bash
cd good-job-backend
```

## Команды для запуска 

<details>

  <summary>Для ubuntu</summary>

    python3.12 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

</details>

<details>

  <summary>Для windows</summary>

    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

</details>

---


## Документация

[Swagger](http://127.0.0.1:8000/api/schema/swagger/)
