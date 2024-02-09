from django.db import models
from Admin.models import *
# from StationMaster.views import *

# Create your models here.


class tbl_service(models.Model):
    start_point=models.CharField(max_length=10)
    end_point=models.CharField(max_length=10)

class tbl_assignboat(models.Model):
    boat=models.ForeignKey(tbl_boat,on_delete=models.CASCADE)
    service=models.ForeignKey(tbl_service,on_delete=models.CASCADE)
    starttime=models.TimeField()
    arrivaltime=models.TimeField()