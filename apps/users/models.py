from django.db import models
# from django.contrib.auth.models import AbstractUser


class ResetPasswordConfirm(models.Model):
    username = models.CharField(max_length=100)
    code = models.CharField(max_length=6)
