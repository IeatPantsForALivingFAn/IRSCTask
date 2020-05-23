cd into this (IRSCTask) directory

start your virtual environment and/or run the command
        pip install -r requirements

make the initial migrations 
        python manage.py migrate

and start the server
        python manage.py runserver

Since this project uses Django-Rest Framework we can use its Browsable API, 
to use this simply go to the your server url for eg:-

        'http://127.0.0.1:8000/?url=https://httpbin.org&datetime=2020-05-24 11:25'

provide the params as shown above using the ? and & to seperate the key value pairs.
Sample  key value pairs as follows:-

        url = https://httpbin.org
        datetime = 2020-05-24 11:25 (yy-mm-dd HH-MM)
        (follow this specific format for passing the date time parameter)

to test the server go to 
        http://127.0.0.1:8000/ping/

NOTE:-
Django rest Framework is required and replace https://127.0.0.1:8000 with your own servers
URL 
To get JSON response specifically use the format suffix .json on the url eg:- 
        http://127.0.0.1:8000/ping.json

.api for API response