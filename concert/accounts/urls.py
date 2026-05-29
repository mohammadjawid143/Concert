from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from ticketSales.views import time_view

urlpatterns = [
    path('login/', views.my_login, name='login'),
    path('time/', time_view, name='time_view'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='Profile'),
    path('register/', views.register, name='register'),
    path('profile_Edit/', views.profileEdit, name='profile_Edit'),
    path('forget-reset', auth_views.PasswordResetView.as_view(
        template_name='accounts/forgot_password.html'), name='password_reset'),
    path('forget-reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/forgot_password_done.html'), name='password_reset_done'),
    path('forget-reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('forget-reset_complate', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complate'),
]
