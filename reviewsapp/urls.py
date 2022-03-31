
from django.urls import path
from .views import test, create_review,retrieve_hotel_reviews

urlpatterns = [
    path('test/',test),
    path('create/',create_review),
    path('list/',retrieve_hotel_reviews)
]
