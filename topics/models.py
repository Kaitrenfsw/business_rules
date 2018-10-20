from django.db import models


class LdaModel(models.Model):
    filename = models.CharField(unique=True, max_length=1000)
    creation_date = models.DateField(auto_now=True)
    newest = models.BooleanField(default=True, null=False)
    in_use = models.BooleanField(default=False, null=False)


class Topic(models.Model):
    topic_number = models.IntegerField(null=False)
    coherence = models.FloatField(default=0.5)
    lda_model_id = models.IntegerField(null=False, blank=True)
    name = models.CharField(null=True, blank=True, max_length=100)


class Keyword(models.Model):
    name = models.CharField(null=False, max_length=100)
    weight = models.FloatField()
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='keyword_topic')


class TopicComparison(models.Model):
    topic1_id = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic1_topic2')
    topic2_id = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic2_topic1')
    distance = models.FloatField()

    class Meta:
        unique_together = ('topic1_id', 'topic2_id')


class KeywordMatch(models.Model):
    name = models.CharField(null=False, max_length=100)
    topicComparison_id = models.ForeignKey(TopicComparison, on_delete=models.CASCADE, related_name='keywords_match')

