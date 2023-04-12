from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, LoginView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
# Create your views here.

class SignupView(CreateView):
    
    form_class=CustomUserCreationForm
    
    template_name = 'signup.html'
    
    success_url = reverse_lazy('acount:signup_success')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_general = True
        # user.is_approval = True
        user.save()
        return super().form_valid(form)

class CompanySignupView(CreateView):
    from_class=CustomUserCreationForm

    template_name='companysignup.html'

    success_url = reverse_lazy('acount:signup_success')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_general = False
        # user.is_approval = False
        user.save()
        return super().form_valid(form)

class SignupSuccessView(TemplateView):
    template_name = 'signup_success.html'

# class LoginView(LoginView):
#     template_name = 'login.html'

#     def get_success_url(self):
#         if self.request.user.is_general:
#             return reverse_lazy('seed:mypage')
#         elif self.request.user.is_approval:
#             return reverse_lazy('seed:company_mypage')
#         else:
#             return reverse_lazy('acount:login')

class LoginView(TemplateView):
    template_name = 'login.html'
