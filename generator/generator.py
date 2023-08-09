import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')

Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_en.job()[:25],
        current_address=faker_en.address().replace('\n', ' '),
        permanent_address=faker_en.address().replace('\n', ' '),
    )


def generated_file():
    path = f'/Users/abeazovsky/Desktop/automation_qa_course/filetest{random.randint(0, 999)}'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0,999)}')
    file.close()
    return file.name, path
