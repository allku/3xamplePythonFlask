# 3xamplePythonFlask
Basic example project in Python with Flask 2 and SQLAlchemy

## Software
* Python 3.9 
* Postgres 13 or above

### Create database on GNU/Linux and MacOS with Postgres.app
```
createdb epythonflask
```
```
createuser jorgeluis
```
```
psql
```
or
```
psql -d database -U user -W
```
```
grant all privileges on database epythonflask to jorgeluis;
```
```
alter user jorgeluis with encrypted password 'j';
```
### Create virualenv
```
virtualenv venv
```
```
. ./venv/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Migrate database
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```
### Seeder
```
flask seed
```
### Run
```
export FLASK_APP=app
```
```
export FLASK_ENV=development
```
```
flask run
```
#### Custom port
```
flask run --port=5001
```

### Drop tables
```
flask db downgrade
```
## Test
Use HTTPie
https://httpie.io/
### GET
```
http http://localhost:5000/rest/v1/beers
```
### GET
```
http http://localhost:5000/rest/v1/beer/1
```
### POST
```
http POST http://localhost:5000/rest/v1/beer <<< '{
    "brand": "Anheuser-Busch Inbev",
    "dateReleased": "2000-01-01",
    "ingredients": [
        {
            "name": "Malta"
        },
        {
            "name": "Agua"
        }
    ],
    "name": "Cusqueña",
    "origin": "Perú"
}'
```
### PUT
```
http PUT http://localhost:5000/rest/v1/beer/3 <<< '{
    "brand": "Other",
    "dateReleased": "2001-01-01",
    "name": "Cusqueñita",
    "origin": "Perú - Ecuador"
}'
```
### DELETE
```
http DELETE http://localhost:5000/rest/v1/beer/3
```
