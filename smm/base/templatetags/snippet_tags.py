from django import template
from base.models.snippets import NewsItem, Publication

register = template.Library()


@register.inclusion_tag("newsitem.html")
def newsitem(new: NewsItem):
    return {"self": new}


@register.inclusion_tag("publications_table.html")
def publications_table():
    publications = Publication.objects.all().order_by("year").reverse()
    indices = list(range(len(publications), 0, -1))
    return {"publications": list(zip(indices, publications))}

