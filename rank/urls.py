from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_user_score, name='add_user_score'),
    path('top10/', views.top_10_users, name='top_10_users'),
     path('update/<str:username>/', views.update_user_score, name='update_user_score'),
]
