from rest_framework import serializers
from topics.models import LdaModel, Topic, Keyword, TopicComparison


class LdaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LdaModel
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class TopicComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicComparison
        fields = '__all__'


class TopicKeywordSerializer(serializers.ModelSerializer):
    keyword_topic = KeywordSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'topic_number', 'lda_model', 'name', 'keyword_topic')