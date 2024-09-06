from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import ItemViewSet
from .views import SendMessageToSlack

router = DefaultRouter()
# router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notify-message', SendMessageToSlack.as_view(), name='notify-message'),
]