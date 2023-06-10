from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    choices = (
        ('M','Male'),
        ('F',"Female")
    )
    Gender = models.CharField(max_length=1,choices=choices)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=50)
    speed = models.IntegerField(default=50)

