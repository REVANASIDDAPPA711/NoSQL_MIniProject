from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB (local instance)
app.config["MONGO_URI"] = "mongodb://localhost:27017/book_management_db"
mongo = PyMongo(app)

# Route to list all books
@app.route('/')
def index():
    # Fetch all books from the MongoDB 'books' collection
    books = mongo.db.books.find()  # 'books' is your MongoDB collection name
    return render_template('list_books.html', books=books)

# Route to add a new book
@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        # Insert the new book data into MongoDB 'books' collection
        mongo.db.books.insert_one({
            'title': title,
            'author': author,
            'year': year
        })

        return redirect(url_for('index'))  # Redirect to the homepage after adding the book
    return render_template('add_book.html')

# Route to edit an existing book (by book id)
@app.route('/edit/<book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    # Convert book_id from string to ObjectId
    book = mongo.db.books.find_one({'_id': ObjectId(book_id)})  # Find book by ObjectId
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        # Update the book in MongoDB
        mongo.db.books.update_one(
            {'_id': ObjectId(book_id)},  # Update using ObjectId
            {'$set': {'title': title, 'author': author, 'year': year}}
        )

        return redirect(url_for('index'))

    return render_template('edit_book.html', book=book)

# Delete Book Route
@app.route('/delete/<book_id>', methods=['GET'])
def delete_book(book_id):
    # Convert book_id from string to ObjectId
    mongo.db.books.delete_one({'_id': ObjectId(book_id)})  # Delete using ObjectId
    return redirect(url_for('index'))  # Redirect to homepage after deleting

if __name__ == '__main__':
    app.run(debug=True)
