from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    MultiFieldPanel,
)
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)


@register_setting
class NavigationSettings(BaseGenericSetting):
    x_url = models.URLField(verbose_name="X URL", blank=True)
    mailto = models.EmailField(verbose_name="Contact email", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("x_url"),
                FieldPanel("mailto"),
            ],
            "Contact points",
        )
    ]

