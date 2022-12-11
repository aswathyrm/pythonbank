from os import name

from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place


# Create your views here.


# def demo(request):
#     obj = branch.objects.all()
#     obj1 = district.objects.all()
#     return render(request, "index.html", {'result': obj,'result1':obj1})
def demo(request):
    #     # obj = place.objects.all()
    #     # obj1 = team.objects.all()
    return render(request, "index.html")


def form(request):
    return render(request, "form.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('form')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        print("user registered")
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def onclick(request):
    messages.info(request, "Application accepted")

def logout(request):
    auth.logout(request)
    return redirect('/')


# def form(request):
#     if request.method == 'POST':
#         username = request.POST['name']
#         dob = request.POST['dob']
#         age = request.POST['age']
#         gender = request.POST['gender']
#         phone = request.POST['phone number']
#         email = request.POST['email']
#         address = request.POST['address']
#         district = request.POST['district']
#         branch = request.POST['branch']
#         account = request.POST['acc type']
#         payment = request.POST['payment method']
#         if form.is_valid():
#             form.save()
#         else:
#             username = username
#             messages.info(request, "application accepted")
#             return render(request, 'form.html')
#         return redirect('/')
#     #     if dob == dob:
#     #         if User.objects.filter(username=name).exists():
#     #             messages.info(request, "Username Taken")
#     #             return redirect('form')
#     #         elif User.objects.filter(email=email).exists():
#     #             messages.info(request, "email Taken")
#     #             return redirect('form')
#     #         else:
#     #             user = User.objects.create_user(username=name, dob=dob, branch=branch)
#     #             user.submit();
#     #             return redirect('login')
#     #     else:
#     #         messages.info(request, "application accepted")
#     #         # return redirect('register')
#     #     # return redirect('/')
#     # return render(request, "form.html")
#     #
#

