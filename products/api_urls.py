from django.urls import path
from products import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include


# API Router

router = DefaultRouter()
router.register('id', views.ProductViewSet)

urlpatterns = [
    # Products API URLs
    path('products/', include(router.urls)),
    path('products_search/', views.ProductAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

