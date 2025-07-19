# mysite/urls.py

from django.urls import path

from . import views

urlpatterns = [
  
    path('login/', views.user_login, name='login'), 
    path('', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('home/login.html', views.user_login, name='login'),
    path('home/register.html', views.register, name='register'),
    path('register.html', views.register, name='register'),
    path('login.html', views.user_login, name='login'), 
    path('cart/', views.cart_view, name='cart_view'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:product_id>/', views.remove_from_cart, name='remove_from_cart'),  
    path('update-quantity/<str:product_id>/', views.update_quantity, name='update_quantity'), 
    path('cart/order.html',views.order_view, name='order'),
    path('cart/payment.html',views.payment_page, name='payment'),
    path('order', views.order_view, name='order'),
    path('home/about.html', views.about, name='about'),
    path('home/contact.html', views.contact, name='contact'),
    path('home/revieww.html', views.review, name='review'),     

]


