from django.db import models

from apps.master.models import Master


class Schedule(models.Model):
    master = models.OneToOneField(
        Master,
        on_delete=models.CASCADE,
        related_name='available_times'
    )

    available_times = models.JSONField()

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"

    def __str__(self):
        return str(self.master)
