from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
# Create your views here.

class LandingPage(TemplateView):
    template_name = 'pages/index.html'

class SignupPage(TemplateView):
    template_name = 'pages/signup.html'

class LoginPage(TemplateView):
    template_name = 'pages/login.html'