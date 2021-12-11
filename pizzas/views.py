from django.shortcuts import redirect, render
from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

def new_topping(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            return redirect('pizzas:pizza',pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/new_topping.html', context)

def edit_topping(request, topping_id):
    """Edit an existing topping."""
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    #if pizza != request.user:
    #    raise Http404

    if request.method != 'POST':
        # This argument tells Django to create the form prefilled
        # with information from the existing entry object.
        form = ToppingForm(instance=topping)
    else:
        # POST data submitted; process data.
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', pizza_id=pizza.id)

    context = {'topping':topping, 'pizza':pizza, 'form': form}
    return render(request, 'pizzas/edit_topping.html', context)