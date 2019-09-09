from django.urls import path, include
from knox import views as knox_views
from accounts.api.views import LoginAPI

urlpatterns = [
    path('api/auth', include('knox.urls')),
    path('api/auth/login', LoginAPI.as_view())
]
