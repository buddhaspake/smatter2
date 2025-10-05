from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from base.models import BasePage


class ResearchIndexPage(BasePage):

    def get_context(self, request):
        ctx = super().get_context(request)
        # live = published only
        # -first_published_at = reverse chronological order
        entries = self.get_children().live().order_by('-first_published_at')
        ctx["research_entries"] = entries
        return ctx


class ResearchEntry(Page):
    date = models.DateField("Publish date")
    body = RichTextField()
    citation = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        "date",
        "body",
        "citation",
        "url",
    ]

