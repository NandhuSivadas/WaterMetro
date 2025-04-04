from django.db import models
from Admin.models import *
from Guest.models import *
from StationMaster.models import *

# Create your models here.

# class tbl_ticketbooking(models.Model):
#     date=models.DateField()
#     Passenger_count=models.CharField(max_length=10)
#     ticket_type=models.ForeignKey(tbl_tickettype,on_delete=models.CASCADE)
#     book_amount=models.CharField(max_length=10)
#     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
#     assign = models.ForeignKey(tbl_assignboat,on_delete=models.CASCADE,null=True)
#     status = models.IntegerField(default=0)


class tbl_ticketbooking(models.Model):
    date = models.DateField()
    service_from = models.ForeignKey(tbl_service, on_delete=models.CASCADE, related_name="service_from")
    service_to = models.ForeignKey(tbl_service, on_delete=models.CASCADE, related_name="service_to")
    Passenger_count = models.CharField(max_length=10)
    
    book_amount = models.CharField(max_length=10)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    assign = models.ForeignKey(tbl_assignboat, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=0)


class tbl_complaint(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)
    reply=models.CharField(max_length=100)

class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    booking_amount=models.CharField(max_length=50)
    booking_status=models.CharField(max_length=10,default=0)
    payment_status=models.CharField(max_length=10,default=0)

class tbl_cart(models.Model):
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_qty=models.IntegerField()
    food=models.ForeignKey(tbl_food,on_delete=models.CASCADE)
    cart_status=models.CharField(max_length=10,default=0)

class tbl_eventbooking(models.Model):
    date=models.DateField()
    Passenger_count=models.CharField(max_length=10)
    tickettype=models.CharField(max_length=10)
    book_amount=models.CharField(max_length=10)
    details=models.CharField(max_length=80)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    assign = models.ForeignKey(tbl_assignboat,on_delete=models.CASCADE,null=True)
    status = models.IntegerField(default=0)

class tbl_review(models.Model):
    review=models.CharField(max_length=100)
