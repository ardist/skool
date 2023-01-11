from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from admins.models import UserProfile

class Post(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500)
    image = models.ImageField(upload_to="posts")
    body = RichTextUploadingField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    writer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()    
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title
