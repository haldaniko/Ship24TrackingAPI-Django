from django.urls import path
from . import views

urlpatterns = [
    path('<str:tracking_id>/', views.track_package_view, name='track_shipment'),
]
