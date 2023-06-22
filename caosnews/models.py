from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.CharField(primary_key=True, max_length=20, verbose_name='Nombre de usuario')
    password = models.CharField(max_length=20, verbose_name='Contraseña')

    def __str__(self):
        return self.user.username


