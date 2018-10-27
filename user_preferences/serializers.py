from rest_framework import serializers
from user_preferences.models import Source, TopicUser, DashboardUser, UserGraph, TopicGraph, ContentUser, SourceUser


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'


class TopicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicUser
        fields = ('topic_id',)


class TopicGraphSerializer(serializers.ModelSerializer):
    topic_id = serializers.IntegerField(source='topic_user_id.topic_id.id',read_only=True)
    name = serializers.CharField(source='topic_user_id.topic_id.name',read_only=True)
    class Meta:
        model = TopicGraph
        fields = ('topic_id', 'name',)

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


class ContentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentUser
        fields = ('id', 'content_id')


class SourceUserSerializer(serializers.ModelSerializer):
    user_source = SourceSerializer(many=True)
    class Meta:
        model = SourceUser
        fields = ('id', 'user_id', 'user_source',)


