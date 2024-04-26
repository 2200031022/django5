from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    return render(request, 'register.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def paymentdetails(request):
    return render(request, 'paymentdetails.html')

def feedback(request):
    return render(request, 'feedback.html')

def amount(request):
    return render(request, 'amount.html')


def logout(request):
    return render(request, 'logout.html')




