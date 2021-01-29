from django.db import models
from django.contrib.auth.models import AbstractUser, Group
import uuid
from django.shortcuts import reverse
from django.contrib.auth.hashers import make_password


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True, related_name="user_role")

    

    def get_absolute_url(self):
        return reverse("user", kwargs={"pk": self.id})

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.password = self.password
        else:
            self.password = make_password(self.password, hasher='default')
        super().save(*args, **kwargs)

