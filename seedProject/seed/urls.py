from django.urls import path
from . import views

app_name = 'seed'

urlpatterns = [
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('company_mypage/', views.CompanyMypageView.as_view(), name='company_mypage'),
    path('food_rescue/', views.FoodRescueView.as_view(), name='food_rescue'),
    path('community/', views.CommunityView.as_view(), name='community'),
    path('mission/', views.MissionView.as_view(), name='mission'),
    path('gather/', views.GatherView.as_view(), name='gather'),
    path('gatherpost/', views.CreateGatherView.as_view(), name='gatherpost'),
    path('gatherdone/', views.GatherDoneView.as_view(), name='gatherdone'),
    path('mygather/', views.MyGatherView.as_view(), name='mygather'),
]