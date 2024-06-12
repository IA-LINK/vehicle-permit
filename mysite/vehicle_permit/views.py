from django.http import HttpResponse
from django.shortcuts import render
from . models import Owner, VechicleDetail



def home(request):
    vehicles = VechicleDetail.objects.all()
    context = {'vechicle_details': vehicles}
    return render(request, 'home/index.html', context)