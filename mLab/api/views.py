from rest_framework.generics import ListAPIView, RetrieveAPIView
from mLab.models import Mlab
from .serializers import MlabSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions


class MLabFilter(filters.FilterSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    mLab_name = filters.CharFilter(field_name="mLab_name", lookup_expr='icontains')
    mLab_city_location = filters.CharFilter(field_name="mLab_city_location", lookup_expr='icontains')
    mLab_department = filters.CharFilter(field_name="mLab_department", lookup_expr='icontains')
    clinical_condition = filters.CharFilter(field_name="clinical_condition", lookup_expr='icontains')
    session_videos = filters.CharFilter(field_name="session_videos", lookup_expr='icontains')
    session_drs = filters.CharFilter(field_name="session_drs", lookup_expr='icontains')

    class Meta:
        model = Mlab
        fields = ('mLab_name', 'mLab_city_location', 'mLab_department', 'clinical_condition', 'session_videos',
                  'session_drs',)


class MlabListView(ListAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MLabFilter


class MlabDetailView(RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
