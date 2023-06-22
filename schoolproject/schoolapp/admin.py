from django.contrib import admin
from .models import Student, Course, Department, Material, Purpose, Gender

# Register your models here.
admin.site.register(Student),
admin.site.register(Course),
admin.site.register(Department),
admin.site.register(Material),
admin.site.register(Purpose),
admin.site.register(Gender),
