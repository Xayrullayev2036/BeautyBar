from django.core.cache import cache
from django.db import models

from apps.master.choices import MasterStatusChoices
from apps.users.models import User
from apps.base.models import BaseModel
from apps.users.choices import GenderChoices


class Appointment(BaseModel):
    provider_id = models.IntegerField()
    canceled_at__isnull = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Master'
        verbose_name_plural = 'Masters'

    def __str__(self):
        return (
            f"{self.first_name}, "
            f"{self.last_name}, "
            # f"{self.description}, "
            # f"{self.master_status}, "
            # f"{self.gender}, "
            # f"{self.languages}, "
            # f"{self.experiance}, "
            # f"{self.age}, "
            # f"{self.salon}, "
            # f"{self.user}"
        )
