from django.views.generic import View
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.views.generic.edit import FormView, CreateView
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth import authenticate, login, logout


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = authenticate(email=email, password=password)

        try:
            if user is not None:
                login(request, user)
                return redirect('core:files')
        except Exception as e:
            print("Login Error is ", str(e))

        return super(LoginView, self).form_invalid(form)


class SignupView(CreateView):
    form_class = RegistrationForm
    template_name = 'account/register.html'
    success_url = '/'


class LogoutView(View):
    def get(self, request):
        request = self.request
        logout(request)
        return redirect('/')

