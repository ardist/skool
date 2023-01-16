from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from pages.sitemap import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path('', include('pages.urls')),
    path('backend/', include('admins.urls')),
    path('admin/', admin.site.urls), 
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)