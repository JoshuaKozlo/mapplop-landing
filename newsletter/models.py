from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField('Email',max_length=255,primary_key=True, blank=False)
    full_name = models.CharField('Name',max_length=255, editable=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip = models.GenericIPAddressField('IP', max_length=200, default='0.0.0.0', editable=True)