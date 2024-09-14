from django.urls import path
from .import  views 

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('predict/', views.employee_predict, name='employee_predict'),
    
    
]
