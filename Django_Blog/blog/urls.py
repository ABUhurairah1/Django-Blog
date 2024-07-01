from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from blog.views import *

urlpatterns = [

    path("",Home,name='Home'),
    path('Blog/<str:blog_id>/',Blog_page,name='Blog'),
    path('create-blog/',Add_Blog,name="Create-Blog"),
    path('update-blog/<str:blog_id>',Update_Blog,name="Update-Blog"),
    path('delete-blog/<str:blog_id>',Delete_Blog,name="Delete-Blog"),
    path('sign-up/',Sign_up,name='Sign-up'),
    path('login/',Login,name='Login'),
    path('logout/',Logout,name='Logout'),
    path('password-change/',Password_change,name='Password-change'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password_reset'),
    
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
