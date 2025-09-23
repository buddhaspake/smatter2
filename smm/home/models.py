from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images import get_image_model_string


class HomePage(Page):
    intent = models.CharField(max_length=700, default="intent")
    methods = models.CharField(max_length=700, default="methods")
    vision = models.CharField(max_length=700, default="vision")

    def get_context(self, request):
        ctx = super().get_context(request)
        feat_news = self.get_children().type(NewsItem)
        ctx["featured_news"] = feat_news
        return ctx

    content_panels = Page.content_panels + [
        "intent",
        "methods",
        "vision",
    ]


class NewsItem(Page):
    date = models.DateField("Publish date")
    caption = models.CharField(max_length=500)
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )
    featured = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        "date",
        "caption",
        "photo",
        "featured",
    ]

