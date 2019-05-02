#!/usr/bin/env python
from django import template

register = template.Library()

"""
https://github.com/collections/programming-languages
"""

COLORS = dict(
    C="#555555",
    Crystal="#000100",
    Dockerfile="#384d54",
    Haskell="#5e5086",
    HTML="#e34c26",
    Shell="#89e051",
    python="#3572A5"
)

"""template.html:
{% load language_color %}

{% language_color repo.language %}
"""


@register.simple_tag
def language_color(language):
    if language:
        for name, value in COLORS.items():
            if name.lower() == language.lower():
                return value
    return "#555555"
