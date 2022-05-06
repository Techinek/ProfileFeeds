from django.urls import path

from .views import HiApiView

urlpatterns = [
    path('hi/', HiApiView.as_view(), name='hi')
]
