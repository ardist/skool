from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    username = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='avatar', blank=True, null=True)
    about = models.TextField()
    profile_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)

    def __str__(self):
        return self.username
