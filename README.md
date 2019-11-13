# ubu-datascience-webapp

----sh
##install pipenv
python -m pip install pipenv --user
##install pipenv
pipenv install django
------
#start pipenv
----sh
pipenv shell
##start django web project
----sh
django-admin startproject webapp
-----
cd webapp
python mange.py startapp myapp
python mange.py makemigrations
python mange.py migrate
python mange.py createsuperuser
python mange.py runserver
