from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DateConversion
from .serializers import DateConversionSerializer
from datetime import datetime, timedelta


class DateConversionViewSet(viewsets.ViewSet):
    queryset = DateConversion.objects.all()

    lookup_field = 'date_value'
    lookup_value_regex = '[-\w]+'

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        response_json = ["Dates saved successfully!"]
        response_status = status.HTTP_200_OK

        try:
            if ('start_date' and 'end_date') in request.data:
                start_date = datetime.strptime(request.data['start_date'], '%d/%m/%Y')
                end_date = datetime.strptime(request.data['end_date'], '%d/%m/%Y')
                new_date = start_date
                week = 1
                week_day = 1
                while new_date <= end_date:
                    formatted_date = new_date.strftime('%d/%m/%Y')
                    if week_day % 8 == 0:
                        week = week + 1
                    # Save data to database
                    date_object = DateConversion(date=formatted_date, week=week)
                    date_object.save()

                    print("week:" + str(week) + " | " + formatted_date)
                    new_date = new_date + timedelta(days=1)
                    week_day = week_day + 1
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, date_value=None):
        response_json = []
        try:
            date_object = DateConversion.objects.get(date=date_value)
            serialized_date_code = DateConversionSerializer(date_object).data
            response_json.append(serialized_date_code)
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR

        return Response(data=response_json, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})
