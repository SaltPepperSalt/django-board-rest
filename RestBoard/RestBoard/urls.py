"""RestBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from bbs.views import ArticleViewset, ArticleDetailView, ArticleUpdate, ArticleDelete, ArticleCreate

# router= routers.DefaultRouter()
# router.register('get_article', ArticleViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ArticleViewset.as_view(), name="article-list"),
    path('create/', ArticleCreate.as_view(), name="article-create"),
    path('detail/<id>', ArticleDetailView.as_view(), name="article-detail"),
    path('update/<id>', ArticleUpdate.as_view(), name="article-update"),
    path('delete/<id>', ArticleDelete.as_view(), name="article-delete"),
]
