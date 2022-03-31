from django.urls import path
from .views import test, create_hotel,retrieve_hotel,update_hotel,delete_hotel

urlpatterns = [
    path('test/',test),
    path('create/',create_hotel),
    path('list/',retrieve_hotel),
    path('update/<int:hotel_id>/',update_hotel),
    path('delete/<int:id>/',delete_hotel)

    # path('hotel/crud/',HotelCRUDAPI.as_view())
]
