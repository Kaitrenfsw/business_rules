from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DateConversion
from .serializers import DateConversionSerializer
from datetime import datetime, timedelta


class DateConversionViewSet(viewsets.ViewSet):
    queryset = DateConversion.objects.all()

    lookup_value_regex = '([0-9]{2})/([0-9]{2})/([0-9]{4})'

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
                sunday_date = new_date.strftime('%d/%m/%Y')
                week = 1
                week_day = 1

                # Find first Sunday
                if new_date.weekday() != 6:
                    days_left_to_sunday = 6 - new_date.weekday()
                    fixed_date = new_date + timedelta(days=days_left_to_sunday)
                    sunday_date = fixed_date.strftime('%d/%m/%Y')

                # Main loop
                while new_date <= end_date:
                    formatted_date = new_date.strftime('%d/%m/%Y')

                    # +1 to week code and change sunday date
                    if new_date.weekday() == 0:
                        week = week + 1
                        sunday_date = new_date + timedelta(days=6)
                        sunday_date = sunday_date.strftime('%d/%m/%Y')

                    # Save data to database
                    date_object = DateConversion(date=formatted_date, week=week, sunday_date=sunday_date)
                    date_object.save()

                    print("week:" + str(week) + " | " + "formatted_date: " + formatted_date + " | " + "sunday_date: " + sunday_date)
                    new_date = new_date + timedelta(days=1)
                    week_day = week_day + 1
        except Exception as e:
            response_json = {"Exception raised": e}
            response_status = status.HTTP_500_INTERNAL_SERVER_ERROR
        return Response(data=response_json, status=response_status)

    @staticmethod
    def retrieve(request, pk=None):
        response_json = []
        date = datetime.strptime(pk, '%d/%m/%Y')
        try:
            for i in range(0, 24):
                date_object = DateConversion.objects.get(date=pk)

                serialized_date_code = DateConversionSerializer(date_object).data
                response_json.append(serialized_date_code)

                date = date + timedelta(days=1)
                pk = date.strftime('%d/%m/%Y')
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
