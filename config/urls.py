from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("follower",views.follower,name="follower"),
    path("search",views.search,name="search"),
    path("like-post",views.like_post,name="like-post"),
    path("logout",views.Logout,name="logout"),
    path("settings",views.settings,name="settings"),
    path("upload",views.upload,name="upload"),
    path("profile/<str:pk>",views.profile,name="profile"),
]