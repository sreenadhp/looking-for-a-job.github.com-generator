from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("stars/", include("apps.starred_repos.urls", namespace="starred_repos")),
    path("starred-gists/", include("apps.starred_gists.urls", namespace="starred_gists")),
    #path("starred-repos/", include("apps.starred_repos.urls", namespace="starred_repos")),
    path("gists/", include("apps.gists.urls", namespace="gists")),
    path("", include("apps.repos.urls", namespace="repos")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

