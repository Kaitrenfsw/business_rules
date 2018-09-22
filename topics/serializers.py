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
    keyword_topic = KeywordSerializer(many=True)

    class Meta:
        model = Topic
        fields = ('id', 'topic_number', 'lda_model_id', 'coherence', 'keyword_topic',)

    def create(self, validated_data):
        keywords_data = validated_data.pop('keyword_topic')
        topic = Topic.objects.create(**validated_data)
        for keyword in keywords_data:
            Keyword.objects.create(topic_id=topic, **keyword)
        return topic
