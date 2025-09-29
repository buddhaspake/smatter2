from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images import get_image_model_string
from base.models.snippets import Member, Publication


# Base pages
class BasePage(Page):
    hero = models.ForeignKey(
        get_image_model_string(),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        "hero",
        "intro",
    ]

    class Meta:
        abstract = True


class PublicationsPage(BasePage):
    publications = StreamField([
        ('publication', SnippetChooserBlock(Publication)),
    ], blank=True)

    content_panels = BasePage.content_panels + [ "publications" ]


class TeamPage(BasePage):
    scholars = StreamField([
        ('scholar', SnippetChooserBlock(Member)),
    ], blank=True)
    masters = StreamField([
        ('master', SnippetChooserBlock(Member)),
    ], blank=True)
    alumni = StreamField([
        ('alumnus', SnippetChooserBlock(Member)),
    ], blank=True)

    content_panels = BasePage.content_panels + [
        "scholars",
        "masters",
        "alumni",
    ]


class GalleryPage(BasePage):
    photos = StreamField([
        ('photo', ImageChooserBlock()),
    ], blank=True)

    content_panels = BasePage.content_panels + [ "photos" ]

