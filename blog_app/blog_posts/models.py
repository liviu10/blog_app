import decimal
from enum import unique
from django.conf import settings
from django.db import models
from datetime import datetime


# Blog categories
class Category(models.Model):
    category_title = models.CharField(
        max_length=100,
        blank=False,
        default='',
        unique=True,
        help_text="Insert the category title",
        verbose_name="Title"
    )
    category_short_description = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the category short description",
        verbose_name="Short description"
    )
    is_active = models.BooleanField(
        blank=True,
        default=False,
        help_text="Activate the category?",
        verbose_name="Active / Inactive?"
    )
    image_url = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the category image url path",
        verbose_name="Image URL"
    )
    category_url = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the category url path",
        verbose_name="Category URL path"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_title


# Blog subcategories
class Subcategory(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='blog_category',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the category id",
        verbose_name="Blog category"
    )
    subcategory_title = models.CharField(
        max_length=100,
        blank=False,
        default='',
        unique=True,
        help_text="Insert the subcategory title",
        verbose_name="Title"
    )
    subcategory_short_description = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the subcategory short description",
        verbose_name="Short description"
    )
    is_active = models.BooleanField(
        blank=True,
        default=False,
        help_text="Activate the subcategory?",
        verbose_name="Active / Inactive?"
    )
    subcategory_url = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the subcategory url path",
        verbose_name="Subcategory URL path"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.subcategory_title


# Blog articles
class Article(models.Model):
    subcategory = models.ForeignKey(
        Subcategory,
        related_name='blog_subcategory',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the subcategory id",
        verbose_name="Blog subcategory"
    )
    author = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the author",
        verbose_name="Author"
    )
    article_time = models.PositiveIntegerField(
        blank=False,
        default=0,
        help_text="Insert the article's reading, listening or viewing time (number of minutes)",
        verbose_name="Time"
    )
    article_title = models.CharField(
        max_length=255,
        blank=False,
        default='',
        unique=True,
        help_text="Insert the title",
        verbose_name="Title"
    )
    article_short_description = models.CharField(
        max_length=255,
        blank=False,
        default='',
        unique=True,
        help_text="Insert the short description",
        verbose_name="Short description"
    )
    article_url = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the article url",
        verbose_name="Article URL path"
    )
    is_active = models.BooleanField(
        blank=True,
        default=False,
        help_text="Activate the article?",
        verbose_name="Active / Inactive?"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.author


# Blog article content
class ArticleContent(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='blog_article_content',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the article id",
        verbose_name="Blog article"
    )
    content = models.CharField(
        max_length=2000,
        blank=True,
        default='',
        help_text="Insert article content",
        verbose_name="Article content"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article content'


# Blog article media
class ArticleMedia(models.Model):
    article = models.ForeignKey(
        Article,
        related_name='blog_article_media',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the article id",
        verbose_name="Blog article"
    )
    media_url = models.CharField(
        max_length=255,
        blank=True,
        default='',
        help_text="Insert article media url path",
        verbose_name="Media url path"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article media'


# Blog article appreciation system
class ArticleAppreciation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_article_appreciation_user',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the user id",
        verbose_name="User ID"
    )
    article = models.ForeignKey(
        Article,
        related_name='blog_article_appreciation',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the article id",
        verbose_name="Blog article"
    )
    rate = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="Insert the article's rate system",
        verbose_name="Rating system"
    )
    like = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="Insert the article's likes",
        verbose_name="No of likes"
    )
    dislike = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="Insert the article's dislikes",
        verbose_name="No of dislikes"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article appreciation'


# Blog article comments
class ArticleComment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_article_comment_user',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the user id",
        verbose_name="User ID"
    )
    article = models.ForeignKey(
        Article,
        related_name='blog_article_comment',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the article id",
        verbose_name="Blog article"
    )
    full_name = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the full name",
        verbose_name="Full name"
    )
    email = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the email address",
        verbose_name="Email address"
    )
    comment = models.CharField(
        max_length=255,
        blank=False,
        default='',
        help_text="Insert the comment",
        verbose_name="Comment"
    )
    is_public = models.BooleanField(
        blank=True,
        default=False,
        help_text="Activate the comment?",
        verbose_name="Public / Private?"
    )
    is_active = models.BooleanField(
        blank=True,
        default=False,
        help_text="Activate the article?",
        verbose_name="Active / Inactive?"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article comment'


# Blog article comment appreciation system
class ArticleCommentAppreciation(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='blog_article_comment_appreciation_user',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the user id",
        verbose_name="User ID"
    )
    article = models.ForeignKey(
        Article,
        related_name='blog_article_comment_appreciation',
        on_delete=models.CASCADE,
        blank=False,
        default='',
        help_text="Insert the article id",
        verbose_name="Blog article"
    )
    like = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="Insert the article's comment likes",
        verbose_name="No of likes"
    )
    dislike = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="Insert the article's comment dislikes",
        verbose_name="No of dislikes"
    )
    created_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Created date"
    )
    updated_at = models.DateTimeField(
        blank=True,
        default=datetime.now(),
        verbose_name="Updated date"
    )

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article comment appreciation'

