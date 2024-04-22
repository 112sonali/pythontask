from django.shortcuts import render,redirect
from. models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here
def index(request):
    return render(request, "index.html")


def create_user(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST["password"])
        if user.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            user.objects.create(name=name,email=email,password=password)
            return HttpResponse("user created successfully!")

def table(request):
    users = user.objects.all()
    return render(request, "table.html",{"users":users})

def delete_user(request,pk):
    user.objects.get(id=pk).delete()
    return redirect('/data/')

def update_user(request,uid):
    user_obj=user.objects.get(id=uid)
    return render(request, "update.html", {"user_obj":user_obj})

def update_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        name = request.POST["name"]
        email = request.POST["email"]
        user.objects.filter(id=uid).update(name=name,email=email)
        return HttpResponse("user update successfully")


