from django.db import models

# Create your models here.
class DoctorAppointmentModel(models.Model):
    doctor_id = models.AutoField(primary_key = True)
    name = models.TextField(help_text="Enter Your Name",max_length=200)
    gmail = models.EmailField(help_text="Enter Gmail",max_length=200)
    password = models.CharField(help_text="Enter Password",max_length=200)
    class Meta:
        db_table='Appointment_Details'

      
            
class UserModel(models.Model):
    doctor_id = models.AutoField(primary_key = True)
    user_name = models.TextField(help_text = "Enter Your Name",max_length = 30)
    user_email = models.EmailField(help_text = "Enter Your Email" ,max_length = 20)
    user_contact = models.BigIntegerField(help_text = "Enter Your Contact Number")
    # user_profile = models.ImageField(help_text = "Upload Your Image") 
    user_gender = models.CharField(max_length=50)
    user_dob = models.DateField()
    user_password = models.CharField(help_text = "Enter Your Password" , max_length=50)
    class Meta:
        db_table = 'user_details'