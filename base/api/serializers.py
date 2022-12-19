from base.models import Room
from rest_framework.serializers import ModelSerializer


class roomSerializer(ModelSerializer):
  class Meta:
    model = Room
    fields = '__all__'