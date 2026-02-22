from django.contrib import admin          
from django.urls import path, include
from rest_framework import routers
from core.views import PatientViewSet, DoctorViewSet, MappingViewSet
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'mappings', MappingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),     
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]