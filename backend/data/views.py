from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import City, State, Student
import json
import csv
import os

# Create your views here.

@csrf_exempt
def user_csv(request):
    file = request.FILES["file"]

    if (file.endswith('.csv')):
        items = file.readlines()
        columns = items[0].decode("utf-8").strip().split(',')
        data = {}

        for col in columns:
            data[col] = []
        
        for item in items[1:]:
            row_item = item.decode("utf-8").strip().split(',')
            data['student_f_name'].append(row_item[0])
            data['student_l_name'].append(row_item[1])
            data['student_m_name'].append(row_item[2])
            data['student_state'].append(row_item[3])
            data['student_city'].append(row_item[4])
            data['gender'].append(row_item[5])

            print(data)

            state=State.objects.get_or_create(state=row_item[3])
            city=City.objects.get_or_create(state=state,city=row_item[4])

            Student.objects.get_or_create(student_f_name=row_item[0],
                        student_l_name=row_item[1],
                        student_m_name=row_item[2],
                        student_state=state,
                        student_city=city,
                        gender=row_item[5],
                        )

        return(JsonResponse(data=data,safe=False))
    else:
        return HttpResponse("File should be in .csv format with valid data")

def home(request):

    if request.method=="GET":

        data=Student.objects.all()
        students = []
        for student in data:
            val = {
                "student_f_name":student.student_f_name,
                "student_m_name":student.student_m_name,
                "student_l_name":student.student_l_name,
                "student_state":student.student_state.state,
                "student_city":student.student_city.city,
                "gender":student.gender,

            }
            students.append(val)

        print(students)
        return render(request,'home.html',{'students':students})

    if request.method=="POST":

        file = request.FILES["file"]
        if (file.endswith('.csv')):
            items = file.readlines()
            columns = items[0].decode("utf-8").strip().split(',')
            data = {}

            for col in columns:
                data[col] = []
            
            for item in items[1:]:
                row_item = item.decode("utf-8").strip().split(',')
                data['student_f_name'].append(row_item[0])
                data['student_l_name'].append(row_item[1])
                data['student_m_name'].append(row_item[2])
                data['student_state'].append(row_item[3])
                data['student_city'].append(row_item[4])
                data['gender'].append(row_item[5])

                print(data)

                state=State.objects.get_or_create(state=row_item[3])
                city=City.objects.get_or_create(state=state,city=row_item[4])

                Student.objects.get_or_create(student_f_name=row_item[0],
                            student_l_name=row_item[1],
                            student_m_name=row_item[2],
                            student_state=state,
                            student_city=city,
                            gender=row_item[5],
                            )

            return render(request,'home.html',{'students':data})
        else:
            return HttpResponse("File should be in .csv format with valid data")


@csrf_exempt
def download(request):

    result = []
    students = Student.objects.all()
    for student in students:
        data = {
            "student_f_name":student.student_f_name,
            "student_m_name":student.student_m_name,
            "student_l_name":student.student_l_name,
            "student_state":student.student_state.state,
            "student_city":student.student_city.city,
            "gender":student.gender,
        }
        result.append(data)
    columns = result[0].keys()
    with open('students.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, columns)
        dict_writer.writeheader()
        dict_writer.writerows(result)

    file_path = os.path.join('students.csv')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    return render(request,'home.html',{'students':result})
    
