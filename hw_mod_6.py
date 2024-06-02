import psycopg2
import random
from faker import Faker

fake = Faker()

conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cur = conn.cursor()

# Create groups
groups = []
for i in range(3):
    group_name = fake.company()
    cur.execute("INSERT INTO groups (name) VALUES (%s) RETURNING id", (group_name,))
    group_id = cur.fetchone()[0]
    groups.append(group_id)

# Create students
students = []
for i in range(40):
    student_name = fake.name()
    group_id = random.choice(groups)
    cur.execute("INSERT INTO students (name, group_id) VALUES (%s, %s) RETURNING id", (student_name, group_id))
    student_id = cur.fetchone()[0]
    students.append(student_id)

# Create teachers
teachers = []
for i in range(5):
    teacher_name = fake.name()
    cur.execute("INSERT INTO teachers (name) VALUES (%s) RETURNING id", (teacher_name,))
    teacher_id = cur.fetchone()[0]
    teachers.append(teacher_id)

# Create subjects
subjects = []
for i in range(7):
    subject_name = fake.word()
    teacher_id = random.choice(teachers)
    cur.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id", (subject_name, teacher_id))
    subject_id = cur.fetchone()[0]
    subjects.append(subject_id)

# Create grades
for student_id in students:
    for subject_id in subjects:
        grade = round(random.uniform(1.0, 5.0), 2)
        cur.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)", (student_id, subject_id, grade))

conn.commit()
cur.close()
conn.close()