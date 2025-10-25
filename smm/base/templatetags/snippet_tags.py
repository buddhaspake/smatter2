from django import template
from wagtail.images.models import Image as WagtailImage
from base.models.snippets import NewsItem, Publication, Member

register = template.Library()


@register.inclusion_tag("newsitem.html")
def newsitem(new: NewsItem):
    return {"self": new}


@register.inclusion_tag("publications_table.html")
def publications_table():
    publications = Publication.objects.all().order_by("year").reverse()
    indices = list(range(len(publications), 0, -1))
    return {"publications": list(zip(indices, publications))}


@register.inclusion_tag("member.html")
def member(member: Member):
    return {"self": member}


@register.inclusion_tag("gallery_photo.html")
def gallery_photo(image: WagtailImage):
    return {"self": image}

