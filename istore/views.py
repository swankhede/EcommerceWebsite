from django.shortcuts import render,redirect
from django import http
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import products
from customer.models import cart
from django.test.client import RequestFactory

# Create your views here.

def index(request):

         
    context={}
    print(request.method=="POST")
    

    if request.GET.get('category'):

            category_name = request.GET.get('category')
            all_products = products.get_product_by_category(category_name)
            context['products']=all_products
            print(context)
    else:
            all_products = products.objects.all()
            context['products']=all_products
    
    if request.method=="POST":
        name = request.POST['search']
        print(name)
        product_obj = products.get_product_by_name(input_name=name)
        context['products']=product_obj

    
    print(context)
    return render(request,'index.html',context=context)


def view_product(request,pk):
    context={}
    
    product_obj= products.objects.get(pk=pk)
    context['products']=product_obj
   
    if request.user.is_authenticated:
        cart_obj = cart.objects.filter(user=request.user)
        product_list=[]
        for i in cart_obj:
            product_list.append(i.product_name)
      
        if product_obj.name in product_list:
            cart_obj = cart.objects.get(user=request.user,product_name=product_obj.name)
            context['cart']=cart_obj
            context['list']=product_list
     

            if request.method=='POST':
                
                if request.POST.get('add'):
                    
                    cart_obj.quantity+=1
                    cart_obj.save()
                    cart_obj.price=cart_obj.quantity*product_obj.price
                    cart_obj.save()
                    
                    return render(request,'details.html',context=context)
                    
            
                if request.POST.get('remove'):
                    cart_obj.quantity-=1
                    cart_obj.save()
                    cart_obj.price=cart_obj.quantity*product_obj.price
                    cart_obj.save()
                    
                    cart.check_cart(cart_obj.quantity,product_obj.name)
                    return render(request,'details.html',context=context)
  
       


    return render(request,'details.html',context=context)


@login_required(login_url='login_view')
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


