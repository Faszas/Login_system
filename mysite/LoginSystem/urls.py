from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('content/', views.ContentView.as_view(), name='content'),
    path('reset/', views.ChangePasswordView.as_view(), name='reset')
]
