from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.Home,name='home'),
    path('home/<int:pk>',views.Catimg,name='home'),
    path('hire/',views.hirepage,name='hire'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)