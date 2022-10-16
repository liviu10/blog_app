from django.contrib import admin
from blog_posts.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category_title',
        'category_short_description',
        'is_active',
        'image_url',
        'category_url'
    )


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'category',
        'subcategory_title',
        'subcategory_short_description',
        'is_active',
        'subcategory_url'
    )


class ArticleContentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'article',
        'content'
    )


class ArticleMediaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'article',
        'media_url'
    )


class ArticleAppreciationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'article',
        'rate',
        'like',
        'dislike'
    )


class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'article',
        'full_name',
        'email',
        'comment',
        'is_public',
        'is_active'
    )


class ArticleCommentAppreciationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'article',
        'like',
        'dislike'
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'subcategory',
        'author',
        'article_time',
        'article_title',
        'article_short_description',
        'article_url',
        'is_active'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ArticleContent, ArticleContentAdmin)
admin.site.register(ArticleMedia, ArticleMediaAdmin)
admin.site.register(ArticleAppreciation, ArticleAppreciationAdmin)
admin.site.register(ArticleComment, ArticleCommentAdmin)
admin.site.register(ArticleCommentAppreciation, ArticleCommentAppreciationAdmin)
admin.site.register(Article, ArticleAdmin)