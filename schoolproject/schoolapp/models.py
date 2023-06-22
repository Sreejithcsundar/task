from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Purpose(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Gender(models.Model):
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender


class Student(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.ForeignKey(Purpose, on_delete=models.CASCADE)
    materials_provide = models.ManyToManyField(Material)

    def __str__(self):
        return self.name

