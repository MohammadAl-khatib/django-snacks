from django.urls import path
from .views import AboutUsView, HomeView, SnackListView, SnackLDetailView

urlpatterns = [
    # path('', HomeView.as_view(), name = 'home'),
    path('about-us/', AboutUsView.as_view(), name = 'about-us'),
    path('', SnackListView.as_view(), name = 'snack_list'),
    path("<int:pk>", SnackLDetailView.as_view(), name = 'snack_detail'),
]