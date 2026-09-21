from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet, BasketModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'produts', ProductModelViewSet)
router.register(r'baskets', BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
