from django.db import models

# Create your models here.
class Role(models.Model):
    role_name= models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'role'
    def __str__(self):
      return self.role_name
class WorkunitList(models.Model):
    name =models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'workunit'
    def __str__(self):
      return self.name