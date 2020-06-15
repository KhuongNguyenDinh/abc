from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from inside.models import SanPham
from datetime import datetime
from inside.models import User
from . import forms
from cart.forms import CartAddProductForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.db import models
from inside.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login,update_session_auth_hash, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from . import models
from inside import forms
from .forms import UserUpdateForm
# Create your views here.
def index(request):
    SanPham_list = SanPham.objects.all()
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1

    response = render(request, "inside/index.html", {'sanpham_list':SanPham_list, 'num_visits':num_visits})
    date1 = datetime.now()
    response.set_cookie("last_visit", date1.strftime('%d-%m-%Y %H:%M:%S'))
    last_visit = request.COOKIES.get('last_visit')

    return render(request, "inside/index.html", {'sanpham_list':SanPham_list, 'num_visits':num_visits, 'last_visit': last_visit})

def index1(request):
    return render(request,'basic_app/index.html')

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'inside/signin.html', {})

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    result = "You have logged out, Please choose  SIGN IN"

    return render(request, "inside/logout.html", {"result":result})

@login_required(login_url='/login')
def signup(request):
    form = forms.FormRegister()
    if request.method == 'POST':
        form =forms.FormRegister(request.POST, User)

        if form.is_valid() and form.cleaned_data['password'] == form.cleaned_data['confirm']:
            request.POST._mutable = True
            post = form.save(commit = False)
            post.name = form.cleaned_data['name']
            post.email = form.cleaned_data['email']
            post.password = form.cleaned_data['password']
            post.save()
            print("Saved to database")

        elif form.cleaned_data['password'] != form.cleaned_data['confirm']:
            form.add_error('confirm', 'The password does not match')
            print("Not confirm!")
    return render(request, "inside/signup.html", {'form': form})

def chiTiet(request, id):
    sanPham = SanPham.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request,'inside/chitiet.html',{'sanPham':sanPham, 'cart_product_form': cart_product_form})


@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your Profile was successfully updated!')
            return HttpResponseRedirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    context = {'page': 'user',
               'form': form,
              }
    return render(request, "inside/user_update.html", context)

@login_required
def user_change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('user_change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {'page': 'user',
               'form':form,
               }
    return render(request, "inside/user_change_password.html",context)


@login_required(login_url='/login')
def user_profile(request):
    context = {'page': 'user',}
    return render(request, "inside/user_detail.html", context)

def Registration(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data= request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user =user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'inside/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registerd': registered})
