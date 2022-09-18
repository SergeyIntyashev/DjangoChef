from django.urls import path

from blog import views

urlpatterns = [
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path('', views.home)
]
