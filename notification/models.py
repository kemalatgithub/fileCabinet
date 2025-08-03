from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    holder= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    class Meta:
        db_table = 'notification'
class NotifiableUsers(models.Model):
    user_id= models.CharField(max_length=255)
    soft_delete =models.CharField(max_length=255, default=0)
    class Meta:
        db_table = 'notifiable_user'
class SystemNotification(models.Model):
    recipient = models.CharField(max_length=255)
    message = models.TextField()
    soft_delete =models.CharField(max_length=255, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    class Meta:
        db_table = 'system_notification'
    def __str__(self):
        return f"Notification for {self.recipient.username}"