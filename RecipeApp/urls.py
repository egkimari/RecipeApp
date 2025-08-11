from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from recipes.views import CategoryViewSet, RecipeViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
