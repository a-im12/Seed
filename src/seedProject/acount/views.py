from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class SignupView(CreateView):
    
    form_class=CustomUserCreationForm
    
    template_name='signup.html'
    
    success_url = reverse_lazy('acount:signup_success')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_general = True
        user.is_active = True
        user.save()
        return super().form_valid(form)

class CompanySignupView(CreateView):
    
    form_class=CustomUserCreationForm
    
    template_name='companysignup.html'
    
    success_url = reverse_lazy('acount:signup_success')
    
    
    def form_valid(self, form):
        address = self.request.POST.get('address')
        user = form.save(commit=False)
        user.is_general = False
        user.is_active = False
        user.address = address
        user.save()
        return super().form_valid(form)

class SignupSuccessView(TemplateView):
    template_name = 'signup_success.html'

class UserLoginView(LoginView):
    template_name = 'login.html'
    
    def get_success_url(self):
        return reverse_lazy('seed:mypage')

class LogoutView(LogoutView):
    template_name = 'logout.html'