from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
         
        return render(request, 'base.html')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/content/')
        return HttpResponse('not valid')

class SignupView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'signup.html', {'forms': SignupForm()})

    def post(self, request, *args, **kwargs):
        forms = SignupForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('/login/')
        return render(request, 'signup.html', {'forms': forms})

class ForgotPassView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request!')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class ContentView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        return render(request, 'content.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request!')

class ChangePasswordView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'resetpass.html')

    def post(self, request, *args, **kwargs):
        try:
            forms = User.objects.get(username=request.POST['username'])
            password = request.POST['password']
            checkpass = request.POST['checkpass']
            if password != checkpass:
               notvalid = True
               return render(request, 'resetpass.html', {'notvalid': notvalid})
            forms.set_password(password)
            forms.save()
            return HttpResponse('You have changed password successfully')
        except Exception:
            return HttpResponse("Username is not exist")
