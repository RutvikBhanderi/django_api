from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import student
from django_api_app.serlializers import studentSerializer

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)

@api_view(['GET'])
def studentlist(request):
    x=student.objects.all()
    y=studentSerializer(x,many=True)
    print(x)
    
    return Response({"message":"success","data":y.data})

@api_view(['POST'])
def addstudent(request):
    a1 = studentSerializer(data=request.data)
    if a1.is_valid():
        a1.save()
        return Response({"message":"added successfully","data":a1.data})
    else:
        return Response({"error":a1.errors})
   

@api_view(['POST'])
def updatestudent(request,id):
    g1 = student.objects.get(id=id)
    u1 = studentSerializer(g1,data=request.data)
    if u1.is_valid():
        u1.save()
        return Response({"message":"update successfully","data":u1.data})
    else:
        return Response({"error":u1.errors})

@api_view(['GET'])
def delstudent(request):

    return Response()