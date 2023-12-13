from datetime import datetime

from rest_framework import serializers, status
from rest_framework.response import Response

from apps.appointment.models import Schedule
from apps.master.models import Master
from apps.utils import save_schedule_to_database


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['available_times']


class ScheduleCreateSerializer(serializers.Serializer):
    start_date = serializers.DateField(format="%Y-%m-%d")
    end_date = serializers.DateField(format="%Y-%m-%d")
    start_time = serializers.TimeField(format="%H:%M")
    end_time = serializers.TimeField(format="%H:%M")
    interval_minutes = 30


