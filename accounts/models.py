from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,first_name,last_name,email,password=None,username=None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError('Username is required')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,first_name,last_name,email,password=None,username=None):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    Restaurant = 1
    Customer = 2

    ROLE_CHOICES = (
    (Restaurant, 'Restaurant'),
    (Customer, 'Customer'),
)

    objects = UserManager()

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50, unique=True)
    email = models.EmailField(max_length = 50,unique=True)
    phone_number = models.CharField(max_length = 12,blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES,blank=True,null=True)

    joined_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add =True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='users/profile_pictures',blank=True,null=True)
    cover_picture = models.ImageField(upload_to='users/cover_pictures',blank=True,null=True)
    address_line_1 = models.CharField(max_length = 100,blank=True,null=True)
    address_line_2 = models.CharField(max_length = 100,blank=True,null=True)
    country = models.CharField(max_length = 30,blank=True,null=True)
    state = models.CharField(max_length = 30,blank=True,null=True)
    city = models.CharField(max_length = 30,blank=True,null=True)
    pincode = models.CharField(max_length = 6,blank=True,null=True)
    latitude = models.CharField(max_length = 20,blank=True,null=True)
    longitude = models.CharField(max_length = 20,blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

        



    





