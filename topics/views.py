from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import LdaModel, Topic
from .serializers import TopicKeywordSerializer, LdaModelSerializer


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
            response_status = status.HTTP_404_NOT_FOUND

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
    def retrieve(request):
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