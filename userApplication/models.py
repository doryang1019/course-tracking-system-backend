from django.db import models

# Create your models here.

class User(models.Model):
  id = models.AutoField(primary_key=True)
  password = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100,default='')
  last_name = models.CharField(max_length=100, default= '')
  admin = models.BooleanField(default=False)
  programId = models.CharField(max_length=500)



