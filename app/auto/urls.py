from django.urls import path
# from .views import CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView
from .views import CarListView, CarDetailView


urlpatterns = [
    path('car_list', CarListView.as_view(), name='car_list'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    # path('car/add/', CarCreateView.as_view(), name='car_add'),
    # path('car/edit/<int:pk>/', CarUpdateView.as_view(), name='car_edit'),
    # path('car/delete/<int:pk>/', CarDeleteView.as_view(), name='car_delete'),
]


