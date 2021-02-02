# Financial dashboard

Python 3.8.
Django 3.1.5.
AdminLTE template

https://gpbdashboard.herokuapp.com

## Implemented (on 31/01/2021):
* Account balances table for each company on each day.
* Inflow chart for each company for week.
* Load data from .csv file:
 ```shell script
    python manage.py load_data file.csv   
 ```

## Installing project
1. [Install python.](https://www.python.org/downloads/)
2. Download or clone repository.
3. Create virtual environment: python -m venv env
4. Activate the virtual environment: source env/bin/activate (for linux) or env/scripts/activate (for windows)
5. Install requirements: pip install -r requirements.txt
7. Migrate: python manage.py migrate (if OperationalError: no such table: python manage.py migrate --run-syncdb)
8. Run the project: python manage.py runserver
9. Open in browser: http://localhost:8000 or http://127.0.0.1:8000.

