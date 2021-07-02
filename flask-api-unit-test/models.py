from flask_migrate import Migrate
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Float
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import timeago
import datetime


now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, test_config=None):
    app.config.from_object('config')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if test_config:
        app.config["SQLALCHEMY_DATABASE_URI"] = test_config
    db.app = app
    Migrate(app, db)
    db.init_app(app)
    db.create_all()


'''
Student

'''


class Student(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    gpa = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    enrollments = relationship("Course", secondary="enrollments")

    def __init__(self, name, email, gpa):
        self.name = name
        self.email = email
        self.gpa = gpa

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'gpa': self.gpa,
            'created_at': timeago.format(self.created_at, now)
        }






'''
Enrollments

'''


class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    course_id = Column(db.Integer, ForeignKey('courses.id'))
    professor_id = Column(db.Integer, ForeignKey('professors.id'))
    student_id = Column(db.Integer, ForeignKey('students.id'))
    grade = Column(Float, default=0)
    
    def __init__(self, course_id, professor_id, student_id, grade):
        self.course_id = course_id
        self.professor_id = professor_id
        self.student_id = student_id
        self.grade = grade

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'course_id': self.course_id,
            'professor_id': self.professor_id,
            'student_id': self.student_id,
            'grade': self.grade
        }




'''
Course

'''


class Course(db.Model):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    semester = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    students_enrollments = relationship("Student", secondary="enrollments")
    professors_enrollments = relationship("Professor", secondary="enrollments")

    def __init__(self, name, semester):
        self.name = name
        self.semester = semester


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'semester': self.semester,
            'created_at': self.created_at,
        }






'''
Professor

'''


class Professor(db.Model):
    __tablename__ = 'professors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    enrollments = relationship("Course", secondary="enrollments")

    def __init__(self, name, email):
        self.name = name
        self.email = email


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at,
        }
