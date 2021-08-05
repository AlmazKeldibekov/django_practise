from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib.auth import authenticate, login, get_user_model, logout

from accounts.forms import LoginForm


class LoginView(View):

    def get(self, request):
        # TODO: setup redirect url if authenticated
        form = LoginForm()
        return render(request('login.html',context={'form':form}))

    def post(self,request):
        bound_form = LoginForm(request.POST)

        if bound_form.is_valid():
            username = bound_form.cleaned_data.get('username')
            password = bound_form.cleaned_data.get('password')
            user = authenticate(username=username,password=password) #User
            if user:
                login(request,user)
                # TODO : URGENT ADD redirect url after login
                return render(request,'login.html',context={'form':bound_form})