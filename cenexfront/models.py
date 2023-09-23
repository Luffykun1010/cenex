from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    company_name=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    pincode=models.CharField(max_length=200)
    def __str__(self):
        return self.company_name