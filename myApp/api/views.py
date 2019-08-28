from rest_framework.generics import ListAPIView, RetrieveAPIView
from myApp.models import Mlab
from .serializers import MlabSerializer
from django_filters import rest_framework as filters


class MLabFilter(filters.FilterSet):
    mLab_name = filters.CharFilter(field_name="mLab_name", lookup_expr='icontains')
    mLab_city_location = filters.CharFilter(field_name="mLab_city_location", lookup_expr='icontains')
    mLab_department = filters.CharFilter(field_name="mLab_department", lookup_expr='icontains')
    clinical_condition = filters.CharFilter(field_name="clinical_condition", lookup_expr='icontains')

    class Meta:
        model = Mlab
        fields = ('mLab_name', 'mLab_city_location', 'mLab_department', 'clinical_condition',)


class MlabListView(ListAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MLabFilter


class MlabDetailView(RetrieveAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
