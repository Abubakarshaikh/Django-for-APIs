(if not installed)
step #1 - pip install pipenv
step #2 - pipenv install django~=3.1.0
step #3 - pipenv shell
(Launching subshell in virtual environment)
[Now that Django is installed]
step #4 - django-admin startproject config .
step #5 - python manage.py startapp todos
step #6 - python manage.py migrate
step #7 - python manage.py makemigrations todos
step #8 - python manage.py migrate
step #9 - winpty python manage.py createsuperuser
step #10 - python manage.py runserver
step #11 - pipenv install djangorestframework~=3.11.0