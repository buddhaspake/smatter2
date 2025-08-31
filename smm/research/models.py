from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page


class ResearchIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        ctx = super().get_context(request)
        # live = published only
        # -first_published_at = reverse chronological order
        entries = self.get_children().live().order_by('-first_published_at')
        ctx["research_entries"] = entries
        return ctx

    content_panels = Page.content_panels + ["intro"]


class ResearchEntry(Page):
    date = models.DateField("Publish date")
    header = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + ["date", "header", "body"]
