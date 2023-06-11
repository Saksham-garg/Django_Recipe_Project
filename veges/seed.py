from faker import Faker
import random
from .models import *
fake = Faker()

def seed_db(n = 10) -> None:
    try:
        for _ in range(n):
            random_index = random.randint(0,len(Department.objects.all())-1)
            department = Department.objects.all()[random_index]
            student_id = f'STU_0{random.randint(100,999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_ID = StudentID.objects.create(student_id = student_id)

            Student.objects.create(
                department = department,
                student_id = student_ID,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)
