from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table de liaison many-to-many
student_books = db.Table('student_books',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)
    birth_date = db.Column(db.Date)
    enrolled = db.Column(db.Boolean, default=True)
    books = db.relationship('Book', secondary=student_books, back_populates='students')

class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    published_at = db.Column(db.Date)
    students = db.relationship('Student', secondary=student_books, back_populates='books')

