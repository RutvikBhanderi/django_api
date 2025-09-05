"""django_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import ApiOverview,studentlist,addstudent,updatestudent,delstudent,readstudent,studentclassbasedlist, studentViewSet,studentList,studentDetail
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'students', studentViewSet, basename='student'),



urlpatterns = [
        path('health',ApiOverview,name='hth'),
        path('studentlist',studentlist,name='stdli'),
        path('studentlist/<int:id>',studentlist,name='stdlist'),
        path('addstudent',addstudent,name='addstd'),
        path('updatestudent/<int:id>',updatestudent,name='updstd'),
        path('delstudent/<int:id>',delstudent,name='delstd'),
        path('readstudent/<int:id>',readstudent,name='readstd'),
        path('studentclassbaseview/<int:pk>/',studentclassbasedlist.as_view(),name='studentclassbaseview'),
        path('studentclassbaseview/',studentclassbasedlist.as_view(),name='studentclassbaseview'),
        path('studentgenericlist/',studentList.as_view(),name='studentgenericl'),
        path('studentgenericdetail/<int:pk>/',studentDetail.as_view(),name='studentgenericd')
        
]
urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)