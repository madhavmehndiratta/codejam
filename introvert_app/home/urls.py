from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('games/', views.games, name='games'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),  
	path('logout/', views.logoutUser, name='logout'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('blog/', views.blog, name='blog'),
    path('music/', views.music, name='music'),
]