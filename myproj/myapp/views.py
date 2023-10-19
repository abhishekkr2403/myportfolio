from django.shortcuts import render
from .models import Category,CatImage
# Create your views here.
def Home(request):
    allcategory=Category.objects.all()
    return render(request,'myapp/home.html',{'category':allcategory})
def Catimg(request,pk):
    catdata=Category.objects.get(id=pk)
    print(catdata.title)
    title=catdata.title
    data = CatImage.objects.filter(title=catdata)
    print(data)
    # for data in data:
    #     print(data)

    return render(request,'myapp/catpage.html',{'data':data,'title':title})