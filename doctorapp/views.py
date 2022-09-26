from django.shortcuts import render

# Create your views here.
def doctor_add_appointment_details(request):
    return render(request,'doctor/doctor-add-appointment-details.html')

def doctor_add_profile(request):
    return render(request,'doctor/doctor-add-profile.html')

def doctor_edit_appointment_details(request):
    return render(request,'doctor/doctor-edit-appointment-details.html')

def doctor_edit_profile(request):
    return render(request,'doctor/doctor-edit-profile.html')

def doctor_index(request):
    return render(request,'doctor/doctor-index.html')

def doctor_profile(request):
    return render(request,'doctor/doctor-profile.html')

def doctor_view_appointment_details(request):
    return render(request,'doctor/doctor-view-appointment-details.html')

def doctor_view_appointment(request):
    return render(request,'doctor/doctor-view-appointments.html')

def doctor_view_feedback(request):
    return render(request,'doctor/doctor-view-feedback.html')

    

