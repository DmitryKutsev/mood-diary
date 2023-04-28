from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.name


class Patient(User):
    """User in the system"""

    pass


class Therapist(User):
    """User in the system"""

    is_staff = True
    patients = models.ManyToManyField(Patient, through="Therapy")


class Therapy(models.Model):
    """Diary for a user."""

    class Meta:
        verbose_name_plural = "Therapies"

    description = models.TextField("Description")
    patient = models.ForeignKey(Patient, verbose_name="owner", on_delete=models.CASCADE)
    therapist = models.ForeignKey(
        Therapist, verbose_name="therapist", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Therapy {self.patient} - {self.therapist}"


#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     """User in the system"""
#
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     objects = UserManager()
#     therapist = models.ManyToManyField(Therapist, verbose_name='theraist')
#     USERNAME_FIELD = 'email'


class Emotions(models.Model):
    """Emotions listed in the entry"""

    name = models.CharField("Emotion name", max_length=50)
    description = models.TextField("Descrition")

    def __str__(self):
        return self.name


class Moods(models.Model):
    """Emotions listed in the entry"""

    name = models.CharField("Mood name", max_length=50)
    description = models.TextField("Descrition")

    def __str__(self):
        return self.name


class Diary(models.Model):
    """Diary for a user."""

    class Meta:
        verbose_name_plural = "Diaries"

    name = models.CharField("Diary name", max_length=50)
    description = models.TextField("Description")
    patient = models.ForeignKey(Patient, verbose_name="owner", on_delete=models.CASCADE)
    therapist = models.ForeignKey(
        Therapist, verbose_name="therapist", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class DiaryEntry(models.Model):
    """One user's entry"""

    class Meta:
        verbose_name_plural = "Diary entries"

    name = models.CharField(max_length=255)
    mood = models.ForeignKey(Moods, verbose_name="mood", on_delete=models.CASCADE)
    emotion = models.ForeignKey(
        Emotions, verbose_name="emotion", on_delete=models.CASCADE
    )
    diary = models.ForeignKey(
        Diary, verbose_name="diary", related_name="entries", on_delete=models.CASCADE
    )
    description = models.TextField("Description")

    def __str__(self):
        return self.name
