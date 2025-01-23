from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from accounts.forms import AuthenticationForm,UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.core.mail import send_mail

class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(
            self.request, "Welcome")
        return super().form_valid(form)
    

from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import UserRegisterForm

class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("accounts:login")

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            # احراز هویت کاربر پس از ثبت‌نام
            user = authenticate(email=self.request.POST["email"], password=self.request.POST["password1"])
            if user is not None:
                login(self.request, user)
                messages.success(self.request, "Registration successful")

                # ارسال ایمیل خوش‌آمدگویی
                subject = 'Welcome to My Website'
                message = 'Thank you for registering with us.'
                from_email = 'arshiadjango@gmail.com'  # ایمیل فرستنده
                recipient_list = [self.request.POST["email"]]  # لیست گیرندگان ایمیل
                send_mail(subject, message, from_email, recipient_list)

        return super().form_valid(form)    
class LogoutView(auth_views.LogoutView):
    pass
