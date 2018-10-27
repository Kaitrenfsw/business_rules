from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Source, TopicUser, Topic, DashboardUser, UserGraph, TopicGraph, GraphType
from .serializers import SourceSerializer, DashboardUserSerializer
from topics.serializers import TopicKeywordSerializer


class SourceViewSet(viewsets.ViewSet):
    queryset = Source.objects.all()

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
        response_message = ""
        response_status = ""
        try:
            source = Source.objects.get(id=pk)
            source.delete()
            response_message = {"Source successfully deleted"}
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_message = {"Exception raised: ": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_message, status=response_status)


class TopicUserViewSet(viewsets.ViewSet):
    queryset = TopicUser.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        try:
            user_topics = TopicUser.objects.filter(user_id=pk).values_list('topic_id')
            topics = Topic.objects.filter(id__in=user_topics)
            response_message = []
            for topic in topics:
                serialized_topic = TopicKeywordSerializer(topic).data
                response_message.append(serialized_topic)
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_message = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_message, status=response_status, content_type='application/json')

    @staticmethod
    def update(request, pk=None):
        if ('user_id' and 'user_topics_id') in request.data:
            try:
                data = request.data
                older_topics = TopicUser.objects.filter(user_id=data['user_id']).values_list('topic_id', flat=True)
                updated_topics = data["user_topics_id"]

                # adding new subscriptions
                for new_topic_id in updated_topics:
                    if new_topic_id not in older_topics:
                        new_topic_user_instance = TopicUser(user_id=data['user_id'], topic_id_id=new_topic_id)
                        new_topic_user_instance.save()
                # unsubscribing
                for old_topic_id in older_topics:
                    if old_topic_id not in updated_topics:
                        topic_user_instance = TopicUser.objects.get(user_id=data['user_id'], topic_id=old_topic_id)
                        topic_graph_instance = TopicGraph.objects.filter(topic_user_id=topic_user_instance)
                        topic_graph_instance.delete()
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


class DashboardUserViewSet(viewsets.ViewSet):
    queryset = DashboardUser.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        try:
            dashboard_user_instance = DashboardUser.objects.get(user_id=pk)
            serialized_preferences = DashboardUserSerializer(dashboard_user_instance).data
            print(serialized_preferences)
            # response_json.append(serialized_preferences)
            response_status = status.HTTP_200_OK
        except DashboardUser.DoesNotExist:
            dashboard_user_instance = DashboardUser(user_id=pk)
            dashboard_user_instance.save()
            dashboard_user_instance = DashboardUser.objects.get(user_id=pk)
            serialized_preferences = DashboardUserSerializer(dashboard_user_instance).data
            print(serialized_preferences)
        return Response(data=serialized_preferences, status=response_status)


    @staticmethod
    def update(request, pk=None):
        # Response setup
        response_status = status.HTTP_200_OK
        response_json = {"User preferences updated!"}
        try:
            dashboard_user_instance = DashboardUser.objects.get(user_id=pk)
            if "graphs_selected" in request.data:
                # Delete older preferences
                user_preferences = UserGraph.objects.filter(user_id=dashboard_user_instance)
                user_preferences.delete()

                # Save new preferences
                new_preferences = request.data
                for graph_preference in new_preferences['graphs_selected']:
                    graph_type_instance = GraphType.objects.get(type=graph_preference['graph_type'])
                    new_user_graph = UserGraph(user_id=dashboard_user_instance,
                                               graph_type=graph_type_instance,
                                               name=graph_preference['name'])
                    new_user_graph.save()
                    for topic_selected in graph_preference['topics_selected']:
                        topic_instance = Topic.objects.get(id=topic_selected['topic_id'])
                        topic_user_instance = TopicUser.objects.get(user_id=pk, topic_id=topic_instance)
                        new_topic_selected = TopicGraph(user_graph=new_user_graph,
                                                        topic_user_id=topic_user_instance)
                        new_topic_selected.save()
        except DashboardUser.DoesNotExist:
            dashboard_user_instance = DashboardUser(user_id=pk)
            dashboard_user_instance.save()
            dashboard_user_instance = DashboardUser.objects.get(user_id=pk)
            if 'graphs_selected' in request.data:
                # Delete older preferences
                user_preferences = UserGraph.objects.filter(user_id=dashboard_user_instance)
                user_preferences.delete()

                # Save new preferences
                new_preferences = request.data
                for graph_preference in new_preferences['graphs_selected']:
                    graph_type_instance = GraphType.objects.get(type=graph_preference['graph_type'])
                    new_user_graph = UserGraph(user_id=dashboard_user_instance,
                                               graph_type=graph_type_instance,
                                               name=graph_preference['name'])
                    new_user_graph.save()
                    for topic_selected in graph_preference['topics_selected']:
                        topic_instance = Topic.objects.get(id=topic_selected['topic_id'])
                        topic_user_instance = TopicUser.objects.get(user_id=pk, topic_id=topic_instance)
                        new_topic_selected = TopicGraph(user_graph=new_user_graph,
                                                        topic_user_id=topic_user_instance)
                        new_topic_selected.save()
        return Response(data=response_json, status=response_status)

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        try:
            user_dashboard_instance = DashboardUser.objects.get(user_id=pk)
            user_preferences = UserGraph.objects.filter(user_id=user_dashboard_instance)
            user_preferences.delete()
            response_status = status.HTTP_200_OK
            response_json = {"User preferences deleted!"}
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_json, status=response_status)

