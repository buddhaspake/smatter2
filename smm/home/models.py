from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from base.models.snippets import NewsItem


class HomePage(Page):
    intent = models.CharField(max_length=700, default="intent")
    methods = models.CharField(max_length=700, default="methods")
    vision = models.CharField(max_length=700, default="vision")
    news =  StreamField([
        ("new", SnippetChooserBlock(NewsItem)),
    ], blank=True)

    content_panels = Page.content_panels + [
        "intent",
        "methods",
        "vision",
        "news",
    ]

