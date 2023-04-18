from django.urls import path
from register import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


app_name='account'
urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refreshtoken'),
]
