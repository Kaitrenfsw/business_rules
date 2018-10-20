from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import LdaModel, Topic, TopicComparison, KeywordMatch
from .serializers import TopicKeywordSerializer, LdaModelSerializer, TopicSerializer, TopicComparisonSerializer


class TopicViewSet(viewsets.ViewSet):
    queryset = Topic.objects.all()

    @staticmethod
    def list(request):
        topics = Topic.objects.all()
        response_json = []
        response_status = status.HTTP_200_OK
        try:
            for topic in topics:
                serialized_topic = TopicKeywordSerializer(topic).data
                response_json.append(serialized_topic)
                response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND

        return Response(data=response_json, status=response_status)

    @staticmethod
    def create(request):
        serialized_data = TopicKeywordSerializer(data=request.data, many=True)
        try:
            if serialized_data.is_valid():
                serialized_data.save()
                response_message = {"Topics and keywords saved successfully!"}
                response_status = status.HTTP_200_OK
            else:
                response_message = {"Wrong format data"}
                response_status = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            response_message = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_message, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        response_json = []
        try:
            topic = Topic.objects.get(id=pk)
            serialized_topic = TopicKeywordSerializer(topic).data
            response_json.append(serialized_topic)
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={"This is the PUT topic method"})

    @staticmethod
    def partial_update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})


class LdaModelViewSet(viewsets.ViewSet):
    queryset = LdaModel.objects.all()

    @staticmethod
    def list(request):
        return Response(data={"This is the GET LDAModel method"})

    @staticmethod
    def create(request):
        # Data received from Processing service
        model_serialized = LdaModelSerializer(data=request.data)
        if model_serialized.is_valid():
            try:
                #Update old models 'newest' attribute
                old_ldamodels = LdaModel.objects.filter(newest=True)
                for model in old_ldamodels:
                    model.newest = False
                    model.save()

                # Save new model received from Processing service
                model_serialized.save()
                response_message = {"New LDAModel added successfully"}
                response_status = status.HTTP_200_OK

            except Exception as e:
                response_message = {"Exception raised": e}
                response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            response_message = {"Bad Request, check sent parameters"}
            response_status = status.HTTP_400_BAD_REQUEST

        return Response(data=response_message, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def update(request):
        return Response(data={"This is the PUT LDAModel method"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request):
        return Response(data={":)"})


class LdaModelTopicsViewSet(viewsets.ViewSet):
    queryset = LdaModel.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        return Response(data={":)"})

    @staticmethod
    def retrieve(request, pk=None):
        response_json = []
        try:
            topics = Topic.objects.filter(lda_model_id=pk)
            serialized_topics = TopicSerializer(topics, many=True).data
            response_json.append(serialized_topics)
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_404_NOT_FOUND

        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request):
        return Response(data={":)"})


class TopicComparisonViewSet(viewsets.ViewSet):
    queryset = TopicComparison.objects.all()

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        request_data = request.data
        try:
            lda_id = request_data["lda_model_id"]
            topic_numbers = Topic.objects.all().values_list('topic_number', flat=True)

            for relation in request_data["relations"]:
                if (relation["topic_1"] in topic_numbers) and (relation["topic_2"] in topic_numbers):
                    topic_1 = Topic.objects.get(lda_model_id=lda_id, topic_number=relation["topic_1"])
                    topic_2 = Topic.objects.get(lda_model_id=lda_id, topic_number=relation["topic_2"])
                    topic_comparison = TopicComparison(topic1_id=topic_1,
                                                       topic2_id=topic_2,
                                                       distance=relation["distance"])
                    topic_comparison.save()
                    for keyword in relation["keywords_match"]:
                        keyword_match = KeywordMatch(name=keyword, topicComparison_id=topic_comparison)
                        keyword_match.save()

            response_json = {"Topics comparison saved!"}
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        response_json = []
        try:
            topic = Topic.objects.get(id=pk)
            topic_comparison = TopicComparison.objects.filter(topic1_id=topic)
            serialized_comparison = TopicComparisonSerializer(topic_comparison, many=True).data
            response_json.append(serialized_comparison)
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request):
        return Response(data={":)"})

    @staticmethod
    def destroy(request):
        return Response(data={":)"})