## Udacity Activity Week#1


### About Flask

Flask is a highly used Python micro Web Framework. It provides basic functionality to build web applications, like routing, request/response handling, etc. It's a "small" framework compared to other ones (like Django), but in many cases that's a great advantage.




### Requirements & Setup


Let us create our first Flask Application project by creating a folder :

```
mkdir flask-activity
```


create a database using psql: 

```
sudo -u postgres -i
createdb flask-activity;
exit;
```


create requirements.txt  for dependencies :
```
touch requirements.txt
```

add the following: 
```
babel==2.9.0
python-dateutil==2.6.0
flask-moment==0.11.0
flask_sqlalchemy==2.4.4
```


create config.py   :
```
touch config.py
open config.py
```

 add the following:
```
import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/flask-activity'
```
create app.py  :

```
touch app.py
```
add the following: 

```
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def index():
    return render_template('my-books.html', books=[ 
        {
            'title': 'A Mind for Numbers',
            'author': 'Barbara Oakley',
            'type': 'Science',
            'read': True
        },
        {
            'title': 'Designing Your Life',
            'author': 'Bill Burnett, Dave Evans',
            'type': 'Life',
            'read': True
        },
        {
            'title': 'A Breif History of Time',
            'author': 'Stephen Hawking',
            'type': 'Science',
            'read': False
        }])
# TODO: implment a GET request to fetch all books

@app.route('/add-book')
def addBook():
    return render_template('add-book.html')
    
# TODO: implment a POST request of adding a book 
# TODO: implment a PUT request to mark the book as read
# TODO: implment a Delete request to delete a book

# Default port:
if __name__ == '__main__':
    app.run(debug=True)
```
create folder named templates:

```
mkdir templates
touch main.html
touch my-books.html
touch add-book.html
```
main.html 

```
<html>
    <head>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="author" content="">
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link type="text/css" rel="stylesheet" href="static/style.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=M+PLUS+Rounded+1c:wght@100&display=swap" rel="stylesheet">
        <!-- /meta -->
        <title>
            MyBooks | Udacity Activity
        </title>
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
</html>
```
my-books.html

```
{% extends 'main.html' %}
{% block content %}
<div class="banner">
    <h1> 
        MyBooks | Udacity Activity
    </h1>
    <div>
        <a class="btn cold" href="/add-book"> Add + </a>
    </div>
</div>
<ul>
    {%for book in books %}
    <li>
        <div class="book-title">
            <h3> 
                {{ book.title }} | {{ book.author }}
            </h3>
            {% if book.read == True %}
            <div>
                &#10003;
            </div>
            {% endif %}
        </div>
        <p>type, {{ book.type }} </p>
        {% if book.read == False %}
        <div class="book-actions">
            <button class="btn success"> Read </button>
            <button class="btn danger"> Delete </button>
        </div>
        {% endif %}
    </li>
    {% endfor %}
</ul>
{% endblock %}
```


add-book.html

```
{% extends 'main.html' %}
{% block content %}
<form action="" method="post">
    <div class="form-input">
        <label> Book Title: </label>
        <input type="text" name="title" />
    </div>
    <div class="form-input">
        <label> Book Author Name: </label>
        <input type="text" name="author" />
    </div>
    <div class="form-input">
        <label> Book Type: </label>
        <input type="text" name="type" />
    </div>
    <button type="submit" class="btn cold float-right"> Add + </button>
</form>
{% endblock %}
```


create static folder :
```
mkdir static
```

create style.css
```
touch style.css
```

add the following: 
```
body {
    background-color: #14141c;
    color: white;
    font-family: 'M PLUS Rounded 1c', sans-serif;
    margin: 20%;
}

ul {
    list-style-type: none;
}

li {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    padding: 0.3rem;
    margin: 0.3rem;
}

form {
    width: 60%;
}

input {
    padding: 0.5rem !important;
    border-radius: 0.5rem !important;
}

a {
    color: white;
    text-decoration: none;
}


.banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.btn {
    border-radius: 0.5rem;
    border: none;
    padding: 0.5rem;
    margin: 0.5rem;
    color: white;
}

.success {
    background-color: #677565;
}

.danger {
    background-color: #A88B99;
}

.cold {
    background-color: #596C7F;
}

.book-title {
    display: flex;
    align-items: center;
}

.float-right {
    float: right;
}

.form-input {
    justify-content: space-between;
    display: flex;
}
```
start with installing the dependencies : 

```
pip3 install -r requirements.txt
```
run the application : 

```
export FLASK_APP=app
flask run
```


### Requirements : 


go through al the TODOs in the app.py  file and implement it, which are the following : 
- [ ] with the help of the dummy data in the index function, create the models needed to make this application functioning. 
- [ ] refactor index function to return an actual data from the database.
- [ ] create a POST request method to add a new book .
- [ ] create a PUT request method to mark a book as read
- [ ] create a DELETE request to delete a book from the list. 



this is how it should look like after implmenting the requirments : 

![Screen Shot 2021-06-21 at 9 50 53 AM](https://user-images.githubusercontent.com/12359091/122719023-517c3300-d276-11eb-9233-6edcbc154fe7.png)

adding a book form: 

![Screen Shot 2021-06-21 at 9 50 58 AM](https://user-images.githubusercontent.com/12359091/122719079-6062e580-d276-11eb-8a55-637d90cfa909.png)


