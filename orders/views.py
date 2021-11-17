from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from .models import *
from .forms import *


def Home(request):
    food = Food.objects.all()[:6]
    context = {"post": food}
    return render(request, "orders/main.html", context)


def Orders(request, pk):
    food = Food.objects.get(id=pk)

    if request.method == "POST":
        quantity = request.POST.get("quantity")
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        address = request.POST.get("address")
        orderform = Order.objects.create(
            food=food,
            quantity=quantity,
            fullname=fullname,
            phone=phone,
            email=email,
            address=address,
        )
        orderform.save()
        return redirect("/")

    context = {"post": food}
    return render(request, "orders/order.html", context)


def FoodSearch(request):
    context = {}
    if request.method == "POST":
        search = request.POST.get("search")
        food = Food.objects.filter(name__contains=search)
        context = {"post": food}
    return render(request, "orders/food-search.html", context)


def Foods(request):
    food = Food.objects.all()
    context = {"post": food}
    return render(request, "orders/foods.html", context)


def Categories(request):
    food = Food.objects.all()
    context = {"post": food}
    return render(request, "orders/category.html", context)


def CategoryFoods(request):
    food = Food.objects.all()
    context = {"post": food}
    return render(request, "orders/category-foods.html", context)
