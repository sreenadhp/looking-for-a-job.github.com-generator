#!/usr/bin/env python
from project.views import DynamicView, StaticView


class IndexView(DynamicView):
    template_name = "starred-gists/index.html"


class StaticView(StaticView):
    build_path = "starred-gists/index.html"
    template_name = "starred-gists/index.html"
