from django.db import models
from django.contrib.auth.models import (
        AbstractBaseUser,
        BaseUserManager,
        PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_volunteer(email, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def create_therapist(self, email, password=None):
        user = self.create_user(email, password)
        user.is_staff = True
        user.save(using=self._db)

        return user


class Therapist(AbstractBaseUser, PermissionsMixin, models.Model):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    therapist = models.ManyToManyField(Therapist, verbose_name='theraist')
    USERNAME_FIELD = 'email'


class Emotions(models.Model):
    """Emotions listed in the entry"""

    name = models.CharField('Emotions name', max_length=50)
    description = models.TextField('Descrition')


class DiaryEntry(models.Model):
    """One user's entry"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    emotions = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE)
