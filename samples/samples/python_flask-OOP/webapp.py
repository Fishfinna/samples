from flask import Flask, render_template, request
from models.school import School
import json
import requests

app = Flask(__name__)


@app.route("/")
def home():
    """display home table"""
    school = School("BCIT")
    if len(school) == 0:
        return "", 201
    return render_template("home.html", school=school)


@app.route("/students", methods=["GET"])
def get_students():
    """Returns all student json"""
    school = School("BCIT")
    students = [i.to_dict() for i in school.students]
    return json.dumps(students)


@app.route("/student", methods=["POST"])
def post_student():
    """Used to add student content to the school"""
    school = School("BCIT")
    start_stu = school.students
    data = request.json

    # a series of checks to ensure the valid input of data
    name = data.get("name")
    if name == None:
        return "Error:401", 401

    sid = data.get("student_id")
    if sid == None:
        return "Error:401", 401

    term = data.get("term")
    if term == None:
        return "Error:401", 401

    try:
        school.add(data)  # add content to the school
        school.save()  # store content
        end_stu = school.students

        if start_stu == end_stu:  # ensure the content has changed
            return "", 201
    except:
        return "", 400


@app.route("/student/<studentID>", methods=["GET"])
def get_student(studentID):
    """Returns JSON with specific student info"""
    school = School("BCIT")
    data = request.json
    cur_ids = [i.student_id for i in school.students]
    if studentID not in cur_ids:
        return "", 404
    student = school.get_by_id(studentID)
    if school.get_by_id(studentID) == " ":
        return "Error: student not found", 404
    if hasattr(data, "name"):
        if data.name != student.name:
            return 404

    return json.dumps(school.get_by_id(studentID).to_dict()), 200


@app.route("/student/<studentID>", methods=["PUT"])
def put_student(studentID):
    """updates a specific student with the provided information"""
    data = request.json
    school = School("BCIT")

    student = school.get_by_id(studentID)

    if data.get("name") == None:
        return "Name note found", 404
    try:
        student.name = data.get("name")
        data_id = data.get("student_id")
        if None != data_id:
            student.student_id = data_id
        school.save()
        return "Student Updated", 201
    except Exception:
        return "", 404


@app.route("/student/<studentID>", methods=["DELETE"])
def delete_student(studentID):
    """Used to delete students from the file"""
    school = School("BCIT")

    if school.get_by_id(studentID) == None:
        return "", 404

    try:
        school.delete(studentID)
        school.save()
        return "User deleted", 201
    except Exception:
        return "", 404


if __name__ == "__main__":
    app.run(debug=True)
