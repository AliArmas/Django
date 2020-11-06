from django.contrib import admin
from django.conf.urls import url
from django.urls import include,re_path
from rest_framework.routers import DefaultRouter
from models.user.views import UserViewSet
from models.product.views import ProductViewSet

router = DefaultRouter()
router.register('users',UserViewSet)
router.register('products',ProductViewSet)

urlpatterns = [
    # url('admin/', admin.site.urls),
    re_path(r'^api/',include(router.urls))
]
