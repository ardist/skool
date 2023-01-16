from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
import uuid
from admins.models import UserProfile
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
    )
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique_for_date='publish')
    image = models.ImageField(upload_to="posts/%Y/%m/%d/", blank=True, null=True)
    body = RichTextUploadingField()
    post_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    writer = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
        
    objects = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('detail',args=[self.slug])

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()    
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return self.title
