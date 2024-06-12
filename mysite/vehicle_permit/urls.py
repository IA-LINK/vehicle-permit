from django.urls import path 
from vehicle_permit  import views 



urlpatterns = [
    path('', views.home, name='home'),
    
]
