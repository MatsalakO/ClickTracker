from django.urls import path
from .views import track_click, thank_you

urlpatterns = [
    path("click/", track_click, name="track_click"),
    path("thank-you/", thank_you, name="thank_you"),
]

app_name = "tracker"
