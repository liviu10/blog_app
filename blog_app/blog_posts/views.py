from rest_framework import viewsets, permissions
from blog_app.blog_posts import serializers
from blog_app.blog_posts.models import *


# Category view set
class CategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = [permissions.AllowAny]


# Subcategory view set
class SubcategoryList(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer
    permission_classes = [permissions.AllowAny]


# Article view set
class ArticleList(viewsets.ModelViewSet):
    queryset = Article.objects.select_related(
        'blog_article_content',
        'blog_article_media',
        'blog_article_appreciation',
        'blog_article_comment',
        'blog_article_comment_appreciation'
    )
    serializer_class = serializers.ArticleSerializer
    permission_classes = [permissions.AllowAny]

