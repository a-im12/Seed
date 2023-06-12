from django import forms
from .models import Gather, MissionDetail, Product, Community

class GatherPostForm(forms.ModelForm):

    class Meta:
        model = Gather
        fields = ('title', 'image', 'prefecture', 'access', 'contact', 'detail')

class MissionDetailForm(forms.ModelForm):

    class Meta:
        model = MissionDetail
        fields = ('mission', 'draw_time')

class DateInput(forms.DateInput):
    input_type = 'date'

class FoodPostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'genre', 'price', 'deadline', 'detail', 'image')
        widgets = {
            'deadline': DateInput(),
        }

class CommunityPostForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ('title', 'genre')