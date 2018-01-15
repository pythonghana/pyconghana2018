pyGhana

This is the source code for the http://gh.pycon.org website.

Running the site locally
Requirments

    Python 3.6.3
    Django 2.0.1
    Virtualenv
    

Installation

    Follow the guide here on how to clone or fork a repo

    Follow the guide here on how to create virtualenv

    To create a normal virtualenv (example myvenv) and activate it (see Code below).

    sudo apt-get install python-virtualenv

    virtualenv --python=python3.6.3 myvenv

    source myvenv/bin/activate

    (myvenv) $ pip install -r requirements.txt

    (myvenv) $ python manage.py makemigrations

    (myvenv) $ python manage.py migrate

    (myvenv) $ python manage.py runserver

    Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).

    Open the address in the browser

    Don't forget to Change ALLOWED_HOSTS = ['127.0.0.1'] in settings.py

    Note: It is important that when you create your virtualenv, do not create it in the same folder as the code you downloaded.

Contributing

Read our Contributing Guide on how to contribute to the project.
