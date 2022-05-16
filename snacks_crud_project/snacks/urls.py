from django.urls import path
from .views import HomeView, SnackDeleteView, SnackDeleteView, SnackDetailView, SnackListView, SnackUpdateView

urlpatterns = [
  path('', HomeView.as_view(), name='home'),
  path('', SnackListView.as_view(), name='snack_list'),
  path('<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
  path('create/', SnackDeleteView.as_view(), name='snack_create'),
  path('<int:pk>/update/', SnackUpdateView.as_view(), name='snack_update'),
  path('<int:pk>/delete/', SnackDeleteView.as_view(), name='snack_delete'),
]