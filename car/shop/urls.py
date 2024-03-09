from django.urls import path
from shop import views
app_name="shop"
urlpatterns = [
    path('',views.allcategories,name="cate"),
    path('product/<p>',views.product,name="product"),
    path('details/<c>',views.details,name="details"),
]