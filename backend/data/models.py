from django.db import models

# Create your models here.

class State(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.CharField(max_length=50)

    def __str__(self):
        return self.state


class City(models.Model):
    id=models.AutoField(primary_key=True)
    state=models.ForeignKey(State,on_delete=models.CASCADE,default=None) #if categories needed
    city=models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    student_f_name=models.CharField(max_length=100)
    student_m_name=models.CharField(max_length=100)
    student_l_name=models.CharField(max_length=100)
    student_state=models.ForeignKey(State,on_delete=models.CASCADE)
    student_city=models.ForeignKey(City,on_delete=models.CASCADE)
    gender=models.CharField(choices=[("Male","male"),("Female","female"),("Others","others")],max_length=10)

    def __str__(self):
        return (self.student_f_name+" "+self.student_l_name)

