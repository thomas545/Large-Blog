"""django_project URL Configuration"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls' , namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    # path('register/' , user_views.register , name='register'),
    # path('profile/' , user_views.profile , name='profile'),
    # path('login/' , auth_views.LoginView.as_view(template_name='users/login.html') , name='login'),
    # path('logout/' , auth_views.LogoutView.as_view(template_name='users/logout.html') , name='logout'),
    # path('change-password/' , auth_views.PasswordChangeView.as_view(template_name='users/change_password.html') , name='change_password'),
    # path('change-password/done' , auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html') , name='password_change_done'),
    # path('passsword-reset/' , auth_views.PasswordResetView.as_view(template_name='users/password_reset.html') ,name='password_reset'),
    # path('passsword-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html') ,name='password_reset_confirm'),
    # path('passsword-reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html') ,name='password_reset_done'),
    # path('passsword-reset/complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html') ,name='password_reset_complete'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
