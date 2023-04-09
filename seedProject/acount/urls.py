from django.urls import path
from . import views
app_name = 'acount'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signup_success/', views.SignupSuccessView.as_view(), name='signup_success'),
]