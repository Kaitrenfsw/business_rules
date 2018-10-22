from rest_framework import serializers
from user_preferences.models import Source, TopicUser, DashboardUser, UserGraph, TopicGraph


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class TopicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicUser
        fields = ('topic_id',)


class TopicGraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicGraph
        fields = ('topic_id',)

class UserGraphSerializer(serializers.ModelSerializer):
    topics_selected = TopicGraphSerializer(many=True)
    class Meta:
        model = UserGraph
        fields = ('graph_type', 'name', 'topics_selected',)


class DashboardUserSerializer(serializers.ModelSerializer):
    graphs_selected = UserGraphSerializer(many=True)
    class Meta:
        model = DashboardUser
        fields = ('user_id', 'graphs_selected',)


