Overview
============
Application code is stored in the `boilerflask` folder (package), with sub folders for `templates` and `static` content. Tests, scripts and other non runtime code is stored in this root directory.


Views `views.py`
------------
Views in flask work by declaring a url to map to a given function i.e. `@app.route('/home')`
Code is executed to perform actions, query the database via models, etc, and then varialbes are passed
to templates by calling `render_template` i.e. `render_template('launch.html')`. These templates are
located in the origiart/templates directory. Some of these views use Forms to handle validation and
other actions, in order to provide a clean and easy to read mapping. Future versions may break these
views into smaller sections and make them more modular



Models `models.py`
------------
Depending on the application you are building, you will likely use a datastore, either NOSQL, i.e. MongoDB
or a relational database, i.e. Postgresql or MySQL. Interacting with these databases is often 
annoying and headache-inducing, thus this boilerplate has support for ORM and ODM, with
SQLAlchemy and Mongodb drivers and ODM commented.


Utils `utils.py`
------------
This module holds utility functions that are used throughout the application. This is often a 
good pattern for holding code which is common to a number of different views, or models, and 
helps keep your code DRY (Do not repeat yourself).