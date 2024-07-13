from djongo import models

class Drink(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=500)

  def __str__(self):
    return self.name + '' + self.description
# User：
# object_id
# userName
# email
# pwd
# program_id
# is_admin

#
from djongo import models
import uuid
class Course(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, default='')
    pre_requisites = models.JSONField(default=list)

    def __str__(self):
        return self.name

class Program(models.Model):
   _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   name = models.CharField(max_length=100)
   term = models.IntegerField(default=3)
   courses = models.JSONField(default=list)
   collegeId = models.UUIDField()

class College(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=100)










