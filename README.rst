IndigoRESTWrapper is intended to provide more complete access to the information in the Indigo database.

This is a (completely unauthorized) wrapper for Indigo (http://www.indigodomo.com/), using 
Django (https://www.djangoproject.com/) and Django-rest-framework (http://www.django-rest-framework.org/).

It can do two things:
 - wrap (some of) the current REST calls, in case you'd like different authentication (the authentication provided by django 
   REST is detailed here: http://www.django-rest-framework.org/api-guide/authentication/)
 - provide a few new acccessors, such as retrieving a device by its 'id' and also providing a view of the history of a device.

Technically it works by either just calling the current Indigo REST api, or for information which isn't available there, scanning the database file(s).

If you don't know Django at all, you might want to follow the Django tutorial first.

To install it you need to :
pip install django pip install djangorestframework

to check this package out. 

You will need to update the name for indigo_db in the DATABASES section in settings.py and also INDIGO_URL (also in settings.py) to tell it where to find the indigo server.

Then, in the project directory, do:

./manage.py migrate 
./manage.py makemigrations indigorestframework 
./manage.py updateindigodb

