from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from faker import Faker
import random


engine = create_engine('sqlite:///file.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

student_courses = Table('student_courses', Base.metadata,
                        Column('student_id', Integer, ForeignKey('students.id')),
                        Column('course_id', Integer, ForeignKey('courses.id')))


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    courses = relationship('Course', secondary=student_courses, back_populates='students')

    def __str__(self):
        return f'Student - id={self.id}, name={self.name}, age={self.age}'


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    students = relationship('Student', secondary=student_courses, back_populates='courses')

    def __str__(self):
        return f'Course - id={self.id}, title={self.title}'


Base.metadata.create_all(engine)
fake = Faker()

list_of_courses = ['Colonization', 'Cybersecurity', 'Wormholes', 'Bioengineering', 'Time Travel']
for i in range(len(list_of_courses)):
    course = Course(title=list_of_courses[i])
    session.add(course)
session.commit()

courses = session.query(Course).all()
for _ in range(20):
    student = Student(name=fake.name(), age=random.randrange(18, 60))
    student.courses = random.sample(courses, random.randint(1, 5))
    session.add(student)
session.commit()


def add_student(name, age, course_titles):
    student = Student(name=name, age=age)
    student.courses = session.query(Course).filter(Course.title.in_(course_titles)).all()
    session.add(student)
    session.commit()


def update_student(student_id, course_titles):
    student = session.get(Student, student_id)
    if not student:
        print(f'Student with id={student_id} not found')
        return

    select_courses = session.query(Course).filter(Course.title.in_(course_titles)).all()
    if not select_courses:
        print(f'There are no courses in the database {course_titles}')
        return

    student.courses = select_courses
    session.commit()


def update_courses(new_courses):
    for i in range(len(new_courses)):
        course = Course(title=new_courses[i])
        session.add(course)
    session.commit()


def get_courses_from_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        print(f'Student with id={student_id} not found')
        return
    print(f'Student {student.name} with id={student_id} is studying on courses '
          f'{[course.title for course in student.courses]}')


def get_students_from_course(course_id):
    select_courses = session.query(Course).filter(Course.id == course_id).first()
    if not select_courses:
        print(f'Course with id={course_id} not found')
        return
    print(f'The following list of students:')
    print(f'{[student.name for student in select_courses.students]}')
    print(f'study in the "{select_courses.title}" course')


def delete_student(student_id):
    student = session.query(Student).filter(Student.id == student_id).first()
    if not student:
        print(f'Student with id={student_id} not found')
        return
    else:
        session.delete(student)
        session.commit()


if __name__ == '__main__':
    course_titles = ['Colonization', 'Cybersecurity']
    add_student(name='Vladimir Monomakh', age=39, course_titles=course_titles)
    update_student(student_id=21, course_titles=['Time Travel', 'Wormholes'])
    update_courses(new_courses=['Math'])
    get_courses_from_student(student_id=8)
    get_students_from_course(course_id=5)
    delete_student(student_id=21)
