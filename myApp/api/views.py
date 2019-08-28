from rest_framework.generics import ListAPIView, RetrieveAPIView
from myApp.models import Mlab
from .serializers import MlabSerializer


class MlabListView(ListAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer


class MlabDetailView(RetrieveAPIView):
    queryset = Mlab.objects.all()
    serializer_class = MlabSerializer
