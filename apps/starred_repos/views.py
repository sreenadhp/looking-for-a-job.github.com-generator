#!/usr/bin/env python
from project.views import DynamicView, StaticView


class IndexView(DynamicView):
    template_name = "starred-repos/index.html"


class StaticView(StaticView):
    build_path = "starred-repos/index.html"
    template_name = "starred-repos/index.html"
