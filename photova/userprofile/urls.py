from django.urls import path
from . import views

app_name = "userprofile"

urlpatterns = [
    path('user-list/',views.UserListView.as_view(), name = "user_list"),
    path('signup/', views.SignUpView.as_view(), name = "signup"),
]