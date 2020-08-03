# acme1
Acme Inc product a management

### Technology 

* Python (Django)
* SQLite 

## Code base contains 
* Db model
* APIs 

## Setup for development
* Create and activate env
* Install packages using`pip install requirements.txt`
* Create `db.sqlite3` DB and run `./mangae.py migrate`
* `.env` and replace dummy values with actual crednetials
* Install Rabiit MQ : `sudo apt-get install rabbitmq-server -y --fix-missing`
* Run local server using `./mangae.py runserver`
* Run `celery -A acme worker -l info`

# Urls

## Test
- In browser equivalent tool: hit
   * GET  http://127.0.0.1:8000/products/list/  with filters and search
   * POST http://127.0.0.1:8000/products/upload/
   * POST http://127.0.0.1:8000/products/delete/
   
