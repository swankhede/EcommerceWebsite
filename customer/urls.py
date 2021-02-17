from django.urls import path
from . import views
urlpatterns = [

  
        path('register/',views.register,name='register'),
         path('login/',views.login_view,name='login_view'),
           path('addtocart/<pk>/<quantity>',views.add_to_cart,name='add_to_cart'),
           path('cart/',views.view_cart,name='view_cart'),
           path('order/',views.view_orders,name='view_orders'),
       
           path('order/payment/<pk>',views.buy_product,name='buy_product'),
     
]
