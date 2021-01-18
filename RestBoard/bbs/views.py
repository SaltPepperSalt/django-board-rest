from .models import Article
from .serializer import ArticleSerializer, ArticleDetailSerializer, ArticleCreateSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

class ArticleViewset(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer


class ArticleUpdate(UpdateAPIView):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDelete(DestroyAPIView):
    lookup_field = 'id'
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleCreate(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

