from django.urls import path
from .views import LandingPage, SignupPage, LoginPage

app_name = 'pages'

urlpatterns = [
    path('', LandingPage.as_view(),name='landingpage'),
    path('signup/', SignupPage.as_view(),name='signuppage'),
    path('login/', LoginPage.as_view(),name='loginpage'),
]