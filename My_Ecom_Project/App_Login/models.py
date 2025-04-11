from django.db import models





from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _

#To automatucally create oneToOne objects
from django.db.models.signals import post_save
from django.dispatch import receiver






# Create your models here.

class MyUserManager(BaseUserManager):
    """A custrom Manager to deal with emails as unique identifier """
    def create_user(self,email,password=None,**extra_fields):
        """Creates and saves a User with the given email, and password."""
        
        if not email:
            raise ValueError("User must have an email address")
        user= self.model(
            email=self.normalize_email(email), 
            **extra_fields     
        )
       
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True') 
        return self.create_user(email,password,**extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(
        null=False,
        unique=True,
    )
    is_staff=models.BooleanField(
        _('staff status'),
        default=False,
        help_text=('Designates whether the user can log in this site')
    )
    
    is_active=models.BooleanField(
        _('active'),
        default=True,
        help_text=_('Designates wether this user should be treate as active. Unsellect this instead of deleting accounts')
    )

    USERNAME_FIELD='email'
    objects=MyUserManager()
    
    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username=models.CharField(max_length=264,blank=True)
    full_name=models.CharField(max_length=264,blank=True)
    address_1=models.TextField(max_length=300,blank=True)
    city=models.CharField(max_length=40,blank=True)
    zip_code=models.CharField(max_length=10,blank=True)
    country=models.CharField(max_length=50,blank=True)
    phone=models.CharField(max_length=20,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Profile"

    def is_fully_field(self):
        field_names=[f.name for f in self._meta.get_fields()]
        
        for field_name in field_names:
            value=getattr(self,field_name)
            if value is None or value=='':
                return False
        return True

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()        





