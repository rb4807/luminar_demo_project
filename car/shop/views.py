from django.shortcuts import render,redirect
from shop.models import Category,Product

def allcategories(request):
    m = Category.objects.all()
    f = Product.objects.all()[:6]
    context={
        'm':m,
        'f':f
    }
    return render(request,'category.html',context)

def product(request,p):
    m = Category.objects.get(name=p)
    p = Product.objects.filter(category=m)
    return render(request,'product.html',{'m':m,'p':p})

def details(request,c):
    p = Product.objects.get(name=c)
    return render(request,'details.html',{'p':p})