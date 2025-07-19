# mysite/views.p
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm,LoginForm
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import *
import json

def home(request):
    if 'q' in request.GET:
        q = request.GET['q']
        item = user.objects.filter(name__icontains=q)
        is_single_product = item.exists()  
        return render(request, 'mysite/base.html', {'food': item, 'is_single_product': is_single_product})
    else:
        item= user.objects.all()
    return render(request,'mysite/home.html', {'food':item})

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = user2(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],  
            )
            user.save()
            return redirect('login')  
    else:
        form = RegistrationForm()
    
    return render(request, 'mysite/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = user2.objects.get(username=username) 

                if user.password == password: 
                    request.session['user_id'] = user.id 
                    return redirect('home')  
                else:
                    messages.error(request, "Invalid username or password")
            except user2.DoesNotExist:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()
    
    return render(request, 'mysite/login.html', {'form': form})


def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        item = get_object_or_404(user, id=product_id) 

        cart = request.session.get('cart', {})
        if item.id in cart:
            cart[item.id]['quantity'] += 1 
        else:
            cart[item.id] = {
                'name': item.name,
                'price': item.price,
                'image': item.image,
                'quantity': 1, 
        }
        
        request.session['cart'] = cart
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'message': 'Item added to cart', 'cart_count': len(cart)})

        
        return redirect('home')
    return redirect('cart') 

def cart_view(request):
    cart = request.session.get('cart', {})
    total_price = 0.0
    
    for item in cart.values():
        
        price = float(item['price'])  
        quantity = item.get('quantity', 1)  
        total_price += price * quantity

    return render(request, 'mysite/cart.html', {'cart': cart, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        del cart[product_id]
    
    request.session['cart'] = cart
    return redirect('cart_view')  

@require_POST
def update_quantity(request, product_id):
    cart = request.session.get('cart', {})
    
    if product_id in cart:
        data = json.loads(request.body)
        quantity = data.get('quantity', 1)
        cart[product_id]['quantity'] = int(quantity)
        
        request.session['cart'] = cart
    
    return JsonResponse({'success': True})


def payment_page(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        if payment_method == 'card':
            # Card payment processing (you can add additional validation as needed)
            card_number = request.POST.get('card_number')
            expiry_date = request.POST.get('expiry_date')
            cvv = request.POST.get('cvv')
            if card_number and expiry_date and cvv:
                return redirect('order')
            else:
                messages.error(request, "Please complete all card details.")
        
        elif payment_method == 'scan_pay':
            # Simulate success for Scan & Pay
            return redirect('order')
        
        elif payment_method == 'cod':
            # Cash on Delivery selected, no additional details required
            return redirect('order')
        
        else:
            messages.error(request, "Please select a payment method.")
    
    return render(request, 'mysite/payment.html')

# Order Confirmation Page
def order_view(request):
    return render(request, 'mysite/order.html')

def about(request):
    return render(request,'mysite/about.html')

def contact(request):
    return render(request,'mysite/contact.html')

def review(request):
    return render(request,'mysite/revieww.html')

