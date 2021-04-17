from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm, UserUpdateForm
from booking.models import Booking

from .models import UserFeedback
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView
)


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


@login_required
def ProfilePage(request):
    if request.method == "POST":
        u_form = UserUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            messages.success(
                request, "You have successfully update your profile!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
    }

    return render(request, 'user/profile.html', context)


@login_required
def PasswordChanges(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', {
        'form': form
    })


@login_required
def BookingList(request):
    my_bookings = Booking.objects.filter(customer__email=request.user.email)
    print(my_bookings)

    context = {
        'my_bookings': my_bookings
    }
    return render(request, 'user/list_booking.html', context)


class CreateFeedback(LoginRequiredMixin, CreateView):
    model = UserFeedback
    fields = ['category', 'comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def CreatedFeedback(request):
    return render(request, "user/userfeedback_form.html", {'notes': "You have submitted the feedback"})
