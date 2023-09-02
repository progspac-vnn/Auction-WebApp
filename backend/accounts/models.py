from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.mail import send_mail
from utils.otp import generate_otp

# Create your models here.

class customUserManager(BaseUserManager):

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, self.email, **kwargs)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Invalid Email")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)

class customUser(AbstractUser):
    USER = (
        ('1', 'Admin'),
        ('2', 'Seller'),
        ('3', 'Customer')
    )
    email = models.EmailField(unique=True)
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    otp = models.IntegerField(default=0)

    # Deal with OTP

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    objects = customUserManager()

    def send_otp_email(self, otp):
        if not self.email:
            raise ValueError("User must have an email address to send OTP.")

        subject = "Your OTP for Login"
        message = f"Your OTP: {otp}"
        from_email = settings.EMAIL_HOST_USER  

        send_mail(subject, message, from_email, [self.email], fail_silently=False)

    def send_otp(self):
        otp = generate_otp()  # Generate OTP
        self.otp = otp
        self.save()
        print(self.otp)
        self.send_otp_email(otp)

        return otp

