from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password

# Create your views here.
def index(request):
    return render(request,"index.html")

def create_user(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=make_password(request.POST["password"])
        if user.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            user.objects.create(name=name,email=email,password=password,mobile=mobile)
            return HttpResponse("user created successfully!")

def table(request):
    users=user.objects.all()
    return render(request, "table.html",{"users" : users})

def delete_user(request,pk):
    user.objects.get(id=pk).delete()
    return redirect('/data/')

def update_user(request,uid):
    user_obj=user.objects.get(id=uid)
    return render(request,"update.html",{"user_obj":user_obj})

def update_data(request):
    if request.method == "POST":
        uid=request.POST["uid"]
        name=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        user.objects.filter(id=uid).update(name=name,email=email,mobile=mobile)
        return HttpResponse("user update successfully")

def login(request):
    return render(request,"login.html")

def login_view(request):
    if request.method == "POST":
        person = user.objects.get(email=request.POST['email'])
        if check_password(request.POST['password'],person.password):
            request.session['login'] = True
            request.session['username'] = person.name
            return redirect('/data/')
        else:
            return HttpResponse("Invalid Email and password")



def products(request):
    return render(request,"product.html")


def upload_product(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        pro = product.objects.create(product_name=product_name ,description=description ,image=image)
        print(pro)
        return HttpResponse("Product add Successfully")


