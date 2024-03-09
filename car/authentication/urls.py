from django.urls import path
from authentication import views
app_name="authentication"
urlpatterns = [
    path('register',views.register,name="reg"),
    path('login', views.user_login, name="log"),
    path('logout',views.user_logout,name="logout"),
]