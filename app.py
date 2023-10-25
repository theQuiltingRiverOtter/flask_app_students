from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///students"

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    grade = db.Column(db.String(1))

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


@app.route("/old_students", methods=["GET"])
def old_students():
    students = Student.query.filter(Student.age > 20)
    return jsonify(
        [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
            }
            for student in students
        ]
    )


@app.route("/young_students", methods=["GET"])
def young_students():
    students = Student.query.filter(Student.age < 21)
    return jsonify(
        [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
            }
            for student in students
        ]
    )


@app.route("/advance_students", methods=["GET"])
def advance_students():
    students = Student.query.filter(Student.grade == "A")
    return jsonify(
        [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
            }
            for student in students
        ]
    )


@app.route("/student_names", methods=["GET"])
def student_names():
    students = Student.query.all()
    return jsonify(
        [
            {
                "first_name": student.first_name,
                "last_name": student.last_name,
            }
            for student in students
        ]
    )


@app.route("/student_ages", methods=["GET"])
def student_ages():
    students = Student.query.all()
    return jsonify(
        [
            {"name": student.first_name + " " + student.last_name, "age": student.age}
            for student in students
        ]
    )


@app.route("/students/grades", methods=["GET"])
def get_students_by_grade():
    grade = request.args.get("grade", default=None)
    students = Student.query.filter(Student.grade == grade)
    return jsonify(
        [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
            }
            for student in students
        ]
    )


@app.route("/students/student", methods=["GET"])
def get_student_by_id():
    id = request.args.get("id", default=1, type=str)
    found_student = Student.query.get(id)
    return jsonify(
        {
            "id": found_student.id,
            "first_name": found_student.first_name,
            "last_name": found_student.last_name,
            "age": found_student.age,
            "grade": found_student.grade,
        }
    )


@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify(
        [
            {
                "id": student.id,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "age": student.age,
                "grade": student.grade,
            }
            for student in students
        ]
    )


app.run(debug=True)
