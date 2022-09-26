"""doctorappointmentproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from mainapp import views as main_views
from userapp import views as user_views
from doctorapp import views as doctor_views
from adminapp import views as admin_views


urlpatterns = [
    path('admin/', admin.site.urls),
    #Comments for Main  Urls
    path('',main_views.home,name='home'),
    path('about',main_views.about,name='about'),
    path('admin-login',main_views.admin_login,name='admin-login'),
    path('doctor-login',main_views.doctor_login,name='doctor-login'),
    path('doctor-register',main_views.doctor_register,name='doctor-register'),
    path('user-login',main_views.user_login,name='user-login'),
    path('user-register',main_views.user_register,name='user-register'),
    path('contact',main_views.contact,name='contact'),


    # comments for User urls
    path('confirmation',user_views.confirmation,name='confirmation'),
    path('user-confirm-payment',user_views.user_confirm_payment,name='user-payment-confirm'),
    path('creditcard',user_views.user_creditcard,name='user-credit-card'),
    path('debitcard',user_views.user_debitcard,name='user-debit-card'),
    path('feedback',user_views.user_feedback,name='user-feedback'),
    path('find-doctors',user_views.user_find_doctors,name='user-find-doctors'),
    path('user-home',user_views.user_home,name='user-home'),
    path('make-appointment',user_views.user_make_appointment,name='user-make-appointment'),
    path('netbanking',user_views.user_netbanking,name='user-netbanking'),
    path('video-consult-payment',user_views.user_video_consult_payment,name='user-video-consult-payment'),
    path('video-consult',user_views.user_video_consult,name='user-video-consult'),
    path('doctor-profile',user_views.user_view_doctor_profile,name='user-view-doctor-profile'),
   
    # comments for doctor urls
    path('doctor-index',doctor_views.doctor_index,name='doctor-index'),
    path('add-appointment',doctor_views.doctor_add_appointment_details,name='add-appointment-details'),
    path('add-profile',doctor_views.doctor_add_profile,name='add-profile'),
    path('edit-appointment',doctor_views.doctor_edit_appointment_details,name='edit-appointment-details'),
    path('edit-profile',doctor_views.doctor_edit_profile,name='edit-profile'),
    path('view-profile',doctor_views.doctor_profile,name='view-profile'),
    path('view-appointment-details',doctor_views.doctor_view_appointment_details,name='view-appointment-details'),
    path('view-appointments',doctor_views.doctor_view_appointment,name='view-appointments'),
    path('view-feedback',doctor_views.doctor_view_feedback,name='view-feedback'),

    #comments for admin urls
    path('admin-index',admin_views.admin_index,name='admin-index'),
    path('admin-view-appointments',admin_views.admin_view_appointments,name='admin-view-appointments'),
    path('admin-view-doctors',admin_views.admin_view_doctors,name='admin-view-doctors'),
    path('admin-view-feedback',admin_views.admin_view_feedback,name='admin-view-feedback'),
    path('admin-view-patients',admin_views.admin_view_patients,name='admin-view-patients'),

]
