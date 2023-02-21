"""authors_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Authors Medium Clone API",
        default_version = "v1",
        description="API endpoints for the Authors API project",
        contact=openapi.Contact(email="medium.clone@gmail.com"),
        license=openapi.License(name="MIT license")
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), 
    name="schema-redoc"),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Authors API Admin"
admin.site.site_title = "Authors API Admin Portal"
admin.site.index_title = "Welcome to the Authors Medium API clone Portal"