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


class Therapist(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cv = models.FileField(upload_to='uploads/cv/', null=True, blank=True)

    bio = models.TextField()
    diploma = models.FileField(upload_to='uploads/diploma/', null=True, blank=True)
    patients = models.ManyToManyField('Patient', through='Therapy')

    def __str__(self):
        return self.user_profile.name


class Supervisor(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    cv = models.FileField(upload_to='uploads/cv/', null=True, blank=True)

    bio = models.TextField()
    diploma = models.FileField(upload_to='uploads/diploma/', null=True, blank=True)
    therapists = models.ManyToManyField('Therapist', through='Supervision')

    def __str__(self):
        return self.user_profile.name


class Patient(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()

    class Meta:
        verbose_name_plural = "patients"

    def __str__(self):
        return self.user_profile.name


class Diary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='diaries')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "diaries"

    def __str__(self):
        return self.title


class Lvl(models.Model):
    lvl = models.CharField(max_length=20)

    def __str__(self):
        return self.lvl


class Emotion(models.Model):
    lvl = models.ForeignKey(Lvl, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lvl} {self.name}'


class Mood(models.Model):
    lvl = models.ForeignKey(Lvl, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.lvl} {self.name}'


class DiaryEntry(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)

    emotion = models.ForeignKey(Mood, on_delete=models.CASCADE)
    mood = models.ForeignKey(Emotion, on_delete=models.CASCADE)
    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name='entries')
    reaction = models.TextField()

    # emotion_lvl = models.ForeignKey(EmotionLvl, on_delete=models.CASCADE)
    # mood_lvl = models.ForeignKey(MoodLvl, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.title


class Therapy(models.Model):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE, blank=True)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('therapist', 'patient',)


class Supervision(models.Model):
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    diary = models.ForeignKey(Diary, on_delete=models.CASCADE)
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('therapist', 'supervisor')
