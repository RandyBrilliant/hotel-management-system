from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from PIL import Image
from django.urls import reverse

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            password=password,
            username=username,
        )

        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email Address", max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='Last Login', auto_now=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin


class Profile(models.Model):
    MALE = "MA"
    FEMALE = "FE"
    OTHER = "OT"
    GENDER = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, verbose_name="First Name")
    last_name = models.CharField(
        max_length=200, verbose_name="Last Name", blank=True, null=True)
    address = models.TextField()
    phone_no = models.CharField(max_length=20, verbose_name="Phone Number")
    gender = models.CharField(
        max_length=2,
        choices=GENDER,
        verbose_name="Gender"
    )
    id_proof = models.CharField(max_length=200, verbose_name="ID Proof")
    address_proof = models.CharField(
        max_length=200, verbose_name="Address Proof")
    image = models.ImageField(
        default="default.png", upload_to="profile_pics", verbose_name="Profile Picture")
    status = models.CharField(max_length=200)
    last_update = models.DateTimeField(
        verbose_name='Last Update', auto_now=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    @property
    def profileURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
