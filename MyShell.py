import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping
#NoSQL coding
pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id)
    print(pizza) #topic.text returns same thing
    


t = Pizza.objects.get(id=1)
print(t) #Chess

entries = t.topping_set.all()

for e in entries:
    print(e)