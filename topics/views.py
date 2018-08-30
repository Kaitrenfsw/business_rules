from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import LdaModel, Topic, Keyword, TopicComparison
from .serializers import LdaModelSerializer, TopicSerializer, KeywordSerializer, TopicComparisonSerializer


class TopicViewSet(viewsets.ViewSet):

	@staticmethod
	def list(request):
		return Response(data={":)"})

	@staticmethod
	def create(request):
		return Response(data={":)"})

	@staticmethod
	def retrieve(request, pk=None):
		return Response(data={":)"})

	@staticmethod
	def update(request, pk=None):
		return Response(data={":)"})

	@staticmethod
	def partial_update(request, pk=None):
		return Response(data={":)"})

	@staticmethod
	def destroy(request, pk=None):
		return Response(data={":)"})


topic_list = TopicViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
})
