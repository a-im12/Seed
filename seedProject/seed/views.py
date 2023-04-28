from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class MypageView(TemplateView):
    template_name = 'mypage.html'

class CompanyMypageView(TemplateView):
    template_name = 'companymypage.html'

class FoodRescueView(TemplateView):
    template_name = 'foodrescue.html'

class CommunityView(TemplateView):
    template_name = 'community.html'

class MissionView(TemplateView):
    template_name = 'mission.html'

class GatherView(TemplateView):
    template_name = 'gather.html'
