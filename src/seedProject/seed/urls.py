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
    path('addfavorite/', views.add_favorite, name='addfavorite'),
    path('foodfavorite/', views.FoodFavoriteView.as_view(), name='foodfavorite'),
    path('foodfavoritedelete/', views.delete_favorite, name='foodfavorite_delete'),
    path('myfood/', views.MyFoodView.as_view(), name='myfood'),
    path('search_for_genre/', views.search_for_genre, name='search_for_genre'),
    path('fooddetail/<int:pk>/fooddelete/', views.FoodDeleteView.as_view(), name='food_delete'),
    path('download_mission_qr/', views.download_mission_qr, name='download_mission_qr'),
    path('point/', views.use_point, name='point'),
    path('pointthankyou/', views.PointThankyouView.as_view(), name='pointthankyou'),
    path('pointexplanetion/', views.PointExplanetionView.as_view(), name='pointexplanetion'),
    path('search_for_prefecture/', views.search_for_prefecture, name='search_for_prefecture'),
    path('communitypost/', views.CreateCommunityView.as_view(), name='communitypost'),
    path('communitydone/', views.CommunityDoneView.as_view(), name='communitydone'),
    path('community_joined/', views.JoinedCommunityView.as_view(), name='community_joined'),
    path('mycommunity/', views.MyCommunityView.as_view(), name='mycommunity'),
    path('community_detail/<int:pk>/', views.CommunityDetailView.as_view(), name='community_detail'),
    path('send_message/', views.send_message, name='send_message'),
    path('mycommunity/<int:pk>/delete/', views.CommunityDeleteView.as_view(), name='community_delete'),
    path('search_for_community_genre/', views.search_for_community_genre, name='search_for_community_genre'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('namechange/', views.NameChangeView.as_view(), name='namechange'),
    path('change_name/', views.change_name, name='change_name'),
    path('profile_pic_change', views.ImageChangeView.as_view(), name='profile_pic_change'),
    path('change_pic/', views.change_pic, name='change_pic'),
    path('storedetail/<int:pk>/', views.StoreDetailView.as_view(), name='storedetail'),
]