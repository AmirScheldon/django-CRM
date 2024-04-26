from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm, AddCustomerForm
from .models import Record




def home(request):
    record = Record.objects.all() 
    context = {'record': record}
    return render(request, 'home.html', context)
    

def login_user(request):
    is_login_page = request.path == reverse('login')
    context= { 'is_login_page': is_login_page}
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # if user autheticated, it returns User object otherwise it returns None.
        user = authenticate(request, username= username, password = password)
        
        if user is not None: 
            login(request, user)
            messages.success(request, message= 'You have been loggedin')
            return redirect('home')
        else:
            messages.success(request, message= ' You are not able to login')
            return redirect('home')
    else :
        return render(request, 'login.html', context)

    
        
def logout_user(request):
    logout(request)
    messages.success(request, message='You have been loggedout')
    return redirect('home')

def register(request):
    is_register_page = request.path == reverse('register')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, message= 'You have been successfully registered!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form, 'is_register_page': is_register_page})
    
    return render(request, 'register.html', {'form': form, 'is_register_page': is_register_page})    
        

def customer_id(request, pk):
    if request.user.is_authenticated:
        queryset = Record.objects.get(id=pk)
        return render(request, 'customer-id.html', {'queryset': queryset})
    else:
        messages.success(request, message= 'you are not signed-up please first sign-in')
        return redirect('home')
    
def delete_customer(request, pk):
    customer = Record.objects.get(id=pk)
    customer.delete()
    messages.success(request, message= 'Customer successfully deleted!')
    return redirect('home')  

def add_customer(request):
    is_customer_id_page = request.path == reverse('add_customer')
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, message= 'Customer successfully added!')
                return redirect('home')             
        return render(request, 'add-customer.html', {'form':form, 'is_customer_id_page': is_customer_id_page})
    else:
        messages.success(request, message= 'you are not signed-up please first sign-in')
        return redirect('home')  
    
    
def update_customer(request, pk):
    if request.user.is_authenticated:
        current_user = Record.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_user )
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, message= 'Customer successfully updated!')
                return redirect('home') 
    else:
        messages.success(request, message= 'you are not signed-up please first sign-in')
        return redirect('home')                    
