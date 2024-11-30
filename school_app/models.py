from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class School(models.Model):
    region=models.ForeignKey(Region, null=True, blank=True, on_delete=models.SET_NULL)
    district=models.ForeignKey(District, null=True, blank=True, on_delete=models.SET_NULL)
    name=models.CharField(max_length=100)
    adress=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    full_name=models.CharField(max_length=100)
    school=models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    subject=models.ForeignKey(Subject, null=True, blank=True, on_delete=models.SET_NULL)
    position=models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Class (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Pupil (models.Model):
    full_name = models.CharField(max_length=100)
    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.SET_NULL)
    klass = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)
    klass_teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.full_name


