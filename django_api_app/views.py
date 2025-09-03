from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from .models import student
from django_api_app.serlializers import studentSerializer
from rest_framework import viewsets

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
def studentlist(request,id=None):
    if id is not None:
        try:
            r1 = student.objects.get(id=id)
            r2 = studentSerializer(r1)
            return Response({"message":"read successfully","data":r2.data})
        except student.DoesNotExist:
            return Response({"error":"student not found"})        
    else :
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

@api_view(['DELETE'])
def delstudent(request,id):
    try:
        d1 = student.objects.get(id=id)
        d1.delete()
        return Response({"message":"delete successfully"})
    except student.DoesNotExist:
        return Response({"error":"student not found"})

@api_view(['GET'])
def readstudent(request,id):
    try:
        r1 = student.objects.get(id=id)
        r2 = studentSerializer(r1)
        return Response({"message":"read successfully","data":r2.data})
    except student.DoesNotExist:
        return Response({"error":"student not found"})

class studentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = studentSerializer
    queryset = student.objects.all()

class studentclassbasedlist(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get_object(self, id):
        try:
            return student.objects.get(id=id)
        except student.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = studentSerializer(snippet)
        return Response(serializer.data)

    def post(self, request, format=None):
       serializer = studentSerializer(data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id, format=None):
        snippet = self.get_object(id)
        serializer = studentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        d1 = self.get_object(id)
        d1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)