from django import template
from base.models.snippets import NewsItem

register = template.Library()


@register.inclusion_tag("newsitem.html")
def newsitem(new: NewsItem):
    return {"self": new}

