from djongo import models

class College(models.Model):
  id = models.ObjectIdField(primary_key=True)
  name = models.CharField(max_length=100)
