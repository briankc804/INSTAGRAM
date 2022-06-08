from django.urls import path, include
from .views import (PostListView, PostCreateView)

app_name ='insta'

urlpatterns = [
     #local :  http://127.0.0.1:8000/
     path('', PostListView.as_view(),name='post-list'),
     path('new/',PostCreateView.as_view(), name='post-create'),
     path('members/', include('django.contrib.auth.urls')),
     path('members/',include('members.urls')),
]
