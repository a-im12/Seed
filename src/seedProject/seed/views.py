from typing import Any, Dict
from django.http import FileResponse
from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Gather, MissionDetail, Mission, Product, Favorite, Genre, Prefecture
from .forms import GatherPostForm, FoodPostForm

import datetime
import random
import qrcode

class MypageView(TemplateView):
    template_name = 'mypage.html'

class CompanyMypageView(TemplateView):
    template_name = 'companymypage.html'

class FoodRescueView(ListView):
    template_name = 'foodrescue.html'
    model = Product
    context_object_name = 'product_list'
    
    def get_queryset(self):
        return Product.objects.order_by('-create_at')
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        genre = Genre.objects.all()
        context['genre_list'] = genre
        return context

class CommunityView(TemplateView):
    template_name = 'community.html'

class MissionView(TemplateView):
    mission_detail_model = MissionDetail()
    template_name = 'mission.html'
    
    def get_context_data(self, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            mission_detail = MissionDetail.objects.filter(user=self.request.user, draw_time=datetime.date.today()).order_by('-draw_time')
            if mission_detail:
                if mission_detail[0].draw_time == datetime.date.today():
                    context['draw_flg'] = True
                context['data'] = mission_detail[0]
            return context
        else:
            return super().get_context_data(**kwargs)

class GatherView(ListView):
    template_name = 'gather.html'
    model = Gather
    context_object_name = 'gather_list'
    
    def get_queryset(self):
        return Gather.objects.order_by('-create_at')
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        prefecture = Prefecture.objects.all()
        context['prefecture_list'] = prefecture
        return context

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
    if len(data) != 0:
        if data[0].draw_time.date() + datetime.timedelta(days=1) == datetime.date.today():
            return redirect('seed:mission')
    
    mission_detail_model = MissionDetail()
    
    user_model = request.user
    user_model.mission_point += 1
    
    mission_detail_model.user = request.user
    mission_detail_model.mission = Mission.objects.get(id=random.randint(1, len(Mission.objects.all())))
    mission_detail_model.draw_time = datetime.date.today()
    
    user_model.save()
    mission_detail_model.save()
    
    return render(request, 'mission.html', {'data': mission_detail_model, 'draw_flg': draw_flg})

class GatherDetailView(DetailView):
    template_name = 'gatherdetail.html'
    model = Gather

class GatherDeleteView(DeleteView):
    template_name = 'gatherdelete.html'
    model = Gather
    success_url = reverse_lazy('seed:gather')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

class FoodDoneView(TemplateView):
    template_name = 'foodrescuedone.html'

class CreateFoodView(CreateView):
    form_class = FoodPostForm
    template_name = 'foodrescuepost.html'
    
    success_url = reverse_lazy('seed:fooddone')
    
    def form_valid(self, form):
        data = form.save(commit=False)
        data.company = self.request.user
        data.save()
        return super().form_valid(form)

class FoodDetailView(DetailView):
    template_name = 'foodrescuedetail.html'
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        favorite_list = Favorite.objects.filter(user=self.request.user, product=self.object)
        if favorite_list:
            context['favorite'] = favorite_list
        
        return context

def add_favorite(request):
    favorite_model = Favorite()
    
    select_product = Product.objects.get(id=request.POST.get('product_id'))
    page_source = request.POST.get('source')
    
    favorite_model.user = request.user
    favorite_model.product = select_product
    
    favorite_model.save()
    url = reverse('seed:fooddetail', kwargs={'pk': request.POST.get('product_id')})
    
    if page_source == 'rescue':
        return redirect(url + '?source=rescue')
    else:
        return redirect('seed:fooddetail', pk=request.POST.get('product_id'))

class FoodFavoriteView(ListView):
    template_name = 'foodrescuefavorite.html'
    model = Favorite
    context_object_name = 'favorite_list'
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

def delete_favorite(request):
    delete_favorite = Favorite.objects.filter(user=request.user, product=request.POST.get('product_id'))
    page_source = request.POST.get('source')
    
    delete_favorite.delete()
    
    url = reverse('seed:fooddetail', kwargs={'pk': request.POST.get('product_id')})
    
    if page_source == 'rescue':
        return redirect(url + '?source=rescue')
    else:
        return redirect('seed:fooddetail', pk=request.POST.get('product_id'))

class MyFoodView(ListView):
    template_name = 'myfood.html'
    model = Product
    context_object_name = 'product_list'
    
    def get_queryset(self):
        return Product.objects.filter(company=self.request.user)

def search_for_genre(request):
    
    id = request.POST.get('genre')
    
    if id == "":
        return redirect('seed:food_rescue')
    
    food_model = Product.objects.filter(genre_id=id)
    genre_model = Genre.objects.all()
    context = {
        'product_list':food_model,
        'genre_list':genre_model,
        }
    
    return render(request, 'foodrescue.html', context)

class FoodDeleteView(DeleteView):
    template_name = 'fooddelete.html'
    model = Product
    
    def get_success_url(self):
        print("今")
        if self.request.GET.get('posted') == 'posted':
            return reverse_lazy('seed:myfood')
        else:
            return reverse_lazy('seed:food_rescue')

def download_mission_qr(request):
    point = request.user.mission_point
    
    print(point)
    
    img = qrcode.make('http://127.0.0.1:8000/point/')
    img.save("qr.png")
    
    return FileResponse(open("qr.png", 'rb'), as_attachment=True, filename='qr.png')

def use_point(request):
    user_model = request.user
    user_model.mission_point -= user_model.mission_point
    user_model.save()
    
    return redirect('seed:pointthankyou')

class PointThankyouView(TemplateView):
    template_name = 'pointthankyou.html'

class PointExplanetionView(TemplateView):
    template_name = 'point_explanetion.html'

def search_for_prefecture(request):
    p_id = request.POST.get('prefecture')
    
    if p_id == "":
        return redirect('seed:gather')
    
    gather_list = Gather.objects.filter(prefecture_id=p_id)
    prefecture_list = Prefecture.objects.all()
    
    context = {
        'gather_list':gather_list,
        'prefecture_list':prefecture_list,
    }
    
    return render(request, 'gather.html', context)