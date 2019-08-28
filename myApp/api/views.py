from rest_framework.generics import ListAPIView, RetrieveAPIView
from myApp.models import Mlab
from .serializers import MlabSerializer
from django_filters.rest_framework import DjangoFilterBackend


class MlabListView(ListAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('unique_id', 'mLab_name', 'mLab_city_location', 'mLab_department', 'clinical_condition',)


class MlabDetailView(RetrieveAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
