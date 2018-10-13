from rest_framework import serializers
from utils.models import DateConversion


class DateConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateConversion
        fields = '__all__'