from Appform import views
from django.urls import path

urlpatterns = [
    path('',views.stdform,name='stdform')
]