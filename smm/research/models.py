from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images import get_image_model_string


class ResearchIndexPage(Page):
    hero = models.ForeignKey(
        get_image_model_string(),
        null=True,
        on_delete=models.SET_NULL,
    )
    intro = RichTextField(blank=True)

    def get_context(self, request):
        ctx = super().get_context(request)
        # live = published only
        # -first_published_at = reverse chronological order
        entries = self.get_children().live().order_by('-first_published_at')
        ctx["research_entries"] = entries
        return ctx

    content_panels = Page.content_panels + ["hero", "intro"]


class ResearchEntry(Page):
    date = models.DateField("Publish date")
    research_title = models.CharField(max_length=250)
    description = models.CharField(max_length=2000)
    citation = models.CharField(max_length=250)
    url = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        "date",
        "research_title",
        "description",
        "citation",
        "url",
    ]
