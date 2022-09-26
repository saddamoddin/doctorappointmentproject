from django.shortcuts import render

# Create your views here.
def confirmation(request):
    return render(request,'user/confirmation.html')

def user_confirm_payment(request):
    return render(request,'user/user-confirm-payment.html')

def user_creditcard(request):
    return render(request,'user/user-creditcard.html')

def user_debitcard(request):
    return render(request,'user/user-debitcard.html')

def user_feedback(request):
    return render(request,'user/user-feedback.html')

def user_find_doctors(request):
    return render(request,'user/user-find-doctors.html')

def user_home(request):
    return render(request,'user/user-home.html')

def user_make_appointment(request):
    return render(request,'user/user-make-appointment.html')

def user_netbanking(request):
    return render(request,'user/user-netbanking.html')

def user_video_consult_payment(request):
    return render(request,'user/user-video-consult-payment.html')

def user_video_consult(request):
    return render(request,'user/user-video-consult.html')

def user_view_doctor_profile(request):
    return render(request,'user/user-view-doctor-profile.html')

 