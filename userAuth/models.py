from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user class.
    """
    name = models.CharField(max_length=50, blank=True)
    username = models.CharField('username', max_length=50, unique=True, db_index=True)
    email = models.EmailField('email address', unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        db_table = u'user'

    def __unicode__(self):
        return self.username
