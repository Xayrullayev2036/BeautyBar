from django.db import models
from apps.base.models import BaseModel
from apps.services.choices import CategoryTypeChoices


def upload_to(instance, filename):
    return f'media/service_images/{instance.service_name}/{filename}'


class Services(BaseModel):
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="service_category"
    )

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_id"
    )

    service_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to=upload_to)
    time_to_took = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):

        return f"{self.service_name}"

        return f"{self.owner}"



class Category(BaseModel):
    name = models.CharField(max_length=250)
    type = models.CharField(choices=CategoryTypeChoices.choices)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f"{self.name}"
