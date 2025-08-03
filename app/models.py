from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from superAdmin.models import *
# from django.contrib.auth.models import Permission
from django.utils import timezone
# from auditlog.registry import auditlog
# Create your models here.
class UserAccountManager(BaseUserManager):
    def create_user(self, email, first_name,last_name,password=None):
        if not email:
            raise ValueError('user must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,last_name=last_name)

        user.set_password(password)
        user.save()
        return user
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=100,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    user_roles = models.ForeignKey(Role, on_delete=models. CASCADE)
    user_profile =models.ImageField(upload_to='profile_pic', default='profile_pic/sysuser.png')
    otp = models.CharField(max_length=255, default ='000')
    password_change_status = models.CharField(max_length=255, default='0')
    soft_delete =models.CharField(max_length=255, default=0)
    last_password_change = models.DateTimeField(default=timezone.now, null=True, blank=True)
    class Meta:
        db_table = 'users'
    objects = UserAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['first_name']
    def get_full_name(self):
        return self.first_name
    def get_short_name(self):
        return self.first_name
    def __str__(self):
        return self.email
    def password_changed(self):
       self.last_password_change = timezone.now()
       self.save()
    def set_password(self, raw_password):
        super().set_password(raw_password)
        self.last_password_change = timezone.now()
        self.save()
# auditlog.register(CustomUser)