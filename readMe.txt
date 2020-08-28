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

    (you can also specify the python version in virtual env: virtualenv -p /usr/bin/python2 <env name>)

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

21. we can use wtf package for managing forms in python-flask: 

        a. first you have to install it: 
                pip install flask-wtf

        b. in flask_wtf we write a python class that represent our form, and it will 
            convert to html, in this class we use another classes that we import

            from flask_wtf import FlaskForm
            from wtforms import StringField, PasswordField, SubmitField, BooleanField
            from wtforms.validators import DataRequired, Length, Email, EqualTo

            class RegistrationForm(FlaskForm):
                username = StringField('Username',
                                        validators=[DataRequired(), Length(min=2, max=20)])
                email = StringField('Email', validators=[DataRequired(), Email()])
                
                password = PasswordField('Password', validators=[DataRequired()])
                confirm_password = PasswordField('Confirm Password', 
                                                validators=[DataRequired(), EqualTo('password')])            
                submit = SubmitField('Sign Up')
                

            class LoginForm(FlaskForm):

                email = StringField('Email', validators=[DataRequired(), Email()])
                
                password = PasswordField('Password', validators=[DataRequired()])
                
                remember = BooleanField('Remember Me')
                
                login = SubmitField('Login')

            
            c. you can use secret keys against CSRF attacks:

                    first get secret from secret module built in python: 

                        import secrets
                        secrets.token_hexa(16)
                    
                    when you get this secret, you can add it:
                        app.config['SECRET_KEY'] = '93f19072e4afdb96021f44d3ce3c9448'

22. then we can import this forms in the app, and pass this to the template, then we can use this form in the template: 

                @app.route('/register')
                def register():
                    form = RegistrationForm()
                    return render_template('register.html', title = 'Register', form=form)

23. using form in the template: 

            {% extends "layout.html" %}
            {% block content %}
            <div class="content-section">
                <form action="Post" action="">
                {{ form.hidden_tag() }}
                <fieldset class="form-group">
                    <legend class="border-bottom mb-4">Join Today</legend>
                    <div class="form-group">
                    {{ form.username.label(class="form-control-label") }}
                    {{ form.username(class="form-control form-control-lg") }}
                    </div>
                    <div class="form-group">
                    {{ form.email.label(class="form-control-label") }}
                    {{ form.email(class="form-control form-control-lg") }}
                    </div>
                    <div class="form-group">
                    {{ form.password.label(class="form-control-label") }}
                    {{ form.password(class="form-control form-control-lg") }}
                    </div>
                    <div class="form-group">
                    {{ form.confirm_password.label(class="form-control-label") }}
                    {{ form.confirm_password(class="form-control form-control-lg") }}
                    </div>
                </fieldset>
                <div class="form-group">
                    {{ form.submit(class="btn btn-outline-info") }}
                </div>
                </form>
            </div>
            <div class="border-top p-3">
                <small class="text-muted">
                Already have an account? <a class="ml-2" href="{{ url_for('login') }}">Sign In</a>
                </small>
            </div>
            {% endblock %}

24. If we send the form we get not allowed request, so we have to define the list of methods in the route: 

            @app.route('/register', methods=['GET', 'POST'])
            def register():
                form = RegistrationForm()
                if form.validate_on_submit():
                    flash(f'Account created for {form.username.data}', 'success')
                    return redirect(url_for('home'))            # import redirect from flask
                return render_template('register.html', title = 'Register', form=form)


25. We can use flask-sqlalchemy package to interact with database, sqlalchemy is a orm:

        a. first install it: 
                pip install flask-sqlalchemy
        
        b. then import it: 
                from flask_sqlalchemy import SQLAlchemy

        
        c. the use in app.config: 

                app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

                # /// in sqlite means relative address

        d. make the database that has been defined: 

                db = SQLAlchemy(app)