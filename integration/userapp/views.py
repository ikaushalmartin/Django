 
from django.http import HttpResponse, JsonResponse
 
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect 




def hey(request): #this function will accept request ****
    return HttpResponse("Hey")


 
def registeruser(request):
     if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        print("--------------------------------------->",username)

        if(password1!=password2):
            return HttpResponse("Both password is not same")

        elif(User.objects.filter(email=email).exists()):
            return HttpResponse("Email already exist")
        else:
            user=User.objects.create_user(username=username, password=password1,email=email, first_name=first_name,last_name=last_name)
            user.save()
           
            return HttpResponse(email," registered")
   
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        print('username',username,'password',password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return HttpResponse("Success")
        else:
            return HttpResponse("invalid")       


def logout(request):
    auth.logout(request)
    return HttpResponse("Logged Out")