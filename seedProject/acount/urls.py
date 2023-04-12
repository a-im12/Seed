from django.urls import path
from . import views
app_name = 'acount'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.SignupSuccessView.as_view(), name='signup_success'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('companysignup/', viewes.CompanySignupView.as_view(), name='company_signup'),
]