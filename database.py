from pymongo import MongoClient
from bson.objectid import ObjectId

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['book_management']
books_collection = db['books']

def get_books():
    return list(books_collection.find())

def add_book(title, author, year):
    book = {
        "title": title,
        "author": author,
        "year": int(year) if year else None
    }
    books_collection.insert_one(book)

def get_book_by_id(book_id):
    return books_collection.find_one({"_id": ObjectId(book_id)})

def update_book(book_id, title, author, year):
    books_collection.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {"title": title, "author": author, "year": int(year) if year else None}}
    )

def delete_book(book_id):
    books_collection.delete_one({"_id": ObjectId(book_id)})
