from django.db import models

# Create your modelj
class Images(models.Model):
    description= models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to='pictures')
class Category(models.Model):
    title=models.CharField(max_length=60,null=True,blank=True)
    coverimage=models.ImageField(upload_to='coverimg')
    def __str__(self):
      return str(self.title)
class CatImage(models.Model):
    title=models.ForeignKey(Category,on_delete=models.CASCADE)
    images=models.ImageField(upload_to=f'coverimg')
    def __str__(self):
      return str(self.title)