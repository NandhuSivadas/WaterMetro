from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.

class tbl_ticketbooking(models.Model):
    date=models.DateField()
    Passenger_count=models.CharField(max_length=10)
    ticket_type=models.ForeignKey(tbl_tickettype,on_delete=models.CASCADE)
    book_amount=models.CharField(max_length=10)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)
    reply=models.CharField(max_length=100)