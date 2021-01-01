from django.db import models
from django.contrib.auth.models import AbstractUser, Group
import uuid


class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    photo = models.ImageField(upload_to='photos', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def group(self):
        groups = self.groups.all()
        return groups[0].name if groups else None
