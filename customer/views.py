from django.shortcuts import render,redirect,get_object_or_404,HttpResponse,HttpResponseRedirect
from .forms import CreateUserForm
from django.urls import reverse
from .models import cart,Orders
from django.contrib.auth.decorators import login_required
from istore.models import products
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
import logging
import time
# Create your views here.

def register(request):
    form = CreateUserForm()
  
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
          
            form.save()
            messages.success(request,"Account created")
            
            return redirect(reverse('login_view'))
        else:
            messages.warning(request,form.errors)
      
    
    context = {
        'form' :form
        }
    return render(request,'signup.html',context=context)

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        
        if user is not None:
            context = {
            'user':user.id
        }
            login(request,user)
            return redirect(reverse('index'),context=context)
        else:
            context={
                'error':'Password or Username does not matched'
                }
            
            return render(request,'login.html',context=context)



    return render(request,'login.html')


@login_required(login_url="login_view")
def add_to_cart(request,pk,quantity):
    user = get_object_or_404(User,username=request.user)
    flag=False
    if user.is_authenticated:
        product = products.objects.get(pk=pk)
        try:
            user_cart = cart.objects.get(product_id=pk,user=request.user)
            flag=True
        except:
            pass
        
        if flag:
                print("procuct exists")
                print("old",user_cart.price,user_cart.quantity,user_cart.price*user_cart.quantity)
                cart.objects.filter(product_id=pk,user=request.user).update(
                    quantity=user_cart.quantity+1,
                    price=user_cart.price+product.price
                )
        
                print("new",user_cart.price,user_cart.quantity,user_cart.price*user_cart.quantity)

                messages.success(request,"Product Added to cart")
     
        else:
           
                print("procuct not  exists")
                cart_obj = cart(
                    product_name=product.name,
                    user = request.user,
                    quantity = quantity,
                    price= int(quantity)*product.price,  
                    product_id=product      
                )
                cart_obj.save()
                messages.success(request,"Product Added to cart")
      
    
    return redirect(reverse('view_product',kwargs={'pk':product.id}),context={'products':product})


@login_required(login_url="login_view")
def view_cart(request):
    
 
    cart_obj = cart.objects.filter(user=request.user)
 
    total =0

    for i in cart_obj:
        total=total+i.price
    
    if request.POST.get('add'):
        pk = request.POST.get('pk')
        new_cart_obj,product = cart.get_cart_product(pk,request.user)
        new_cart_obj.quantity+=1
        new_cart_obj.save()
        new_cart_obj.price=new_cart_obj.quantity*product.price
        new_cart_obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
                    
       
                    
            
    if request.POST.get('remove'):
        pk = request.POST.get('pk')
        new_cart_obj,product = cart.get_cart_product(pk,request.user)
        new_cart_obj.quantity-=1
        new_cart_obj.save()
        new_cart_obj.price=new_cart_obj.quantity*product.price
        new_cart_obj.save()
        cart.check_cart(new_cart_obj.quantity,product.name)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    
    print(request.GET.get('delete'))
    if request.GET.get('delete'):
        name = request.GET.get('delete')
        product = cart.objects.filter(product_name=name,user=request.user)
        product.delete()
        print("product:",product)
     

    
    if request.POST.get('phone') and request.POST.get('address'):
        cart_obj = cart.objects.filter(user=request.user)
        
        for i in cart_obj:
            quantity=i.quantity
            product=i.product_id
            price=i.price
            
            address= request.POST.get('address')
            contact_no=request.POST.get('phone')  
            
            result=place_order(request.user,quantity,product,price,address,contact_no) 
        if result:
            cart_obj.delete()                    
            messages.success(request,"Order has been placed successfully")
        return render(request,'cart.html',context={'cart':cart_obj,'total':total})
  
   
    
    return render(request,'cart.html',context={'cart':cart_obj,'total':total})




def place_order(user,quantity,product,price,address,contact_no):
    order = Orders(         user=user,
                            quantity=quantity,
                            price=price,
                            product=product,
                            address= address,
                            contact_no=contact_no  
                            ) 
    order.save()
    return True

def buy_product(request,pk):
    print(pk)
    
    product = products.objects.get(pk=pk)
    if request.method=='POST':
        product=product
        quantity=request.POST.get('quantity')
        price=request.POST.get('price')
        address= request.POST.get('address')
        contact_no=request.POST.get('phone')  
            
        result = place_order(request.user,quantity,product,price,address,contact_no) 
        if result:
            messages.success(request,'Order has been placed succesfully')
        

    return render(request,'payment.html',context={'product':product,'total':product.price}) 


@login_required(login_url='login_view')
def view_orders(request):
    order = Orders.objects.filter(user=request.user)
    print(order)
    total=0
    for i in order:
        total=total+i.price
    return render(request,'order.html',context={'orders':order,'total':total})








    

    




