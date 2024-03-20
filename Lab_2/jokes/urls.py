from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.index, name="index"),
    path('', include('django.contrib.auth.urls')),
    path('sign-up', views.register, name='sign_up'),
    # path('login/', views.login, name="login")
]