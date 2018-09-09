from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Source, TopicUser, ContentUser, SourceUser, DashboardUser
from .serializers import SourceSerializer

class SourceViewSet(viewsets.ViewSet):

	@staticmethod
	def list(request):
		sources = Source.objects.all()
		response_json = []
		try:
			for source in sources:
				serialized_source = SourceSerializer(source).data
				response_json.append(serialized_source)
				response_status = status.HTTP_200_OK
		except Exception as e:
			response_json = {"Exception raised": e}
			response_status = status.HTTP_404_NOT_FOUND

		return Response(data=response_json, status=response_status)

	@staticmethod
	def create(request):
		if ('name' and 'site') in request.data:
			try:
				new_source_data = request.data
				new_source = Source(name=new_source_data['name'], site=new_source_data['site'])
				new_source.save()
				response_message = {"New source added successfully"}
				response_status = status.HTTP_200_OK				
				pass
			except Exception as e:
				response_message = {"Bad Request, check sent parameters"}
				response_status = status.HTTP_400_BAD_REQUEST
		else:
			response_message = {"Bad Request, check sent parameters"}
			response_status = status.HTTP_400_BAD_REQUEST

		return Response(data=response_message, status=response_status)

	@staticmethod
	def retrieve(request, pk=None):
		return Response(data={":)"})

	@staticmethod
	def update(request, pk=None):
		return Response(data={"This is the PUT Source method"})

	@staticmethod
	def partial_update(request, pk=None):
		return Response(data={":)"})

	@staticmethod
	def destroy(request, pk=None):
		print(request.data)
		if ('name' and 'site') in request.data:
			try:
				source = Source.objects.get(name=request.data['name'], site=request.data['site'])
				source.delete()
				response_message = {"Source "+source.name+" successfully deleted"}
				response_status = status.HTTP_200_OK
			except Exception as e:
				response_message = {"Bad Request, check sent parameters"}
				response_status = status.HTTP_400_BAD_REQUEST				

		return Response(data=response_message, status=response_status)


source_list = SourceViewSet.as_view({
    'get': 'list',
    'post': 'create',
    'put': 'update',
    'delete': 'destroy',
})

class TopicUserViewSet(viewsets.ViewSet):

	@staticmethod
	def list(request):
		if "user_id" in request.data:
			try:
				#list of topics' ids 
				user_data = request.data
				user_topics_list = TopicUser.objects.filter(user_id=user_data['user_id']).values_list('topic_id', flat=True)
				response_message = []
				for topic in user_topics_list:
					response_message.append(topic)
				response_status = status.HTTP_200_OK
			except Exception as e:
				response_message = {"Exception raised": e}
				response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
		else:
			response_message = {"Bad Request, check sent parameters"}
			response_status = status.HTTP_400_BAD_REQUEST
		return Response(data=response_message, status=response_status)

	@staticmethod
	def create(request):
		return Response(data={":)"})
		
	@staticmethod
	def retrieve(request):
		return Response(data={":)"})

	@staticmethod
	def update(request):
		if ('user_id' and 'user_topics_id') in request.data:
			try:
				data = request.data
				older_topics = TopicUser.objects.filter(user_id=data['user_id']).values_list('topic_id', flat=True)
				updated_topics = data["user_topics_id"]

				# adding new subscriptions
				for new_topic_id in updated_topics:
					if new_topic_id not in older_topics:
						new_topic_user_instance = TopicUser(user_id=data['user_id'], topic_id=new_topic_id)
						new_topic_user_instance.save()
				# unsubscribing
				for old_topic_id in older_topics:
					if old_topic_id not in updated_topics:
						topic_user_instance = TopicUser.objects.get(user_id=data['user_id'], topic_id=old_topic_id)
						topic_user_instance.delete()
				response_message = {"Topics updated successfully!"}
				response_status = status.HTTP_200_OK
			except Exception as e:
				response_message = {"Exception raised": e}
				response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
		else:
			response_message = {"Bad Request, check sent parameters"}
			response_status = status.HTTP_400_BAD_REQUEST

		return Response(data=response_message, status=response_status)
		
	@staticmethod
	def partial_update(request):
		return Response(data={":)"})
		
	@staticmethod
	def destroy(request):
		return Response(data={":)"})
		
topicuser_list = TopicUserViewSet.as_view({
    'post': 'list',
    'put': 'update',
})


