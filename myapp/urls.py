from django.urls import path
from .views import MyModelAPIView, UserLoginView, UserRegistrationView, AdminOnlyView

urlpatterns = [
    path('mymodel/', MyModelAPIView.as_view(), name='mymodel-list'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
]