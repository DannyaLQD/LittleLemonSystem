from django.contrib import admin
from rest_framework import routers
from Restaurant import views
from django.urls import path, include

# Configuración del router
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'booking', views.BookingViewSet)  # Registro de la vista BookingViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('Restaurant.urls')),  # Incluye las URLs de la app Restaurant
    path('', include(router.urls)),  # Rutas del router principal
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Autenticación de la API
]
