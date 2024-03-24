from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('sign-up', views.register, name='sign_up'),
    path('add-joke', views.add_joke, name='add_joke'),
    path('joke-list', views.joke_list, name='joke_list'),
    path('joke-like/<int:joke_id>/', views.joke_like, name='joke_like'),
    path('joke-list/<int:joke_id>/', views.joke_detail, name='joke_detail'),
    path('submit_review/<id>/', views.submit_review, name='submit_review'),
    path('delete_joke/<id>', views.delete_joke, name='delete_joke')

]