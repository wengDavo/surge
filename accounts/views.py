from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import View
from accounts.forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.

class SignupView(View):
    def post(self, request):
        form = CustomUserCreationForm(self.request.POST)

        if form.is_valid():
            form.save()
            return redirect('pages:loginpage')
        else:
            for key, value in form.error_messages.items():
                 messages.warning(self.request,f"{value}")
            return redirect('pages:signuppage')

class LoginView(View):
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
    
        if user is not None:
            login(self.request, user)
            return redirect('crypto:cryptolist')
        else:
            messages.warning(self.request,"Incorrect Email or Password")
            return render(self.request, 'pages/login.html',)
