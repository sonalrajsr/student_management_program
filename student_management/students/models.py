from django.db import models

# Create your models here.
class students(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    department = models.CharField(max_length = 50)
    email = models.EmailField()
    roll_number = models.CharField(max_length = 10)
    date_of_birth = models.DateField()
    # profile_photo = models.ImageField(upload_to=)