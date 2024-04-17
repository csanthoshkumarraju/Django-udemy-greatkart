from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
 
# Create your models here.
class MyaccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,phone_number,email,password = None):
        if not email:
            raise ValueError('Email Address is must for user')
        if not username:
            raise ValueError('user must have a username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            phone_number = phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password,phone_number):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
            phone_number = phone_number
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser): 
    first_name   = models.CharField(max_length=50)
    last_name    = models.CharField(max_length=50)
    username     = models.CharField(max_length=50,unique= True)
    email        = models.EmailField(max_length=254,unique= True)
    phone_number = models.CharField(max_length=50,unique= True)
    # required fields
    date_joined = models.DateField(auto_now=False, auto_now_add=True)
    last_login = models.DateField(auto_now=True, auto_now_add=False)
    is_admin = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_active = models.BooleanField(default= True)
    is_superadmin = models.BooleanField(default= False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','phone_number']

    objects = MyaccountManager()

    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,add_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=100,blank=True)
    address_line2 = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    profile_picture = models.ImageField(upload_to='userprofile',blank=True)
    state = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.user.first_name
    def full_address(self):
        return f'{self.address_line1} {self.address_line2}'
