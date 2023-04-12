
## Installation steps for local
- clone the repo or download the zip file from github.
- create virtual environment(window:virtualenv venv, ubuntu:python3 -m venv venv).
- activate virtualenv : source venv/bin/activate.
- pip install -r requirements.txt.
- python manage.py migrate
- python manage.py createsuperuser(provide the credentials)
- python manage.py runserver
- paste 'http://127.0.0.1:8000/admin/' in url bar of your favourite browser.
- login with created user.
- click on sidebar tab 'Shops' and add shops by providing shop name, latitude and longitude.
- or visit 'http://127.0.0.1:8000/' on your browser and click on 'Create Shops'tabs.You can add the shop.
- click on 'View Shops' tab in navbar.
- enter latitude, longitude and distance in km.
- you will get all the matched shops within the distance which you have entered.


## testing in live server:
- visit 'https://dilip.up.railway.app/'. You can see all shops.
- click on 'Create Shops' tab on navbar and fill the necessary details and create shops.
- click on 'View Shops' tabs on navbar to find all shops within specified distance.




## Note:
- This project is mainly considered on backend part. so frontend stuff is completely. ignored.
- backend code can be enhanced.


## Deployent process:
- pip freeze > requirements.txt to generate requirements.txt file.
- create Procfile file and add 'web: gunicorn 'name-of-application.wsgi'.
- Create runtime.txt file and add 'python -3.10.2'.
- in settings.py change ALLOWED_HOST = [] to ALLOWED_HOST = ['*']
- add 'STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')' in settings.py.
- run 'python manage.py collectstatic'.
- push it to github.
- simply signup into 'https://railway.app/'.
- click  '+New' button
- select 'GitHub Repo'
- select a repo where the code is pushed up.
- click on the project go to the settings tab.
- under domain click generate domain.
- update domain if you want to update.
- our project is live now.

