from django.urls import path
from . import views
urlpatterns = [
    path('api/',views.User_view_api,name='api'),
    path('create_user/',views.create_lei_user.as_view(),name='create')
]
