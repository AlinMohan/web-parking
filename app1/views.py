from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Users
from django.contrib.auth import logout

# from django.contrib.auth.views import LogoutView
# from django.http import HttpResponseRedirect
from django.urls import reverse

from app1.models import ParkingSlot
from app1.models import BookedSlot

from django.contrib.auth.decorators import login_required
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
    # a = request.POST['userid']
    b = request.POST['name']
    c = request.POST['phone']
    d = request.POST['email']
    e = request.POST['vehiclenumber']
    f = request.POST['username']
    g = request.POST['password']

    z = Users(Name=b,Phone=c,Email=d,VehicleNumber=e,Username=f,Password=g)
    z.save()
    return render(request,'registering.html')

def loged(request):
    try:
        a = Users.objects.get(Username=request.POST['username'])
        if a.Password==request.POST['password']:
            return render(request,'loged.html',{'key':a.Username,'key2':a.Name,'key4':a.Email,'key5':a.Phone,'key6':
                                                 a.VehicleNumber})
        else:
            return render(request,'invalidpassword.html')
    except:
        return render(request,'invaliduser.html')

# @login_required(login_url='/login')
def loggedout(request):
    logout(request)
    return redirect('login')    

    
# class CustomLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         response = super().dispatch(request, *args, **kwargs)

#         # Add a custom message to the redirect URL
#         redirect_url = reverse('login')  # Change 'home' to your desired home or landing page
#         logout_message = "You have been successfully logged out."
#         redirect_url += f'?logout_message={logout_message}'

#         return HttpResponseRedirect(redirect_url)
    
# @login_required(login_url='/login')   
def view_parking_slots(request):
    slots = ParkingSlot.objects.all()
    booked_slots = BookedSlot.objects.all()
    return render(request, 'viewslot.html', {'slots': slots, 'booked_slots': booked_slots})  

# @login_required(login_url='/login')
def book_slot(request, slot_id):
    slot = ParkingSlot.objects.get(pk=slot_id)

    if not slot.is_available:
        # The slot is already booked
        return redirect('view_parking_slots')

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        booking_time = request.POST.get('datetime')
        BookedSlot.objects.create(slot=slot, user_name=user_name,booking_time=booking_time)
        slot.is_available = False
        slot.save()
        return redirect('view_parking_slots')

    return render(request, 'book_slot.html', {'slot': slot})

  

