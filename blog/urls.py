from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('filter/<str>/', views.post_filter, name='post_filter'),
    path('filter/<int:year>/<int:month>/', views.month_archive, name='month_archive'),
]
