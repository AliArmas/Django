from django.contrib import admin
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from models.user.views import UserViewSet

router = DefaultRouter()
router.register('user',UserViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include(router.urls)),
]
