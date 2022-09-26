from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request,'admin/admin-index.html')

def admin_view_appointments(request):
    return render(request,'admin/admin-view-appointments.html')

def admin_view_doctors(request):
    return render(request,'admin/admin-view-doctors.html')

def admin_view_patients(request):
    return render(request,'admin/admin-view-patients.html')

def admin_view_feedback(request):
    return render(request,'admin/admin-view-feedback.html')
