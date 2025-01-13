from django.db import models

# Create your models here.

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=10)
    admin_email=models.CharField(max_length=10)
    admin_password=models.CharField(max_length=10)

class tbl_district(models.Model):
    district_name=models.CharField(max_length=10)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=20)
    place_pincode=models.CharField(max_length=6)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)


class tbl_stationmaster(models.Model):
    master_name=models.CharField(max_length=20)
    master_contact=models.CharField(max_length=20)
    master_email=models.EmailField()
    master_gender=models.CharField(max_length=20)
    master_address=models.TextField()
    master_photo=models.FileField(upload_to='UserDocs/')
    master_proof=models.FileField(upload_to='UserDocs/')
    master_password=models.CharField(max_length=20)
    


class tbl_eventtype(models.Model):
    event_type=models.CharField(max_length=10)
    
class tbl_tickettype(models.Model):
    ticket_type=models.CharField(max_length=10)
    ticket_type_rate=models.CharField(max_length=10)

class tbl_boat(models.Model):
    boat_name=models.CharField(max_length=10)
    boat_capacity=models.IntegerField()
    boat_entrydate=models.DateField()
    
class tbl_addevent(models.Model):
    addevent_title=models.CharField(max_length=50)
    addevent_eventtype=models.ForeignKey(tbl_eventtype,on_delete=models.CASCADE)
    addevent_details=models.CharField(max_length=50)
    addevent_passengercount=models.IntegerField()
    addevent_rate=models.IntegerField()

class tbl_food(models.Model):
    food_name=models.CharField(max_length=50)
    food_description=models.CharField(max_length=60)
    food_image=models.FileField(upload_to='FoodDocs/')
    food_rate=models.IntegerField()   

class tbl_stock(models.Model):
    stock_name=models.CharField(max_length=50)
    product = models.ForeignKey(tbl_food,on_delete=models.CASCADE)
 
