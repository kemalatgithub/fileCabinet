from django.db import models

# Create your models here.
class Region(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'region'
    def __str__(self):
      return self.name
class Zone(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'zone'
    def __str__(self):
      return self.name
class Woreda(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'woreda'
    def __str__(self):
      return self.name
class Kebele(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'kebele'
    def __str__(self):
      return self.name
class Nation(models.Model):
    name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'nation'
    def __str__(self):
      return self.name