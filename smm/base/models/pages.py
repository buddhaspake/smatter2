from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.admin.panels import FieldPanel
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

    template = "base/publications_page.html"

    def get_context(self, request, *args, **kwargs):
        ctx = super().get_context(request, *args, **kwargs)
        ctx["publications"] = Publication.objects.all()
        return ctx


class TeamPage(BasePage):
    
    template = "base/team_page.html"

    lead = models.ForeignKey(
        "Member",
        null=True, blank=True,
        on_delete=models.SET_NULL,
    )
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
        FieldPanel("lead"),
        "scholars",
        "masters",
        "alumni",
    ]


class GalleryPage(BasePage):

    template = "base/gallery_page.html"
    
    photos = StreamField([
        ('photo', ImageChooserBlock()),
    ], blank=True)

    content_panels = BasePage.content_panels + [ "photos" ]

