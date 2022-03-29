from django.contrib import admin
from .models import State, City, Student
# Register your models here.

admin.site.register(Student)
admin.site.register(State)
admin.site.register(City)

