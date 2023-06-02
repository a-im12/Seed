from django.urls import path
from . import views
app_name = 'acount'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.SignupSuccessView.as_view(), name='signup_success'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('company_signup/', views.CompanySignupView.as_view(), name='company_signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]