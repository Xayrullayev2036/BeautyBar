from django.core.cache import cache
from django.db import models

from apps.master.choices import MasterStatusChoices
from apps.users.models import User
from apps.base.models import BaseModel
from apps.users.choices import GenderChoices


class Master(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="master")
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    description = models.TextField()
    work_hours = models.JSONField()

    def set_work_hours(self, start_time, end_time):
        work_hours = {
            "start_time": start_time,
            "end_time": end_time
        }
        self.work_hours = work_hours

    def get_start_time(self):
        return self.work_hours.get("start_time", None)

    def get_end_time(self):
        return self.work_hours.get("end_time", None)

    master_status = models.CharField(choices=MasterStatusChoices.choices)
    gender = models.CharField(choices=GenderChoices.choices)
    languages = models.CharField(max_length=250)
    experiance = models.CharField(max_length=250)
    age = models.IntegerField()

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'

    def __str__(self):
        return (
            f"{self.first_name}, "
            f"{self.last_name}, "
            f"{self.description}, "
            f"{self.master_status}, "
            f"{self.gender}, "
            f"{self.languages}, "
            f"{self.experiance}, "
            f"{self.age}, "
            f"{self.user}"
        )
