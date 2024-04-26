
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html', views.login, name='login'),
    path('home.html', views.home, name='home'),
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('register.html', views.register, name='register'),
    path('aboutus.html', views.aboutus, name='aboutus'),
    path('contactus.html', views.contactus, name='contactus'),
    path('cart.html', views.cart, name='cart'),
    path('checkout.html', views.checkout, name='checkout'),
    path('paymentdetails.html/', views.paymentdetails, name='paymentdetails'),
    path('feedback.html', views.feedback, name='feedback'),
    path('amount.html/', views.amount, name='amount'),
    path('logout.html', views.logout, name='logout'),

]

