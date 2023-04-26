from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager
from base.models import TimestampedModel


# Create your models here.
class User(AbstractBaseUser, TimestampedModel, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    email = models.EmailField(_("email"), db_collation="und-x-icu", unique=True)
    address = models.CharField(blank=True, max_length=255)
    zip_code = models.CharField(blank=True, max_length=16)
    state = models.CharField(blank=True, max_length=128)
    city = models.CharField(blank=True, max_length=128)

    is_designer = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['email', '-created_at']
        

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name





