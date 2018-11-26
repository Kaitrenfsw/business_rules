from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DateConversion
from .serializers import DateConversionSerializer
from datetime import date, datetime, timedelta


class DateConversionViewSet(viewsets.ViewSet):
    queryset = DateConversion.objects.all()
    #                         Year      Month       day
    lookup_value_regex = '([0-9]{4})-([0-9]{2})-([0-9]{2})'

    @staticmethod
    def list(request):
        return Response(data={":)"})

    @staticmethod
    def create(request):
        response_json = ["Dates saved successfully!"]
        response_status = status.HTTP_200_OK

        try:
            if ('start_date' and 'end_date') in request.data:

                # Formatting request
                start_date = datetime.strptime(request.data['start_date'], '%Y-%m-%d')
                end_date = datetime.strptime(request.data['end_date'], '%Y-%m-%d')
                new_date = start_date
                sunday_date = new_date
                week = 1
                week_day = 1

                # Find first Sunday
                if new_date.weekday() != 6:
                    days_left_to_sunday = 6 - new_date.weekday()
                    sunday_date = new_date + timedelta(days=days_left_to_sunday)

                # Main loop
                while new_date <= end_date:

                    # +1 to week code and change sunday date
                    if new_date.weekday() == 0:
                        week = week + 1
                        sunday_date = new_date + timedelta(days=6)

                    # Save data to database
                    date_object = DateConversion(date=new_date.date(), week=week, sunday_date=sunday_date.date())
                    date_object.save()

                    # New day
                    new_date = new_date + timedelta(days=1)
                    week_day = week_day + 1

        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        response_json = []
        end_date = datetime.strptime(pk, '%Y-%m-%d')
        start_date = end_date - timedelta(weeks=23)
        try:
            # Get dates for 6 months
            date_object = DateConversion.objects.filter(date__range=(start_date.date(), end_date.date()))
            serialized_dates = DateConversionSerializer(date_object, many=True).data
            week = 0
            response_data = []
            for date in serialized_dates:
                if week != date["week"]:
                    response_data.append(date)
                week = date["week"]
            #response_json = serialized_dates
            response_status = status.HTTP_200_OK
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_data, status=response_status)

    @staticmethod
    def update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def partial_update(request, pk=None):
        return Response(data={":)"})

    @staticmethod
    def destroy(request, pk=None):
        return Response(data={":)"})
