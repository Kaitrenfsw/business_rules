from django.db import models
from topics.models import Topic


class TopicUser(models.Model):
    user_id = models.IntegerField(null=False)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='user_topic')

    class Meta:
        unique_together = ("user_id", "topic_id")


class ContentUser(models.Model):
    user_id = models.IntegerField(null=False)
    content_id = models.IntegerField(null=False)

    class Meta:
        unique_together = ('user_id', 'content_id')


class Source(models.Model):
    name = models.CharField(null=False, max_length=100)
    site = models.CharField(null=False, max_length=100)


class SourceUser(models.Model):
    user_id = models.IntegerField(null=False)
    source_id = models.ForeignKey(Source, on_delete=models.CASCADE, related_name='user_source')

    class Meta:
        unique_together = ('user_id', 'source_id')


class DashboardUser(models.Model):
    user_id = models.IntegerField(null=False)


class GraphType(models.Model):
    type = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=20)


class UserGraph(models.Model):
    user_id = models.ForeignKey(DashboardUser, on_delete=models.CASCADE, related_name='graphs_selected')
    graph_type = models.ForeignKey(GraphType, on_delete=models.CASCADE, related_name='type_graph')
    name = models.CharField(null=False, max_length=30, default='Gráfico')


class TopicGraph(models.Model):
    user_graph = models.ForeignKey(UserGraph, on_delete=models.CASCADE, related_name='topics_selected')
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_graph')




