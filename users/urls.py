from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('logout/', views.userLogout, name='logout'),
    path('registration/', views.register, name='registration'),
    path('user-account/', views.userAccount, name='user-account'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="users/reset_password.html"), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="users/reset_password_sent.html"), name="password_reset_done"),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/reset.html"), name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="users/reset_password_complete.html"), name="password_reset_complete"),
]