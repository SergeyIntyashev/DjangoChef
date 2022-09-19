from django.urls import path

from blog import views

urlpatterns = [
    path('<slug:slug>/', views.PostListView.as_view(), name='post_list'),
    path(
        '<slug:slug>/<slug:post_slug>',
        views.PostDetailView.as_view(),
        name='post_detail'
    ),
    path('', views.HomeView.as_view(), name='home')
]
