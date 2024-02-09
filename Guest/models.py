from django.db import models
from Admin.models import *

# Create your models here.

class tbl_user(models.Model):
    user_name=models.CharField(max_length=20)
    user_contact=models.CharField(max_length=20)
    user_email=models.EmailField()
    user_gender=models.CharField(max_length=20)
    user_address=models.TextField()
    user_photo=models.FileField(upload_to='UserDocs/')
    user_proof=models.FileField(upload_to='UserDocs/')
    user_password=models.CharField(max_length=20)
    user_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)