from rest_framework import serializers
from blog_app.blog_posts.models import *


# Category serializer class
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'category_title',
            'category_short_description',
            'is_active',
            'image_url',
            'category_url'
        ]


# Subcategory serializer class
class SubcategorySerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = [
            'id',
            'category',
            'subcategory_title',
            'subcategory_short_description',
            'is_active',
            'subcategory_url'
        ]


# Article content serializer class
class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleContent
        fields = [
            'id',
            'article',
            'content'
        ]


# Article media serializer class
class ArticleMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleMedia
        fields = [
            'id',
            'article',
            'media_url'
        ]


# Article appreciation serializer class
class ArticleAppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleAppreciation
        fields = [
            'id',
            'user',
            'article',
            'rate',
            'like',
            'dislike'
        ]


# Article comment serializer class
class ArticleCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleComment
        fields = [
            'id',
            'user',
            'article',
            'full_name',
            'email',
            'comment',
            'is_public',
            'is_active'
        ]


# Article comment appreciation serializer class
class ArticleCommentAppreciationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCommentAppreciation
        fields = [
            'id',
            'user',
            'article',
            'like',
            'dislike'
        ]


# Article serializer class
class ArticleSerializer(serializers.ModelSerializer):

    subcategory = SubcategorySerializer(read_only=True)
    blog_article_content = ArticleContentSerializer(read_only=True)
    blog_article_media = ArticleMediaSerializer(read_only=True)
    blog_article_appreciation = ArticleAppreciationSerializer(read_only=True)
    blog_article_comment = ArticleCommentSerializer(read_only=True)
    blog_article_comment_appreciation = ArticleCommentAppreciationSerializer(read_only=True)

    class Meta:
        model = Article
        fields = [
            'id',
            'subcategory',
            'author',
            'article_time',
            'article_title',
            'article_short_description',
            'blog_article_content',
            'blog_article_media',
            'blog_article_appreciation',
            'blog_article_comment',
            'blog_article_comment_appreciation',
            'article_url',
            'is_active'
        ]

