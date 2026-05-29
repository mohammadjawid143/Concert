from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpRequest, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from accounts.forms import ProfileEditForm, UserEditForm, RegistrationForm, ResetPasswordForm, ForgotPasswordForm
from django.conf import settings
from django.urls import reverse
from utils.email_service import send_email
from django.views import View
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your views here.


def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)

        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get("next"))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "errorMessage": "User name by this info could't found"
            }
            return render(request, "accounts/login.html", context)

    return render(request, "accounts/login.html", {})


def logout(request):

    auth.logout(request)

    return redirect('login')


def profile(request):
    profile = request.user.profile

    context = {
        "profile": profile
    }

    return render(request, "accounts/profile.html", context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)  # Pass both POST and FILES
        if form.is_valid():
            form.save()  # Saves both User and ProfileModel
            return redirect('login')  # Redirect to login page after registration
    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


def profileEdit(request):
    profileEditForm = ProfileEditForm(
        request.POST or None, request.FILES or None, instance=request.user.profile)
    userEditForm = UserEditForm(request.POST or None, instance=request.user)

    if profileEditForm.is_valid() and userEditForm.is_valid():
        profileEditForm.save()
        userEditForm.save()

        return HttpResponseRedirect(reverse('Profile'))

    context = {
        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
        "profileImage": request.user.profile.ProfileImage,
    }

    return render(request, "accounts/profile_Edit.html", context)

# class ForgetPasswordView(View):
#     def get(self, request: HttpRequest):
#         forget_pass_form = ForgotPasswordForm()
#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'accounts/forgot_password.html', context)

#     def post(self, request: HttpRequest):
#         forget_pass_form = ForgotPasswordForm(request.POST)
#         if forget_pass_form.is_valid():
#             user_email = forget_pass_form.cleaned_data.get('email')
#             user: User = User.objects.filter(email__iexact=user_email).first()
#             if user is not None:
#                 send_email(' Forgot_password ', user.email, {'user': user}, 'accounts/send_forgot_password.html')
#                 return redirect(reverse('home'))

#         context = {'forget_pass_form': forget_pass_form}
#         return render(request, 'accounts/forgot_password.html', context)


# class ResetPasswordView(View):
#     def get(self, request: HttpRequest, active_code):
#         user: User = User.objects.filter(email_active_code__iexact=active_code).first()
#         if user is None:
#             return redirect(reverse('login'))

#         reset_pass_form = ResetPasswordForm()

#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }
#         return render(request, 'accounts/reset_password.html', context)

#     def post(self, request: HttpRequest, active_code):
#         reset_pass_form = ResetPasswordForm(request.POST)
#         user: User = User.objects.filter(email_active_code__iexact=active_code).first()
#         if reset_pass_form.is_valid():
#             if user is None:
#                 return redirect(reverse('login'))
#             user_new_pass = reset_pass_form.cleaned_data.get('password')
#             user.set_password(user_new_pass)
#             user.email_active_code = get_random_string(72)
#             user.is_active = True
#             user.save()
#             return redirect(reverse('login'))

#         context = {
#             'reset_pass_form': reset_pass_form,
#             'user': user
#         }

#         return render(request, 'accounts/reset_password.html', context)


# class ActivateAccountView(View):

    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                # todo: show success message to user
                return redirect(reverse('login'))
            else:
                # todo: show your account was activated message to user
                pass

        raise Http404
