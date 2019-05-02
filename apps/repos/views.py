#!/usr/bin/env python
from project.views import DynamicView, StaticView


class IndexView(DynamicView):
    template_name = "index.html"


class StaticView(StaticView):
    build_path = "index.html"
    template_name = "index.html"
