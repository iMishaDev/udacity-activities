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
    app.run()
