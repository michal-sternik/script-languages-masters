from django.contrib import messages
from django.contrib.admin.templatetags.admin_list import pagination
from .models import Joke, CustomUser, ReviewRating
from random import randrange
from django.http import HttpResponse, JsonResponse
from .forms import RegisterForm, AddJokeForm, ReviewForm
from django.http import Http404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from .models import Joke

def index(request):
    """
    Render the home page with a random joke.
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




def add_joke(request):
    form = AddJokeForm(request.POST or None)

    user = get_object_or_404(CustomUser,id=request.user.id)

    if form.is_valid():
        Joke.objects.create(
            name=form.cleaned_data['name'],
            content=form.cleaned_data['content'],
            author=user,
            datetime=timezone.now(),
            likes=0
        )
        return redirect('joke_list')

    return render(request, 'add-joke.html', {'form': form})


def delete_joke(request, id):
    selected_joke = get_object_or_404(Joke, id=id)
    if selected_joke:
        if request.user.role == "ADMIN":
            selected_joke.delete()
            return redirect('joke_list')
        else:
            raise Http404
    else:
        raise Http404


def joke_list(request):
    jokes = Joke.objects.all()

    if request.method == 'POST':
        sorting = request.POST.get('sorting', 'date')
        descending = request.POST.get('descending', 'False')
        name_search = request.POST.get('name_search', None)
        author_search = request.POST.get('author_search', None)
        content_search = request.POST.get('content_search', None)

        if sorting == 'date':
            jokes = jokes.order_by('-datetime' if descending == 'True' else 'datetime')
        elif sorting == 'likes':
            jokes = jokes.order_by('-likes' if descending == 'True' else 'likes')

        if name_search:
            jokes = jokes.filter(name__icontains=name_search)
        if author_search:
            jokes = jokes.filter(author__icontains=author_search)
        if content_search:
            jokes = jokes.filter(content__icontains=content_search)

    page = request.GET.get('page', 1)
    paginator = Paginator(jokes, 5)
    try:
        jokes = paginator.page(page)
    except PageNotAnInteger:
        jokes = paginator.page(1)
    except EmptyPage:
        jokes = paginator.page(paginator.num_pages)

    context = {
        'jokes': jokes,
        'username': request.user.username,
    }

    return render(request, 'joke-list.html', context)

def joke_like(request, joke_id):
    joke = get_object_or_404(Joke, pk=joke_id)
    joke.likes += 1
    joke.save()
    return JsonResponse({'likes': joke.likes})


def joke_detail(request, joke_id):
    """
    View function to display a single joke.
    """

    selected_joke = get_object_or_404(Joke, pk=joke_id)

    review_list = ReviewRating.objects.filter(joke_id = joke_id)

    return render(request, "joke.html", {
        "joke": selected_joke,
        "user":request.user,
        "review_list": review_list
    })

def submit_review(request, id=None):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                # data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                joke = get_object_or_404(Joke, id=id)
                data.joke = joke
                data.created_at = timezone.now()
                data.author = request.user
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)