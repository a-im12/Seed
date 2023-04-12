from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class MypageView(TemplateView):
    template_name = 'mypage.html'

class CompanyMypageView(TemplateView):
    template_name = 'companymypage.html'
