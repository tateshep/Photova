from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path('',views.HomeView.as_view(), name='gallery'),
    path('new-image/',views.NewImage.as_view(), name='new'),
]

