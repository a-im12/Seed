from django import forms
from .models import Gather, MissionDetail

class GatherPostForm(forms.ModelForm):

    class Meta:
        model = Gather
        fields = ('title', 'prefecture', 'access', 'contact', 'detail')

class MissionDetailForm(forms.ModelForm):

    class Meta:
        model = MissionDetail
        fields = ('mission', 'draw_time')