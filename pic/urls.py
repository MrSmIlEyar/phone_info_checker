from django.urls import path
from .views import check_phone_api, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/check-phone/', check_phone_api, name='check_phone_api'),
]