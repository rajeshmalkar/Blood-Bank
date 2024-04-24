from django.urls import path
from bank import views

urlpatterns = [
    path('about',views.about),
    #path('hello',views.hello),
    path('',views.home),
    path('About',views.About),
    path('contact',views.Contact),
    path('register',views.register),
    #path('login',views.user_login),
    path('login/', views.user_login, name='user_login'),
    path('logout',views.user_logout),
    path('profile',views.profile),


  
]