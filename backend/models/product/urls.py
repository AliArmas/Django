from django.conf.urls import url,re_path
from django.urls import include
from rest_framework.routers import DefaultRouter
from models.product.views import ProductViewSet

router = DefaultRouter()
router.register('products',ProductViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
