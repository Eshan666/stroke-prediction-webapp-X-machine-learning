from django.db import models
from django.db.models.fields import FloatField, IntegerField
from django.contrib.auth.models import User

# Create your models here.


class Dataset(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    age = models.IntegerField(null=True)
    hypertension = models.IntegerField(null=True)
    heartDisease = models.IntegerField(null=True)
    glucose = FloatField(null=True)
    bmi = models.IntegerField(null=True)
    gender = models.IntegerField(null=True)
    married = models.IntegerField(null=True)
    workType = models.IntegerField(null=True)
    Residence = models.IntegerField(null=True)
    smoking = models.IntegerField(null=True)
    result = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

class Prediction(models.Model):
    patient = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
    dataset = models.ForeignKey(Dataset,null=True,on_delete=models.SET_NULL)
    result = models.IntegerField(null=True)
    date_predicted = models.DateTimeField(auto_now_add=True, null=True)

