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
        fields = ('name', 'weight',)


class TopicComparisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicComparison
        fields = '__all__'


class TopicKeywordSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('topic_number', 'lda_model_id', 'keywords',)

    def create(self, validated_data):
        keywords_data = validated_data.pop('keywords')
        topic = Topic.objects.create(**validated_data)
        for keyword in keywords_data:
            Keyword.objects.create(topic_id=topic, **keyword)
        return topic
