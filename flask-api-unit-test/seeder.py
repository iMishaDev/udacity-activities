from flask import Flask
from models import Student, Professor, Course, Enrollment
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

db = SQLAlchemy()
app.config.from_object('config')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.app = app
db.init_app(app)


c1 = Course(name="Software Engineering",
            semester=1)


c2 = Course(name="Data Structures",
            semester=1)



db.session.add(c1)
db.session.add(c2)
db.session.commit()



s1 = Student(name="Mohammed",
                email="mohammed@student.com",
                gpa=3.5)


db.session.add(s1)
db.session.commit()

s2 = Student(name="Khlaid",
            email="khalid@student.com",
            gpa=3.5)

db.session.add(s2)
db.session.commit()


s3 = Student(name="Malik",
            email="Malik@student.com",
            gpa=3.9)
db.session.add(s3)
db.session.commit()

s4 = Student(name="Abeer",
            email="abeer@student.com",
            gpa=3.9)
db.session.add(s4)
db.session.commit()



s5 = Student(name="Atheer",
            email="Atheer@student.com",
            gpa=3.9)
db.session.add(s5)
db.session.commit()


s6 = Student(name="Areej",
            email="Areej@student.com",
            gpa=3.9)
db.session.add(s6)
db.session.commit()


prof1 = Professor(name="Abdullah",
                email="abdullah@professor.com")
db.session.add(prof1)
db.session.commit()

prof2 = Professor(name="Rania",
                email="rania@professor.com")
db.session.add(prof2)
db.session.commit()


en1 = Enrollment(
    course_id=c1.id,
    professor_id=prof1.id,
    student_id=s1.id,
    grade=89
)

db.session.add(en1)
db.session.commit()


en1 = Enrollment(
    course_id=c1.id,
    professor_id=prof1.id,
    student_id=s2.id,
    grade=89
)

db.session.add(en1)
db.session.commit()


en1 = Enrollment(
    course_id=c1.id,
    professor_id=prof1.id,
    student_id=s3.id,
    grade=89
)

db.session.add(en1)
db.session.commit()

en1 = Enrollment(
    course_id=c2.id,
    professor_id=prof2.id,
    student_id=s4.id,
    grade=89
)

db.session.add(en1)
db.session.commit()


en1 = Enrollment(
    course_id=c2.id,
    professor_id=prof2.id,
    student_id=s5.id,
    grade=89
)

db.session.add(en1)
db.session.commit()


en1 = Enrollment(
    course_id=c2.id,
    professor_id=prof2.id,
    student_id=s6.id,
    grade=89
)

db.session.add(en1)
db.session.commit()

