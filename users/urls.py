"""django_project URL Configuration"""


from django.urls import path,include
from django.contrib.auth import views as auth_views
from users import views as user_views

# template_name='registration/password_reset_complete.html'
app_name = 'users'


urlpatterns = [

    path('register/' , user_views.register , name='register'),
    path('profile/' , user_views.profile , name='profile'),
    path('login/' , auth_views.LoginView.as_view(template_name='registration/login.html') , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(template_name='registration/logout.html') , name='logout'),
    path('change-password/' , auth_views.PasswordChangeView.as_view() , name='change_password'),
    path('change-password/done' , auth_views.PasswordChangeDoneView.as_view() , name='password_change_done'),
    path('passsword-reset/' , auth_views.PasswordResetView.as_view() , name='password_reset'),
    path('passsword-reset/done/' , auth_views.PasswordResetDoneView.as_view() ,name='password_reset_done'),
    path('users/passsword-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('passsword-reset/complete/' , auth_views.PasswordResetCompleteView.as_view() ,name='password_reset_complete'),

]
