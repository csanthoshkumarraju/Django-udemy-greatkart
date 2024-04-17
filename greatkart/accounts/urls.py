from .  import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register.html/',views.register,name = 'register'),
    path('signin.html/',views.login,name = 'login'),
    path('logout/',views.logout,name = 'logout'),
    path('dashboard/',views.dashboard,name = 'dashboard'),
    path('forgotpassword/',views.forgotpassword,name = 'forgotpassword'),
    path('resetpassword/',views.resetpassword,name = 'resetpassword'),
    # path('activate/<uidb64>/<token>/',views.activate,name = 'activate'),
] 
