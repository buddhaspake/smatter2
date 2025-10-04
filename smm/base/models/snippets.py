from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images import get_image_model_string
from wagtail.images.blocks import ImageChooserBlock


# Member snippet to show under Team
@register_snippet
class Member(models.Model):
    full_name = models.CharField(max_length=50)
    description = RichTextField(blank=True, null=True)
    photo = models.ForeignKey(
        get_image_model_string(),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    year = models.IntegerField(blank=True, null=True)
    placed_at = models.CharField(max_length=50, blank=True, null=True)

    panels = [
        FieldPanel("full_name"),
        FieldPanel("description"),
        FieldPanel("photo"),
        FieldPanel("year"),
        FieldPanel("placed_at"),
    ]

    def __str__(self):
        return self.full_name


# NewsItem snippet to show under News
@register_snippet
class NewsItem(models.Model):
    date = models.DateField("Publish date")
    caption = models.CharField(max_length=500)
    photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )
    featured = models.BooleanField(default=False)

    panels = [
        FieldPanel("date"),
        FieldPanel("caption"),
        FieldPanel("photo"),
        FieldPanel("featured"),
    ]

    def __str__(self):
        return self.caption


# Publication snippet to show under Publications
@register_snippet
class Publication(models.Model):
    topic = RichTextField()
    authors = RichTextField()
    citation = models.CharField(max_length=500, blank=True)
    url = models.URLField(max_length=200, blank=True)
    year = models.IntegerField(blank=True)

    panels = [
        FieldPanel("topic"),
        FieldPanel("authors"),
        FieldPanel("citation"),
        FieldPanel("url"),
        FieldPanel("year"),
    ]

    def __str__(self):
        return str(self.topic)

