from django.urls import path
from . import views
app_name = 'seed'

urlpatterns = [
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('company_mypage/', views.CompanyMypageView.as_view(), name='company_mypage'),
]