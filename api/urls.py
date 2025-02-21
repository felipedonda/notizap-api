from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet, ReminderViewSet, UserRegisterView, Test
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Create a router to handle the API endpoints
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Add API endpoints
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('register', UserRegisterView.as_view()),
    path('test', Test)
]
