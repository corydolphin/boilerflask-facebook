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


Forms `forms.py`
------------
We leverage Flask-WTF forms in this application to handle the heavy lifting of validation
and processing of POST data into easy used Python data structures. These forms handle validation
of fields, as well as customized validation querying models and performing more advanced operations.
I.e. `TextField('username', validators=[Required()])` The three current forms are for the Login page, 
the Uploads page and the Registration page.

Models `models.py`
------------
We leverage SQLAlchemy to perform object relational mapping, providing a pythonic way to access 
objects in the database such that we do not need to spend time writing annoying
SQL statements. Instead of inlining SQL everywhere, i.e. 'select * from users where user.id=2',
and manually processing the result, we simply declare a mapping of a python class to the user table
and declare the properties and relationships we wish to map. Allowing us to simply query a User object
by: `User.query.filter(User.id == 1)`. The models also incorporate helper methods I have written
to reduce the amount of code needed, and abstract common operations.

Utils `utils.py`
------------
This module holds utility functions that are used throughout the application.