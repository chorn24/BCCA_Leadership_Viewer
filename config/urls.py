"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from app.views import (
    show_info,
    show_team_names,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("teams/<team_name>", show_info, name="Info"),
    path("", show_team_names, name="home"),
]


# path("management", show_management, name="manage"),
# path("community", show_community, name="commune"),
# path("documentation", show_documentation, name="document"),
# path("procurement", show_procurement, name="procure"),
