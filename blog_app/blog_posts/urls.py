from rest_framework import routers
from blog_posts import views

router_product = routers.DefaultRouter()

# API endpoints for blog system
router_product.register('categories', views.CategoryList)
router_product.register('subcategory', views.SubcategoryList)
router_product.register('articles', views.ArticleList)

urlpatterns = router_product.urls
