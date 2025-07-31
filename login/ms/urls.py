from django.urls import path
from . import views
urlpatterns = [
    path('',views.query,name="app"),
    path('register/',views.register,name="register"),
    path('create_blog/',views.create_blog, name="blog"),
    path('<int:blog_update>/update_blog',views.blog_update, name="update"),
    path('<int:delete_blog>/delete_blog',views.blog_delete, name="delete"),
    path('<int:id_profile>/change_profile',views.profile_change, name="change"),

]