from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Users
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')


def registering(request):
    a = request.POST['userid']
    b = request.POST['name']
    c = request.POST['phone']
    d = request.POST['email']
    e = request.POST['vehiclenumber']
    f = request.POST['username']
    g = request.POST['password']

    z = Users(UserId=a,Name=b,Phone=c,Email=d,VehicleNumber=e,Username=f,Password=g)
    z.save()
    return render(request,'registering.html')

def loged(request):
    try:
        a = Users.objects.get(Username=request.POST['username'])
        if a.Password==request.POST['password']:
            return render(request,'loged.html',{'key':a.Username,'key2':a.Name,'key4':a.Email,'key5':a.Phone,'key6':
                                                 a.VehicleNumber})
        else:
            return HttpResponse('Invalid password')
    except:
        return HttpResponse('User does not exist')
