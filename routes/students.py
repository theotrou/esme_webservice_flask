from flask import Blueprint, request, jsonify
from models import db, Student, Book
from datetime import datetime

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([
        {
            'id': s.id,
            'first_name': s.first_name,
            'last_name': s.last_name,
            'email': s.email,
            'birth_date': s.birth_date.strftime('%Y-%m-%d') if s.birth_date else None,
            'enrolled': s.enrolled,
            'books': [b.id for b in s.books]
        }
        for s in students
    ])

@students_bp.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'email': student.email,
        'birth_date': student.birth_date.strftime('%Y-%m-%d') if student.birth_date else None,
        'enrolled': student.enrolled,
        'books': [b.id for b in student.books]
    })

@students_bp.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    student = Student(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d'),
        enrolled=data.get('enrolled', True)
    )
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student added', 'id': student.id}), 201

@students_bp.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()

    student.first_name = data.get('first_name', student.first_name)
    student.last_name = data.get('last_name', student.last_name)
    student.email = data.get('email', student.email)
    student.enrolled = data.get('enrolled', student.enrolled)
    if 'birth_date' in data:
        student.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')

    db.session.commit()
    return jsonify({'message': 'Student updated'})

@students_bp.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({'message': 'Student deleted'})

@students_bp.route('/students/<int:id>/borrow/<int:book_id>', methods=['POST'])
def borrow_book(id, book_id):
    student = Student.query.get_or_404(id)
    book = Book.query.get_or_404(book_id)

    if book in student.books:
        return jsonify({'error': 'Book already borrowed'}), 400

    student.books.append(book)
    db.session.commit()
    return jsonify({'message': f'Book {book_id} borrowed by student {id}'}), 200

@students_bp.route('/students/<int:id>/return/<int:book_id>', methods=['POST'])
def return_book(id, book_id):
    student = Student.query.get_or_404(id)
    book = Book.query.get_or_404(book_id)

    if book not in student.books:
        return jsonify({'error': 'Book not borrowed by this student'}), 400

    student.books.remove(book)
    db.session.commit()
    return jsonify({'message': f'Book {book_id} returned by student {id}'}), 200
