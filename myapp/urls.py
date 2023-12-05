
from django.urls import path
from . import views 

urlpatterns = [
    path('' , views.index , name="index"),
    path('register' , views.register , name="register"),
    path('login' , views.login , name="login"),
    path('logout' , views.logout, name='logout'),
    path('blog/' , views.blog, name='blog'),
    path('post/<int:pk>' , views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),  # Ensure this line is present
    path('comment/<int:pk>/like/', views.like_comment, name='like_comment'),
    path('create_post/', views.create_post, name='create_post'),

]