from distutils.log import info
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import info
from django.contrib.auth.models import User
 

def hey(request): #this function will accept request ****
    return HttpResponse("Hey")

def fetchdata():
    infooo=info.objects.filter(name='martin')
    print(infooo.values())
    return HttpResponse(infooo.values()) 

 
def registeruser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        print("--------------------------------------->",username)
        user=User.objects.create_user(username=username, password=password1,email=email, first_name=first_name,last_name=last_name)
        user.save()
        print(email," registered")
    else:
        print('error')    

    
    
