from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from apps.appointment.models import Schedule
from apps.appointment.serializers import ScheduleSerializer, ScheduleCreateSerializer
from apps.master.models import Master
from apps.utils import save_schedule_to_database


class ScheduleCreateAPIView(CreateAPIView):
    serializer_class = ScheduleCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        master_instance = Master.objects.get(id=request.user.id)
        print(master_instance)
        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        start_time = serializer.validated_data['start_time']
        end_time = serializer.validated_data['end_time']
        interval_minutes = serializer.validated_data.get('interval_minutes', 30)
        print(start_date, end_date, start_time, end_time)

        save_schedule_to_database(
            master_instance=master_instance,
            start_date=start_date,
            end_date=end_date,
            start_time=start_time,
            end_time=end_time,
            interval_minutes=interval_minutes
        )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ScheduleListApiView(ListAPIView):
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        schedule = Schedule.objects.all()
        master = Master.objects.get(id=schedule.master.id)
        print(master)
        return master

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
