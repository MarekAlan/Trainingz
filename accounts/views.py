from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from accounts.forms import LoginForm, CreateUserForm, UserPermUpdateForm


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("login")
        return render(request, "form.html", {"form": form})


class RegisterView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, "form.html", {"form": form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["pass1"])
            user.save()
            return redirect("login")
        return render(request, "form.html", {"form": form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class UserListView(ListView):

    model = User
    template_name = "accounts/user_list_view.html"


class UserPermSettingView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermUpdateForm(instance=user)
        return render(request, "form.html", {"form": form})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, "form.html", {"form": form})
