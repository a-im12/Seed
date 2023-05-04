from typing import Any, Dict
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

class MissionView(TemplateView):
    mission_detail_model = MissionDetail()
    template_name = 'mission.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mission_detail = MissionDetail.objects.filter(user=self.request.user, draw_time=datetime.date.today()).order_by('-draw_time')
        if mission_detail:
            if mission_detail[0].draw_time == datetime.date.today():
                context['draw_flg'] = True
            context['data'] = mission_detail[0]
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

def draw(request):
    draw_flg = False
    data = MissionDetail.objects.filter(user=request.user, draw_time=datetime.date.today()).order_by('-draw_time')
    if data:    
        if data[0].draw_time == datetime.date.today():
            draw_flg = True
            return render(request, 'mission.html', {'data': data, 'draw_flg': draw_flg})
    
    mission_detail_model = MissionDetail()
    
    mission_detail_model.user = request.user
    mission_detail_model.mission = Mission.objects.get(id=random.randint(1, len(Mission.objects.all())))
    mission_detail_model.draw_time = datetime.date.today()
    
    mission_detail_model.save()
    
    return render(request, 'mission.html', {'data': mission_detail_model, 'draw_flg': draw_flg})