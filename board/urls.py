from django.conf.urls import  include, url
from . import views
from django.urls import path,include,re_path
urlpatterns=[
    path('',views.index,name="main"),
    path('login/', views.sign_in, name="sign-in"),
    path('signup/', views.signup, name="sign-up"),
    path('new_topic/', views.new_topic, name="new-topic"),
    re_path(r'^topic/(?P<topic_id>\d+)/$', views.topic_detail, name = "topic-detail"),
    path('add_post/', views.add_post, name = "add-post"),
    path('delete_post/', views.delete_post, name = "delete-post"),
    path('logout/', views.logout_view, name = "logout"),
]
