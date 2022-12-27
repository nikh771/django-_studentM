import json
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import STUDENT
from django.conf import settings
from django.core.cache import cache
# Create your views here.



@csrf_exempt
def student(request):
    if request.method == "POST":
        data =json.loads(request.body)
        std=StudentSerializer(data=data)
        
        if std.is_valid():
            std.save()
            return HttpResponse({"success"})

        return HttpResponse(StudentSerializer.errors)


   

@api_view(('GET',))
def get_student(request):
    if cache.get('STUDENT'):
        student=cache.get('STUDENT')
        # print("data from caches")
        serializer = StudentSerializer(student, many=True)
        return Response({"status": "success", "data": serializer.data})

    else:
        student =STUDENT.objects.all()
        cache.set('STUDENT',student,timeout=5)
        # print("data from db")
        serializer = StudentSerializer(student, many=True)
        return Response({"status": "success", "data": serializer.data})



@api_view(('GET',))
def search_student(request,id):
    if cache.get(id):
        student=cache.get(id)
        std_data = StudentSerializer(student)
        # print("data from caches")
        return Response(std_data.data)

    else:
        student =STUDENT.objects.get(rollno=id)
        if student:
            cache.set(id,student)
            std_data = StudentSerializer(student)
            # print("data from db")
            return Response(std_data.data)
        else:
            return HttpResponse({"No Details Found"})


@api_view(('PUT',))
def update_student(request,id):
    student = STUDENT.objects.get(rollno=id)
    if student:
        data = json.loads(request.body)
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
    else:
        return HttpResponse({"No Details Found"})


@csrf_exempt
def delete_student(request,id):
    if request.method == "DELETE":
        student = STUDENT.objects.get(rollno=id)
        if student is not None:
            student.delete()
            return HttpResponse({"success"})

        else:
            return HttpResponse({"No Details Found"})
