from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('about/',views.about,name ='about'),
    path('contactus/',views.contactus,name ='contactus'),
    path('privacy/',views.privacy,name ='privacy'),
    path('career/',views.career,name ='career'),
    path('tandc/',views.tandc,name ='tandc'),
]
