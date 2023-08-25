import os
import random
from data.data import Person
from faker import Faker
from PIL import Image, ImageDraw

faker_ru = Faker('ru_RU')
faker_en = Faker('en_US')

Faker.seed()


def generated_person():
    yield Person(
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        first_name=faker_en.first_name()[:25],
        last_name=faker_en.last_name()[:25],
        email=faker_en.email(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_en.job()[:25],
        current_address=faker_en.address().replace('\n', ' '),
        permanent_address=faker_en.address().replace('\n', ' '),
        phone_number=int(''.join(filter(str.isdigit, faker_en.basic_phone_number()))),
    )


def generated_file():
    path = f'/Users/abeazovsky/Desktop/automation_qa_course/filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 999)}')
    file.close()
    return file.name, path


def generate_jpeg():
    # Create a new image with a white background
    width, height = random.randint(1, 1920), random.randint(1, 1080)
    # RGB color
    background_color = tuple(random.randint(0, 255) for _ in range(3))
    image = Image.new('RGB', (width, height), background_color)
    # Create a drawing object
    draw = ImageDraw.Draw(image)
    # Rectangle RGB color
    rectangle_color = tuple(random.randint(0, 255) for _ in range(3))
    # Rectangle coordinates (Left, Upper, Right, Lower)
    x0 = random.randint(1, width-1)
    x1 = random.randint(x0, width)
    y0 = random.randint(1, height-1)
    y1 = random.randint(y0, height)
    rectangle_coords = (x0, y0, x1, y1)
    draw.rectangle(rectangle_coords, fill=rectangle_color)
    parent_directory = os.path.dirname(os.getcwd())
    path = f'{parent_directory}/output_image{random.randint(0, 999)}.jpg'
    # Save the image as a JPEG file
    image.save(path, 'JPEG')
    return path
