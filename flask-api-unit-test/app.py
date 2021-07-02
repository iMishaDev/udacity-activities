from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from models import  setup_db, Course, Student, Professor, Enrollment
from flask_cors import CORS
# from sqlalchemy.orm import load_only, joinedload
from datetime import date
import sys

DATA_PER_PAGE = 10





def create_app():
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return redirect(url_for('getCourses'))

    @app.route('/courses', methods=['GET'])
    def getCourses():
        try:
            page = request.args.get('page', 1, type=int)
            courses = Course.query.paginate(page, per_page=DATA_PER_PAGE)
            formatted_courses = [course.format() for course in courses.items]
        except: 
            print(sys.exc_info())
            abort(422)

        return jsonify({
            'success': True,
            'courses': formatted_courses,
            'total_courses': courses.total
        })
    
    @app.route('/courses/<int:course_id>')
    def getCourse(course_id):
        course = Course.query.get(course_id)
        
        if course is None:
            abort(404)
        
        return jsonify({
            'success': True,
            'course': course.format(),
        })


    @app.route('/courses', methods=['POST'])
    def createCourse():
        courseData = request.get_json()
        try: 
            course = Course(
                name=courseData['name'],
                semester=courseData['semester']
            )
            course.insert()
        except:
            print(sys.exc_info())
            abort(500)
        

        return jsonify({
            'success': True,
            'course': course.format(),
        })

    @app.route('/courses/<int:course_id>', methods=['PUT'])
    def updateCourse(course_id):
        courseData = request.get_json()
        course = Course.query.get(course_id)
        
        if course is None:
            print(sys.exc_info())
            abort(404)
        
        try :
            course.name = courseData['name']
            course.semester = courseData['semester']
            
            course.update()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'course': course.format(),
        })

    @app.route('/courses/<int:course_id>', methods=['DELETE'])
    def deleteCourse(course_id):
        course = Course.query.get(course_id)
        if course is None:
            abort(404)
        
        try: 
            course.delete()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'course': course_id,
        })



    @app.route('/students')
    def getStudents():
        page = request.args.get('page', 1, type=int)
        students = Student.query.paginate(page, per_page=DATA_PER_PAGE)
        formatted_students = [student.format() for student in students.items]
        return jsonify({
            'success': True,
            'students': formatted_students,
            'total_students': students.total
        })
    
    @app.route('/students', methods=['POST'])
    def createStudent():
        studenteData = request.get_json()
        try: 
            student = Student(
                name=studenteData['name'],
                email=studenteData['email'],
                gpa=studenteData['gpa']
            )
            student.insert()
        except:
            print(sys.exc_info())
            abort(500)
        

        return jsonify({
            'success': True,
            'course': student.format(),
        })

    @app.route('/students/<int:student_id>', methods=['PUT'])
    def updateStudents(student_id):
        studenteData = request.get_json()
        student = Student.query.get(student_id)
        
        if student is None:
            print(sys.exc_info())
            abort(404)
        
        try :
            student.name = studenteData['name']
            student.email = studenteData['email'],
            student.gpa = studenteData['gpa']
            
            student.update()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'student': student.format(),
        })

    @app.route('/students/<int:student_id>', methods=['DELETE'])
    def deleteStudent(student_id):
        student = Student.query.get(student_id)
        if student is None:
            abort(404)
        
        try: 
            student.delete()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'student': student_id,
        })


    @app.route('/students/<int:student_id>')
    def getStudent(student_id):
        student = Student.query.get(student_id)
        if student is None:
            abort(404)

        return jsonify({
            'success': True,
            'student': student.format(),
        })

    @app.route('/professors')
    def getProfessors():
        page = request.args.get('page', 1, type=int)
        professors = Professor.query.paginate(page, per_page=DATA_PER_PAGE)
        formatted_professors = [professor.format() for professor in professors.items]
        return jsonify({
            'success': True,
            'professors': formatted_professors,
            'total_professors': professors.total
        })
    
    @app.route('/professors/<int:professor_id>')
    def getProfessor(professor_id):
        professor = Professor.query.get(professor_id)
        if professor is None:
            abort(404)

        return jsonify({
            'success': True,
            'professor': professor.format(),
        })

    @app.route('/professors', methods=['POST'])
    def createProfessor():
        professorData = request.get_json()
        try:
            professor = Professor(
                name=professorData['name'],
                email=professorData['email'],
            )
            professor.insert()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'professor': professor.format(),
        })

    @app.route('/professors/<int:professor_id>', methods=['PUT'])
    def updateProfessor(professor_id):
        professorData = request.get_json()
        professor = Professor.query.get(professor_id)

        if professor is None:
            print(sys.exc_info())
            abort(404)

        try:
            professor.name = professorData['name']
            professor.email = professorData['email']

            professor.update()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'professor': professor.format(),
        })

    @app.route('/professors/<int:professor_id>', methods=['DELETE'])
    def deleteProfessor(professor_id):
        professor = Professor.query.get(professor_id)
        if professor is None:
            abort(404)

        try:
            professor.delete()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'student': professor_id,
        })


    @app.route('/enrollments')
    def getEnrollments():
        page = request.args.get('page', 1, type=int)
        course_id = request.args.get('course_id', 0, type=int)
        enrollments_query = Enrollment.query

        if course_id != 0:
            enrollments_query = enrollments_query.filter_by(
                course_id=course_id)
        
        enrollments = enrollments_query.paginate(
            page, per_page=DATA_PER_PAGE)
        formatted_enrollments = [enrollment.format() for enrollment in enrollments.items]

        return jsonify({
            'success': True,
            'enrollments': formatted_enrollments,
            'total_enrollments': enrollments.total
        })

    @app.route('/enrollments/<int:enrollment_id>')
    def getEnrollment(enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment is None:
            abort(404)

        return jsonify({
            'success': True,
            'enrollment': enrollment.format(),
        })

    @app.route('/enrollments', methods=['POST'])
    def createEnrollment():
        enrollmentData = request.get_json()
        try:
            enrollment = Enrollment(
                course_id=enrollmentData['course_id'],
                student_id=enrollmentData['student_id'],
                professor_id=enrollmentData['professor_id'],
            )
            enrollment.insert()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'enrollment': enrollment.format(),
        })

    @app.route('/enrollments/<int:enrollment_id>', methods=['PUT'])
    def updateEnrollment(enrollment_id):
        enrollmentData = request.get_json()
        enrollment = Enrollment.query.get(enrollment_id)

        if enrollment is None:
            print(sys.exc_info())
            abort(404)

        try:
            enrollment.course_id = enrollmentData['course_id']
            enrollment.student_id = enrollmentData['student_id']
            enrollment.professor_id = enrollmentData['professor_id']
            
            enrollment.update()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'enrollment': enrollment.format(),
        })

    @app.route('/enrollments/<int:enrollment_id>', methods=['DELETE'])
    def deleteEnrollment(enrollment_id):
        enrollment = Enrollment.query.get(enrollment_id)
        if enrollment is None:
            abort(404)

        try:
            enrollment.delete()
        except:
            print(sys.exc_info())
            abort(500)

        return jsonify({
            'success': True,
            'student': enrollment_id,
        })

    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400


    return app






# Default port:
if __name__ == '__main__':
    create_app.run(debug=True)
