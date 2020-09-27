from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm
from django.contrib.auth import login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import UserProfile
from products.models import Product

def index(request, id):
    user = User.objects.get(id=id)
    user_profile = UserProfile.objects.get(user_id=id)
    products = Product.objects.filter(seller_id=id)
    return render(request, 'users/userinfo.html', {'user': user, 'user_profile': user_profile, 'products': products})
    
@login_required
def myprofile(request):
    id = request.user.id
    user = User.objects.get(id=id)
    user_profile = UserProfile.objects.get(user_id=id)
    products = Product.objects.filter(seller_id=id)
    return render(request, 'users/myprofile.html', {'user': user, 'user_profile': user_profile, 'products': products})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST) 
        
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user 
            
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')

    else:            
        form = RegisterForm()
        profile_form = UserProfileForm() 
    return render(request, 'register/register.html', {'form': form, 'profile_form': profile_form})