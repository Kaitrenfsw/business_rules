from rest_framework import serializers
from user_preferences.models import Source, TopicUser, ContentUser, SourceUser, DashboardUser

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'
