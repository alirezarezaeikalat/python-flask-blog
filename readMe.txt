1. you can see all your python global packages:
        pip list
2. if you run pip freeze you get all the global packages beside local packages in the environment:

        pip freeze --local > requirements.txt

3. you can install all the packages in the requirements.txt file: 
        pip install -r requirements.txt


4. to run the flask app First, make sure virtualenv is installed
    $ pip3 install virtualenv

5. Then create a directory for your new Flask project
    $ mkdir MyNewFlaskApp

6. Navigate to your newly created directory
    $ cd MyNewFlaskApp

7. Create your virtual environment with venv name
    $ virtualenv venv --system-site-packages        #venv is the name

    (you can also specify the python version: virtualenv -p /usr/bin/python2 <env name>)

8. Activate the virtual environment
    $ source venv/bin/activate                      #vene is the name of environment variable

    (you can type deactivate to deactive the environment)
    (then you can delete the environment rm -rf <env name folder>)

9. Make sure Flask is installed
    (venv) $ pip3 install Flask

10. Set the FLASK_APP system variable
    (venv) $ export FLASK_APP=<my_new_flask_app.py>

11. Run Flask
    (venv) $ flask run

12. __name__ is the special variable in the python that is name of the module that the app

13. you can run the flask app in debug mode, to see the changes online:

    a. export FLASK_DEBUG=1
    b. flask run

14. we can also run this directly with python:

        python <name of the file>

15. to return html for the route we can use templates: 

        from flask import Flask, render_template

        @app.route('/')
        @app.route('/home')
        def hello_world():
            return render_template('home.html')

16, you can pass data to the template by passing the data as argument: 

        return render_template('home.html', posts = posts)

17. flask use template engine named jinja-2 and in the view we can use the data that has been passed: 

        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% if title %}
            <title>Flask Blog - {{ title}}</title>
        {% else %}
            <title>Flask Blog</title>
        {% endif %}
        </head>
        <body>
        {% for post in posts %}
            <h1>{{ post.title }}</h1>
            <p>By {{ post.author }} on {{post.date_posted}}</p>
            <p>{{ post.content }}</p>
        {% endfor %}
        </body>
        </html>

18. you can also make the template in jinja-2, check the example in this file: 

        {% block content %} {% endblock %} this section is in the layout file, content is the name

        and this section are in the files
        {% extends "layout.html" %}
            {% block content %}
            {% for post in posts %}
                <h1>{{ post.title }}</h1>
                <p>By {{ post.author }} on {{post.date_posted}}</p>
                <p>{{ post.content }}</p>
            {% endfor %}
        {% endblock %}

19. to serve static files in flask, we have to put them in static directory, python flask has static middleware,

20. for routing we can use url_for from flask

    from flask import Flask, render_template, url_for

    <link rel="stylesheet" href="{{ url_for('static', filename='main.css')}}">

[ATTENTION]
    it is a good idea to use url_for for every routing in the app