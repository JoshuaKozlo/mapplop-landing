from django.db import models
from django.contrib.gis.geoip import GeoIP

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField('Email',max_length=255,primary_key=True, blank=False)
    full_name = models.CharField('Name',max_length=255, editable=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField('Type', max_length=255, editable=True, null = True, blank=True)
    ip = models.GenericIPAddressField('IP', max_length=200, default='0.0.0.0', editable=True)


    def __str__(self):
    	return str(self.email)