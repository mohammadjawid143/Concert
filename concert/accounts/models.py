from django.db import models
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User", related_name="profile")
    ProfileImage = models.ImageField(upload_to="Profileimages/")
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((MALE, "Male"), (FEMALE, "Female"))
    Gender = models.IntegerField(choices=GENDER_CHOICES)
    credit = models.IntegerField("Credit", default=0)
    