from django.urls import path
from . import views


urlpatterns = [
    path('', views.Contact_Us, name='Contactus'),
    path('send-message/', views.sent_message, name='send_message'),
    path('message/', views.messages, name='message'),
    path('delete-message/<int:message_id>/', views.delete_message, name='delete_message'),
]


