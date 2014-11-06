from datetime import date, datetime
from pony.orm import *
from all_entities import *

# This function will populate database with some example data

@db_session
def populate_database():
    g1 = Group(number=123)
    s1 = Student(name='John', dob=date(1990, 1, 1),
                 login='John', password='***', email='jogn@example.com',
                 group=g1, gpa=4.5)
    s2 = Student(name='Mike', dob=date(1992, 1, 1),
                 login='Mike', password='***', email='mike@example.com',
                 group=g1, gpa=4.5)
    p1 = Teacher(name='Donald Knuth', dob=date(1938, 1, 10),
                 login='dknuth', password='***', email='dknuth@example.com',
                 degree='Professor')
    c = Course(name='Math', teachers=[p1], students=[s1, s2])

    f1 = Forum(name='Math 101')
    t1 = Topic(name='What is the result of 2 x 2', forum=f1, author=s1,
               text="Really, tell me the truth!")
    Comment(topic=t1, author=s2, text="I don't know, maybe 5?")
    Comment(topic=t1, author=p1,
            text="This question is too advanced for this forum!")
