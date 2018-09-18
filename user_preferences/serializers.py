from rest_framework import serializers
from user_preferences.models import Source, TopicUser


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class TopicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicUser
        fields = ('topic_id',)
