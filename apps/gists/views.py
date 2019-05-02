#!/usr/bin/env python
from project.views import DynamicView, StaticView


class IndexView(DynamicView):
    template_name = "gists/index.html"


class StaticView(StaticView):
    build_path = "gists/index.html"
    template_name = "gists/index.html"
