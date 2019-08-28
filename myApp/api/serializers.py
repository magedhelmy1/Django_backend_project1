from rest_framework import serializers
from myApp.models import Mlab


class MlabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mlab
        fields = ('unique_id', 'mLab_name', 'mLab_city_location', 'mLab_department', 'clinical_condition')
