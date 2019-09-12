from django.urls import path

from .views import MlabListView, MlabDetailView

urlpatterns = [
    path('api/', MlabListView.as_view()),
    path('api/<pk>', MlabDetailView.as_view())

]
