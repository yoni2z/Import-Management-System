# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username, password=None):
        
#         # extra_fields.setdefault('is_staff', True)
#         # extra_fields.setdefault('is_superuser', True)

#         # if extra_fields.get('is_staff') is not True:
#         #     raise ValueError('Superuser must have is_staff=True.')
#         # if extra_fields.get('is_superuser') is not True:
#         #     raise ValueError('Superuser must have is_superuser=True.')
#         user = self.create_user(username, password,)
#         return user

# class User(AbstractBaseUser, PermissionsMixin):
#     USER_TYPES = (
#         ('importer', 'Importer'),
#         ('exporter', 'Exporter'),
#         ('admin', 'Administrator'),
#         ('accountant', 'Accountant'),
#         ('finance_manager', 'Finance Manager'),
#         ('compliance_officer', 'Compliance Officer'),
#     )

#     user_type = models.CharField(max_length=20, choices=USER_TYPES)
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True, null=True, blank=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.username
#     @property
#     def user(self):
#          return self.user_type

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPES = (
        ('importer', 'Importer'),
        ('admin', 'Administrator'),
        ('accountant', 'Accountant'),
        ('finance_manager', 'Finance Manager'),
        ('store_keeper', 'Store Keeper'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    username = models.CharField( max_length=255, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

    @property
    def user(self):
        return self.user_type
