from django.db import models

# Create your models here.
class Cat:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

cats = [
    Cat('Felix', 'ally cat', 'trouble maker', 5),
    Cat('Harvey', 'sphynx', 'black', 2),
    Cat('Mittins', 'siamese', 'very friendly', 14)
]