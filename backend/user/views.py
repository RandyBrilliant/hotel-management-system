from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import RegisterForm
# Create your views here.


@login_required
def logoutPage(request):
    logout(request)
    messages.success(request, "You have successfully sign out!")
    return redirect("login")


def RegisterPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "You have successfully created your account!")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})
