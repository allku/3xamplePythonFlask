# Example Python Flask
Basic example project in Python with Flask 2 and SQLAlchemy. 
Include:
* Master detail tables and models
* Migrate models to database
* Database seeder or data loader
* API rest services
* CRUD api rest
* Nested json
* Routes
* Body parameters validation

## Software
* Python 3.8 or above
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
### Create virualenv (bash, zsh, ...)
```
virtualenv venv
```
```
. ./venv/bin/activate
```
### Create virualenv (cmd)
```
virtualenv venv
```
```
.\venv\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Configuration (bash, zsh, ...)
```
export FLASK_APP=app
```
```
export FLASK_ENV=development
```
### Configuration (cmd)
```
set FLASK_APP=app
```
```
set FLASK_ENV=development
```
### Configuration (Powershell)
```
$env:FLASK_APP = "app"
```
```
$env:FLASK_ENV = "development"
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
### Create view
```
flask view create
```
### Seeder
```
flask seed
```
### Run
Before, create folder "logs"
```
flask run
```
#### Custom port
```
flask run --port=5001
```
### Test
```
pytest
```
or
```
pytest -s
```
### Drop view
```
flask view drop
```
### Drop tables
```
flask db downgrade
```
