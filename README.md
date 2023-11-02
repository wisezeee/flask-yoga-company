# flask-yoga-company

Установка вирутального окружения

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Запуск контейнера с базой данных

```bash
docker run --name yoga_db -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -p 38748:5432 -d postgres
```

Создание таблицы для работы с сущностью пользователя.

```sql
create table "user"
(
    id       serial primary key,
    email    text,
    password text,
    name     text
)
```

Запуск проект
```bash
export FLASK_APP=runner
export FLASK_DEBUG=1
flask run
```