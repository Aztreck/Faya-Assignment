from django.urls import path, include
from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet, ProductViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('customers', CustomerViewSet, basename='customer')
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
