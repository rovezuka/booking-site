# Создать роутеры здесь.

from rest_framework import routers
from .views import ItemViewSet

router = routers.DefaultRouter() # создать объект роутера
router.register(r'item', ItemViewSet) # зарегистрировать роутер с префиксом 'item'
