# This module contains entities for some specific application domain,
# namely - for the university

from pony.orm import *
from base_entities import db

class Teacher(db.User):
    degree = Required(str)
    courses = Set("Course")

class Student(db.User):
    group = Required("Group")
    courses = Set("Course")
    gpa = Required(float)

class Group(db.Entity):
    number = PrimaryKey(int)
    students = Set(Student)

class Course(db.Entity):
    name = Required(str)
    students = Set(Student)
    teachers = Set(Teacher)
