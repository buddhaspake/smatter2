from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string


class PublicationsPage(Page):
    hero = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )

    content_panels = Page.content_panels + ["hero"]


class Publication(Page):
    authors = RichTextField()
    citation = models.CharField(max_length=500, blank=True)
    url = models.URLField(max_length=200, blank=True)
    year = models.IntegerField(blank=True)

    content_panels = Page.content_panels + [
        "authors",
        "citation",
        "url",
        "year",
    ]

