from atexit import register
from sre_constants import SUCCESS
from unicodedata import name
from django.shortcuts import redirect, render
from mainapp.models import *
import re
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'main/index.html')

def about(request):
    return render(request,'main/about.html')

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username == 'admin' and password == 'admin':
           
            return redirect('admin-index')
        else:
            pass    

    return render(request,'main/admin-login.html')

def doctor_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        try:
            check = DoctorAppointmentModel.objects.get(name=name,password=password)

            request.session["doctor_id"] = check.doctor_id

            return redirect ("admin-index")
        
        except:
            print("error")

    return render(request,'main/doctor-login.html')

def doctor_register(request):
    if request.method =='POST':
        print("This is Post method")
        name = request.POST.get('name')
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        if len(name) > 10:
            messages.error (request, "user name must be 10 characters")
        elif not name.isalpha():
            print("username should only contain letters")
            messages.error (request, "username should only contain letters")
        elif len(password) < 8:
            messages.error (request, "Make sure your password is atleast 8 letters")
        elif re.search('[0-9]', password) is None:
            messages.error (request, "Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None:
            messages.error (request, "Make sure your password has a capital letter in it")
        elif DoctorAppointmentModel.objects.filter(gmail=gmail).exists():
            messages.error (request, "Email alredy exist")
            return render(request,'main/doctor-register.html')
        # print(password)
        else:
            doctor_register = DoctorAppointmentModel.objects.create(name=name,gmail=gmail,password=password)
            doctor_register.save()
            messages.success(request, "Accout created successful")
            return render(request,'main/doctor-login.html')
            
            
    return render(request,'main/doctor-register.html')

def user_login(request):

    return render(request,'main/user-login.html')

def user_register(request):

    return render(request,'main/user-register.html')

def contact(request):
    return render(request,'main/contact.html')

