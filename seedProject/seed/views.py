from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import Gather, MissionDetail, Mission
from .forms import GatherPostForm, MissionDetailForm

import datetime
import random

class MypageView(TemplateView):
    template_name = 'mypage.html'

class CompanyMypageView(TemplateView):
    template_name = 'companymypage.html'

class FoodRescueView(TemplateView):
    template_name = 'foodrescue.html'

class CommunityView(TemplateView):
    template_name = 'community.html'

class MissionView(CreateView):
    form_class = MissionDetailForm
    template_name = 'mission.html'
    
    success_url = reverse_lazy('seed:mission')
    
    def form_valid(self, form):
        data = form.save(commit=False)
        
        data.user = self.request.user
        
        today = datetime.date.today()
        
        mission_detail_data = MissionDetail.objects.filter(user=self.request.user).order_by('-draw_time')
        
        if mission_detail_data:
            if mission_detail_data[0].draw_time == today:
                data.mission = mission_detail_data.mission
                data.draw_time = mission_detail_data.draw_time
                data.save()
                return super().form_valid(form)

        while True:
            mission_id = random.randint(1, len(Mission.objects.all()))
            mission_data = Mission.objects.get(id=mission_id)
            if mission_data:
                break
        data.mission = mission_data
        data.draw_time = today
        data.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mission_detail = MissionDetail.objects.filter(user=self.request.user, draw_time=datetime.date.today()).order_by('-draw_time')
        if mission_detail:
            context['mission_detail'] = mission_detail[0]
        return context

class GatherView(ListView):
    template_name = 'gather.html'
    model = Gather
    context_object_name = 'gather_list'
    
    def get_queryset(self):
        return Gather.objects.order_by('-create_at')

class GatherDoneView(TemplateView):
    template_name = 'gatherdone.html'

class CreateGatherView(CreateView):
    form_class = GatherPostForm
    template_name = 'gatherpost.html'
    
    success_url = reverse_lazy('seed:gatherdone')
    
    def form_valid(self, form):
        data = form.save(commit=False)
        data.user_id = self.request.user

        data.save()
        return super().form_valid(form)

class MyGatherView(ListView):
    template_name = 'mygather.html'
    model = Gather
    context_object_name = 'mygather_list'
    
    def get_queryset(self):
        return Gather.objects.filter(user_id=self.request.user)