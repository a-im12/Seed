from django import forms
from .models import Gather, MissionDetail, Product

class GatherPostForm(forms.ModelForm):

    class Meta:
        model = Gather
        fields = ('title', 'prefecture', 'access', 'contact', 'detail')

class MissionDetailForm(forms.ModelForm):

    class Meta:
        model = MissionDetail
        fields = ('mission', 'draw_time')

class FoodPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'genre', 'price', 'detail', 'image')