from django.shortcuts import render
from.models import Products

# Create your views here.
def Product(request):
    prod=Products.objects.all()
    return render(request,'ProductView.html',{'prod':prod})
