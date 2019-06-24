=====
Yet Another Django URL Shortener
=====

It makes your links shorter, stores it in database and displays it so you can use your short link immediately.

Quick start
-----------

1. Add shorterurlsto your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        shorterurls
    ]

2. Include the shorterurls URLconf in your project urls.py like this::

    path('s/', include('shorterurls.urls')),

3. Run `python manage.py migrate` to create database model.

4. Start the development server.

5. Visit http://127.0.0.1:8000/s/ and make your links shorter.