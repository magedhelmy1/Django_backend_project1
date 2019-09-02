from django.urls import path

from .views import MlabListView, MlabDetailView

urlpatterns = [
    path('', MlabListView.as_view()),
    path('<pk>', MlabDetailView.as_view())

]
