from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.

def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas} # value has to match what is in views.
                # has to match what is after / below and template

    return render(request, "pizzas/pizzas.html", context) # has to match what is in template after /

def pizza(request, pizza_id): # Same nameid as what you sent in url.py
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.all()

    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, "pizzas/pizza.html", context)