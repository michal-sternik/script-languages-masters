from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Joke
from random import randrange
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
# def index(request):
#     return HttpResponse("Hello, world. You're at the jokes index.")

# def index(request):
    # product = Product.objects.all()
    #
    # valid_profiles_id_list = Product.objects.all().values_list('id', flat=True)
    # random_return_size = 8
    # if valid_profiles_id_list.count() < 8:
    #     random_return_size = random.randint(int(valid_profiles_id_list.count()/2), valid_profiles_id_list.count())
    #
    # random_profiles_id_list = random.sample(list(valid_profiles_id_list), random_return_size)
    # query_set = Product.objects.filter(id__in=random_profiles_id_list).order_by('?')
    #
    # 
    # context={
    #     'object_list': product,
    #     'proposed_products' : query_set
    # }
    # return render(request,'index.html')#,context)


# views.py


import os
from django.conf import settings

def index(request):
    """
    Render the home page with a random joke.

    Args:
        request (HttpRequest): The incoming request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    username = request.user.username if request.user.is_authenticated else None
    is_authenticated = request.user.is_authenticated
    random_joke = get_random_joke()
    context = {
        'username': username,
        'is_authenticated': is_authenticated,
        'random_joke': random_joke,
    }
    return render(request, 'index.html', context)

def login(request):
    return render(request, 'registration/login.html')

def get_random_joke():
    """
    Get a random joke from the database.

    Returns:
        Joke: A random joke object, or None if the database is empty.
    """
    try:
        count = Joke.objects.count()
        rand = randrange(count)
    except ValueError:
        return None
    return Joke.objects.all()[rand]

# view for register form
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, "registration/sign-up.html", {"form":form})

# models.py
from django.db import models

# class Joke(models.Model):
#     """
#     A model representing a joke.
#     """
#     text = models.TextField()
#
#     def __str__(self):
#         return self.text[:50] + '...'

# urls.py


# templates/index.html
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Jokes</title>
# </head>
# <body>
#     {% if is_authenticated %}
#         <p>Welcome, {{ username }}!</p>
#     {% else %}
#         <p>You are not logged in.</p>
#     {% endif %}
#
#     {% if random_joke %}
#         <p>Random Joke: {{ random_joke.text }}</p>
#     {% else %}
#         <p>No jokes available.</p>
#     {% endif %}
# </body>
# </html>