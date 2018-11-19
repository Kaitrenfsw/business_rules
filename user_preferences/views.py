from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Source, TopicUser, Topic, DashboardUser, UserGraph, TopicGraph, GraphType, ContentUser, SourceUser, UserVote
from .serializers import TopicUserSerializer, SourceSerializer, DashboardUserSerializer, ContentUserSerializer, SourceUserSerializer, UserVoteSerializer
from topics.serializers import TopicKeywordSerializer, TopicSerializer


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
                new_subscribed_topics = []
                for new_topic_id in updated_topics:
                    if new_topic_id not in older_topics:
                        new_topic_user_instance = TopicUser(user_id=data['user_id'], topic_id_id=new_topic_id)
                        new_subscribed_topics.append(new_topic_user_instance)
                        new_topic_user_instance.save()

                # unsubscribing
                unsusbcribed_topics = []
                for old_topic_id in older_topics:
                    if old_topic_id not in updated_topics:
                        topic_user_instance = TopicUser.objects.get(user_id=data['user_id'], topic_id=old_topic_id)
                        topic_graph_instance = TopicGraph.objects.filter(topic_user_id=topic_user_instance)
                        unsusbcribed_topics.append(topic_user_instance)
                        topic_graph_instance.delete()
                        topic_user_instance.delete()
                response_message = dict()
                response_message['user_id'] = data['user_id']
                response_message['subscribed_topics'] = TopicUserSerializer(new_subscribed_topics, many=True).data
                response_message['unsubscribed_topics'] = TopicUserSerializer(unsusbcribed_topics, many=True).data
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


class ContentUserViewSet(viewsets.ViewSet):
    queryset = ContentUser.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        response_status = ""
        response_json = {}
        if ('user_id' and 'content_id') in request.data:
            try:
                content_user_data = request.data
                content_user_instance = ContentUser(user_id=content_user_data['user_id'],
                                                    content_id=content_user_data['content_id'])
                content_user_instance.save()
                response_status = status.HTTP_201_CREATED
                response_json = {"Content User created!"}
            except Exception as e:
                response_json = {"Exception raised: ": e}
                response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        try:
            content_user_list = ContentUser.objects.filter(user_id=pk)
            content_serialized = ContentUserSerializer(content_user_list, many=True).data
            serialized_content = dict()
            serialized_content['user_id'] = pk
            serialized_content['contents'] = content_serialized
            response_json = serialized_content
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        try:
            data = request.data
            print(data)
            content_user_preference = ContentUser.objects.get(user_id=int(data["user_id"]), content_id=data["content_id"])
            content_user_preference.delete()
            response_status = status.HTTP_200_OK
            response_json = {"Content User preference deleted!"}

        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})


class SourceUserViewSet(viewsets.ViewSet):
    queryset = SourceUser.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        response_status = ""
        response_json = {}
        if ('user_id' and 'source_id') in request.data:
            try:
                source_user_data = request.data
                source_user_instance = SourceUser(user_id=source_user_data['user_id'],
                                                  source_id_id=source_user_data['source_id'])
                source_user_instance.save()
                response_status = status.HTTP_201_CREATED
                response_json = {"Source User created!"}
            except Exception as e:
                response_json = {"Exception raised: ": e}
                response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        try:
            source_user_list_ids = SourceUser.objects.filter(user_id=pk).values_list('source_id',
                                                                                     flat=True)
            source_list = Source.objects.filter(id__in=source_user_list_ids)
            source_serialized = SourceSerializer(source_list, many=True).data
            serialized_content = dict()
            serialized_content['user_id'] = pk
            serialized_content['sources'] = []
            for source in source_serialized:
                temp_dict = source
                user_source = SourceUser.objects.get(user_id=pk, source_id=source["id"])
                temp_dict["sourceUser_id"] = user_source.pk
                serialized_content["sources"].append(temp_dict)
            response_json = serialized_content
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        try:
            source_user_preference = SourceUser.objects.get(id=pk)
            source_user_preference.delete()
            response_status = status.HTTP_200_OK
            response_json = {"Content User preference deleted!"}
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_json, status=response_status)


class UserVotesViewSet(viewsets.ViewSet):
    queryset = UserVote.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        try:
            user_votes = UserVote.objects.filter(user_id=pk)
            serialized_content = UserVoteSerializer(user_votes, many=True).data
            response_json = serialized_content
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        # Response setup
        response_status = status.HTTP_200_OK
        response_json = {"User preferences updated!"}
        try:
            if ("new_id" and "vote" and "source_id") in request.data:
                data = request.data
                user_vote_instance = UserVote.objects.get(user_id=pk, new_id=data['new_id'])
                user_vote_instance.vote = data['vote']
                user_vote_instance.save()
        except UserVote.DoesNotExist:
            data = request.data
            source_instance = Source.objects.get(id=data['source_id'])
            user_vote_instance = UserVote(user_id=pk,
                                          new_id=data['new_id'],
                                          vote=data['vote'],
                                          source_id=source_instance)
            user_vote_instance.save()
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})


class SourceVotesViewSet(viewsets.ViewSet):
    queryset = Source.objects.all()

    @staticmethod
    def list(request):
        try:
            source_instances = Source.objects.all()
            response_list = []
            for source in source_instances:
                up_votes = len(UserVote.objects.filter(source_id=source, vote=1))
                down_votes = len(UserVote.objects.filter(source_id=source, vote=0))
                serialized_source = SourceSerializer(source).data
                serialized_content = serialized_source
                serialized_content['up_votes'] = up_votes
                serialized_content['down_votes'] = down_votes
                response_list.append(serialized_content)
                serialized_content = {}
            response_json = response_list
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        try:
            source_instance = Source.objects.get(id=pk)
            up_votes = len(UserVote.objects.filter(source_id=source_instance, vote=1))
            down_votes = len(UserVote.objects.filter(source_id=source_instance, vote=0))
            serialized_source = SourceSerializer(source_instance).data
            serialized_content = serialized_source
            serialized_content['up_votes'] = up_votes
            serialized_content['down_votes'] = down_votes
            response_json = serialized_content
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})


class NewVotesViewSet(viewsets.ViewSet):
    queryset = UserVote.objects.all()

    @staticmethod
    def list(request):
        try:
            news_ids = UserVote.objects.all().values_list('new_id', flat=True)
            response_list = []
            for new_id in news_ids:
                up_votes = len(UserVote.objects.filter(new_id=new_id, vote=1))
                down_votes = len(UserVote.objects.filter(new_id=new_id, vote=0))
                serialized_content = dict()
                serialized_content['new_id'] = new_id
                serialized_content['up_votes'] = up_votes
                serialized_content['down_votes'] = down_votes
                response_list.append(serialized_content)
            response_json = response_list
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        try:
            up_votes = len(UserVote.objects.filter(new_id=str(pk), vote=1))
            down_votes = len(UserVote.objects.filter(new_id=str(pk), vote=0))
            serialized_content = dict()
            serialized_content['new_id'] = str(pk)
            serialized_content['up_votes'] = up_votes
            serialized_content['down_votes'] = down_votes
            response_json = serialized_content
            response_status = status.HTTP_200_OK

        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})


class TopicStatsViewSet(viewsets.ViewSet):
    queryset = UserVote.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        user_ids = list(map(int, pk.split("-")))
        try:
            topics = Topic.objects.all()
            response_status = status.HTTP_200_OK
            stats = []
            for topic in topics:
                topic_stats = dict()
                subscribed_amount = len(TopicUser.objects.filter(topic_id=topic, user_id__in=user_ids))
                topic_stats['subscribed_amount'] = subscribed_amount
                topic_stats['topic_name'] = topic.name
                stats.append(topic_stats)
            sorted_stats = sorted(stats, key=lambda k: k['subscribed_amount'], reverse=True)
            response_json = sorted_stats[0:10]

        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})