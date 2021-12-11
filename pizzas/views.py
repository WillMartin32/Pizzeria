from django.shortcuts import redirect, render
from .models import Pizza, Topping
from .forms import PizzaForm

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

# get request is when we get sothing from the database. read data from database
# post request is when we post something from the database. write data to database

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('pizzas:pizzas')

    context = {'form':form}
    return render(request, 'pizzas/new_pizza.html', context)