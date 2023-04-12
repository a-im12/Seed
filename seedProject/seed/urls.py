from django.urls import path
from . import views
app_name = 'seed'

urlpatterns = [
    path('mypage/', views.myPageView.as_view(), 'mypage'),
    path('companymypage/', views.companyMyPageView.as_view(), 'company_mypage'),
]