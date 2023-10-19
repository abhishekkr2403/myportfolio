from django.contrib import admin
from .models import Images,Category,CatImage
# Register your models he
@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display=["name",'image']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','coverimage']

@admin.register(CatImage)
class CatImageAdmin(admin.ModelAdmin):
    list_display=['title','images']
    

