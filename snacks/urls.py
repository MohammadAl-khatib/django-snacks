from django.urls import path
from .views import AboutUsView, HomeView

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name = 'about-us'),
    path('', HomeView.as_view(), name = 'home'),
]