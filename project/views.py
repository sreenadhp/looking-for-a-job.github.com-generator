#!/usr/bin/env python
from bakery.views import BuildableTemplateView
import django
from django.conf import settings
from django_github_user.models import Gist, Repo, StarredGist, StarredRepo
from django.shortcuts import render


class BaseView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["repos"] = Repo.objects.filter(full_name__contains=settings.GITHUB_USERNAME).filter(fork=False).filter(private=False).all()
        context["starred_repos"] = StarredRepo.objects.filter(private=False).all()
        context["gists"] = Gist.objects.filter(public=True).all()
        context["starred_gists"] = StarredGist.objects.filter(public=True).all()
        context["username"] = settings.GITHUB_USERNAME
        return context


class DynamicView(BaseView, django.views.View):
    template_name = None

    def render(self, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def get(self, request, *args, **kwargs):
        return self.render()


class StaticView(BaseView, BuildableTemplateView):
    pass
