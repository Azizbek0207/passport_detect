from django.urls import path
from .views import ImageUploadView, PassportInfoView

urlpatterns = [
    path('', ImageUploadView.as_view(), name='image_upload'),
    path('passport/', PassportInfoView.as_view(), name='passport_info'),
]
