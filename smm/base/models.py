from django.db import models
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images import get_image_model_string
from wagtail.images.blocks import ImageChooserBlock


# Reusable snippets
class MemberRole(models.TextChoices):
    PRINCIPAL = "PI", "Principal Investigator"
    PHD = "PH", "PhD Scholar"
    MASTER = "MS", "Master's Student"
    ALUMNI = "AL", "Alumni"


# Member snippet to show under Team
@register_snippet
class Member(models.Model):
    full_name = models.CharField(max_length=50)
    role = models.CharField(
        max_length=2,
        choices=MemberRole.choices,
        default=MemberRole.PHD
    )
    description = RichTextField(blank=True)
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
        FieldPanel("role"),
        FieldPanel("description"),
        FieldPanel("photo"),
        FieldPanel("year"),
        FieldPanel("placed_at"),
    ]

    def __str__(self):
        return self.full_name


# Base pages
class Team(Page):
    hero = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )
    intro = RichTextField(blank=True)
    scholars = StreamField([
        ('scholar', SnippetChooserBlock(Member)),
    ], blank=True)
    masters = StreamField([
        ('master', SnippetChooserBlock(Member)),
    ], blank=True)
    alumni = StreamField([
        ('alumnus', SnippetChooserBlock(Member)),
    ], blank=True)

    content_panels = Page.content_panels + [
        "hero",
        "intro",
        "scholars",
        "masters",
        "alumni",
    ]


class Gallery(Page):
    hero = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )
    intro = RichTextField(blank=True)
    photos = StreamField([
        ('photo', ImageChooserBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        "hero", "intro", "photos",
    ]

