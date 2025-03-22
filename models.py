from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    published_at = db.Column(db.DateTime)
    borrowers = db.relationship('Student', back_populates = 'borrowed_books', secondary='StudentBook')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime)
    borrowed_books = db.relationship('Book', back_populates = 'borrowed_books', secondary='StudentBook')

class StudentBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey(Student.id), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id), nullable=False)
    borrow_date =  db.Column(db.DateTime, nullable=False)
    return_date =  db.Column(db.DateTime)

