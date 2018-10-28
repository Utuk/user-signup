from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = (os.path.join(os.path.dirname(__file__)), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
"""

#@app.route("/")
#def index():
    #template = jinja_env.get_template('index.html')
    #return template.render()

@app.route('/signup')
def display_form():
    template = jinja_env.get_template('index.html')
    return template.render()

@app.route('/signup', methods=['POST'])
def validate_form():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_password_error = '' 
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = "That's not a valid username"
        username = ''
    else:
        if username == '':
            username_error = "That's not a valid username"
            username = ''
    if ' ' in username == True:
        username_error = "That's not a valid username"
        username = ''

    if len(password) < 3 or len(password) > 20:
        password_error = "That's not a valid password"
        password = ''
    else:
        if ' ' in password == True:
            password_error = "That's not a valid password"
            password = ''
    if password == '':
        password_error = "That's not a valid password"
        password = ''
    
    if verify_password != password:
            verify_password_error = "Passwords don't match"
            verify_password = ''
    else:
        if verify_password == '' :
            verify_password_error = "Passwords don't match"
            verify_password = ''

    if '@' not in email:
        email_error = "That's not a valid email"
        email = ''
    else:
        if '.' not in email:
            email_error = "That's not a valid email"
            email = ''
    if ' ' in email:
        email_error = "That's not a valid email"
        email = ''
    else:
        if len(email) < 3 or len(email) > 20:
            email_error = "That's not a valid email"
            email = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        name = username
        return redirect('/welcome?username={0}'.format(username)) 
    else:
        template = jinja_env.get_template('index.html')
        return template.render(username_error=username_error,
            password_error=password_error,
            verify_password_error=verify_password_error,
            email_error=email_error,
            username=username,
            password='',
            verify_password='',
            email=email)

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    template = jinja_env.get_template('welcome.html')
    return template.render(username=username)


app.run()
