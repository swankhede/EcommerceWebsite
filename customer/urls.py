from django.urls import path
from . import views
urlpatterns = [

  
        path('register/',views.register,name='register'),
         path('login/',views.login_view,name='login_view'),
           path('addtocart/<pk>/<quantity>',views.add_to_cart,name='add_to_cart'),
           path('cart/',views.view_cart,name='view_cart'),
     
]
