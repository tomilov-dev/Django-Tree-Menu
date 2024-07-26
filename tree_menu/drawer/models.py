from django.db import models
from django.urls import reverse


class MenuModel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name


class MenuItemModel(models.Model):
    menu = models.ForeignKey(
        MenuModel,
        on_delete=models.CASCADE,
        related_name="items",
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="children",
        blank=True,
        null=True,
    )

    @property
    def url(self) -> str:
        return reverse("menu-item", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name
