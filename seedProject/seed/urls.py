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
    path('draw/', views.draw, name='draw'),
    path('gather_detail/<int:pk>/', views.GatherDetailView.as_view(), name='gather_detail'),
    path('mygather/<int:pk>/delete/', views.GatherDeleteView.as_view(), name='gather_delete'),
    path('foodpost/', views.CreateFoodView.as_view(), name='foodpost'),
    path('fooddone/', views.FoodDoneView.as_view(), name='fooddone'),
    path('fooddetail/<int:pk>/', views.FoodDetailView.as_view(), name='fooddetail'),
]