<h1 align="center">Todo app</h1>

![image](https://github.com/ryabant/todotu/blob/main/Screenshot_2021-05-10%20Todotu.png)

## Using stack
### Backend

- Django REST framework
- Django ORM
- PostgreSQL

### Frontend

- Vue.js
- Javascript
- Styling with Bulma

## Development setup

Steps to locally setup development after cloning the project.

### Backend

Have Python 3.8 installed and in PATH.
Installing Python: https://realpython.com/installing-python/

```sh
python3 --version
# Python 3.8.5
```

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate

# Windows users
# .venv/scripts/activate

pip install -r requirements.txt

# Windows users, if you encounter pg_config error:
# 1) Install PostgresSQL and use the solution at https://stackoverflow.com/a/58440598/1262198

# Need to have Docker and Docker Compose installed
# Start PostgreSQL and other services via Docker Compose
docker-compose -f services.yml up --d

python manage.py migrate
python manage.py createsuperuser --username admin --email a@a.com
python manage.py runserver
```

- API root available at `http://localhost:8000/api/`
- Admin available at `http://localhost:8000/backdoor/`

### Frontend

- [Node.js](https://nodejs.org) v14 or greater

```sh
node --version
# 14.16.1
```

```sh
cd frontend
npm install
npm run serve
```

React app is now accessible at `http://localhost:8080`