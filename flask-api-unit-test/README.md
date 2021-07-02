

## Udacity Activity Week#4 

this project is built as activity for the Full Stack Nanodegree. Students are required to complete the requirments to build the backend of this app using flask & SQLAlchemy. the focus of this activity is to give students more practicing of Unit Test. 


### about the acitivty 
this is a small University System. there're students, professors, courses and enrollments. enrollments contains the course, the student and the professor giving this course. many professors can give the same course. student can have many courses. the course can be taken by many students. as you can see there's no frontend provided or needed for this activity, you can test your backend by using POSTMAN. a collection provided for you to start.


## setup 
1. make sure you have python to run the app. 
2. install the dependencies required by running `pip3 install -r requirements.txt` 
3. create a postgres database for the app by doing the following: 
    - `sudo -u postgres -i` 
    - `createdb flask-api-unit-test;` (for the development)
    - `createdb flask-api-unit-test-test;` (for the unit tests)
    - `exit`
4. make sure you have the same name or else you need to update the `config.py` file with your database name. 
5. start migrating the models you have in `models.py` by doing the following: 
    - `pip3 install flask_migrate`
    - `flask db init`
    - `flask db migrate`
    - `flask db upgrade`
    now you have the database with the tables created, now we need to add data to it.
6. run the `seeder.py` file to fill the database with the dummy data that has been created in the seeder. 
    to run it you just need to do `pythoon3 seeder.py`

7. Now you have the database filled with data and ready to execute the app by running the following : 
    - `export FLASK_APP=app`
    - `export DEBUG_MODE=True`
    - `flask run`

8. import the POSTMAN collection into your machine and test it out to make sure everything is working.



### review 
let's start with showing the project strucure : 
.
```
+-- config.py
+-- models.py
+-- requirements.py
+-- seeder.py
+-- app.py
+-- tests.py
+-- README.md
```


## Models Walk-though
```
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
``` 

we have a 3 Models representing the main entities we mentioned before, `Student`, `Course` and `Professor`. there's a Ternary relationship between them, named `Enrollment` containing the objects of these 3 along with the student grade on this course.




in `app.py`, I have already created the CRUD endpoints for Student, Course, Professor, and Enrollment. 
in `tests.py` you will find an initial setup for creating test cases on these endpoints.  




## requirments 
- [ ] test getting all courses has a success response with the following structure : 
    ```
        {
            'success': True,
            'courses': formatted_courses,
            'total_courses': courses.total
        }
     ```
- [ ] test getting all courses with an invalid page number has a `422` failure response with a message `unprocessable`.
- [ ] test getting a course has a success response with the following structure : 
    ```
        {
            'success': True,
            'course': courseData,
        }
     ```
- [ ] test getting a course with an invalid id has a `404` failure response with a message `resource not found`.
- [ ] test posting a course with a valid data has a success reponse with the following structure: 
  ```
    {
         'success': True,
          'course': courseData,
    }
   ```
- test posting a course with an invalid data or missing ones, make sure it returns `500` response. 
- [ ] test deleting a course with a valid id has a success reponse with the following structure: 
  ```
    {
         'success': True,
          'course': course_id,
    }
   ```
- test deleting a course with an invalid id has a `404` reponse with a message `resource not found`. 
- [ ] PLUS+ in the enrollment GET, PUT and DELETE endpoints, I want you to load the data related to the course, student and professor. 
- [ ] test the other endpoints the same way courses are tested with handling additional failure schenarios if possible. 
to run your tests, run `python3 tests.py`

This is How your postman collection looks like affter importing: 
<img width="1646" alt="Screen Shot 2021-07-02 at 6 55 31 PM" src="https://user-images.githubusercontent.com/12359091/124300387-314a4f00-db67-11eb-8fc4-1737281345cb.png">

