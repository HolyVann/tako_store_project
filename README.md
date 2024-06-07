# My first Django project
## Online store - _**Tako store**_

---

### Versions

* **Python version** - 3.12+
* **Django verison** - 4.2+
* **PostgreSQL** - 16

---

#### Install PostreSQL

- Install PostgresSQL 16 and pgAdmin 4
- Create user tako with password tako
- Create table tako with user tako

---

#### Run

- Change directory to tako_store:

```
cd tako_store_project
```

- Create virtual environment:

```
python -m venv venv
```

- Activate virtual enviroment:

```
venv\Scripts\activate
```

- Install dependencies:

```
pip install requirements.txt

```

- Create migrations:
```
python manage.py makemigrations

python manage.py migrate
```

- Create superuser:

```
Pthon manage.py createsuperuser
```

- Load fixtures:
```
python manage.py loaddata fixtures/db.json
```

- Run server:

```
python manage.py runserver
```

---
