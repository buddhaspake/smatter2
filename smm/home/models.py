from django.db import models
from wagtail.models import Page


class HomePage(Page):
    intent = models.CharField(max_length=700, default="intent")
    methods = models.CharField(max_length=700, default="methods")
    vision = models.CharField(max_length=700, default="vision")

    content_panels = Page.content_panels + [
        "intent",
        "methods",
        "vision",
    ]

