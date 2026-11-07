from app import app, db
from models import Student, Major, User
from werkzeug.security import generate_password_hash
import datetime as dt

with app.app_context():
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Add Celia as an Information Systems student
    major = Major.query.filter_by(major='Information Systems').one()
    celia = Student(
        first_name='Celia',
        last_name='Pham',
        email='celia.pham121@terpmail.umd.edu',
        major_id=major.major_id,
        birth_date=dt.datetime(2005, 1, 15),
        is_honors=False
    )
    db.session.add(celia)

    # Add Celia STUDENT account using a hashed password
    elms_username = 'cpham121'
    celia_user = User(
        username=elms_username,
        first_name='Celia',
        last_name='Pham',
        email='celia.pham121@terpmail.umd.edu',
        password=generate_password_hash(elms_username),
        role='STUDENT'
    )
    db.session.add(celia_user)
    db.session.commit()

    # Add a separate ADMIN account using a hashed password
    admin_username = 'cpham121_admin'
    admin_user = User(
        username=admin_username,
        first_name='Celia',
        last_name='Pham',
        email='cpham_admin',
        password=generate_password_hash(admin_username),
        role='ADMIN'
    )
    db.session.add(admin_user)
    db.session.commit()

    # Add a separate MANAGER account using a hashed password
    manager_username = 'cpham121_manager'
    manager_user = User(
        username=manager_username,
        first_name='Celia',
        last_name='Pham',
        email='cpham_manager',
        password=generate_password_hash(manager_username),
        role='MANAGER'
    )
    db.session.add(manager_user)
    db.session.commit()

    # Initial loading of students first_name, last_name, email, major_id, birth_date, is_honors
    students = [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', 'email': 'robert.smith@example.com', 'major_id':3,
            'birth_date': dt.datetime(2007, 6, 1), 'is_honors':1},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', 'email': 'leo.vanmunching@example.com', 'major_id':6,
         'birth_date': dt.datetime(2008, 3, 24), 'is_honors': 0},
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            email=each_student["email"],
                            major_id=each_student["major_id"], birth_date=each_student["birth_date"],
                            is_honors=each_student["is_honors"])
        db.session.add(a_student)
        db.session.commit()


