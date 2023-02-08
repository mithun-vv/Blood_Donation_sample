from django.db import models

# Create your models here.

class BloodGroup(models.Model):
    b_group = models.CharField(max_length=3)
    def __str__(self):
        return self.b_group

class Gender(models.Model):
    gender = models.CharField(max_length=1)
    def __str__(self):
        return self.gender
    
class DyfiUnit(models.Model):
    unit = models.CharField(max_length=100)
    def __str__(self):
        return self.unit


class Contact(models.Model):
    Name =models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    contact_date = models.DateField(auto_now=True)


class Index_bgs(models.Model):
    b_dyfi_unit = models.ForeignKey(DyfiUnit, on_delete=models.DO_NOTHING)
    b_name = models.CharField(max_length=50)
    b_fathers_name = models.CharField(max_length=50)
    b_group = models.ForeignKey(BloodGroup, on_delete=models.DO_NOTHING)
    b_gender = models.ForeignKey(Gender, on_delete=models.DO_NOTHING)
    b_age = models.CharField(max_length=2)
    b_donated = models.DateField()
    



class SearchResult(models.Model):
    bd_group = models.ForeignKey(BloodGroup,on_delete=models.DO_NOTHING)

