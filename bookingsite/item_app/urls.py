from django.urls import path, include

from .models import Reservation
from .routers import router
from .views import ReservationView

urlpatterns = [
    path('reservation/', ReservationView.as_view())
]

urlpatterns += router.urls
