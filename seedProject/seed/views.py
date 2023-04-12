from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

class myPageView(TemplateView):
    template_name = 'mypage.html'

class companyMyPageView(TemplateView):
    template_name = 'companymypage.html'
