
from django.urls import path
from .views import test, create_review

urlpatterns = [
    path('test/',test),
    path('create/',create_review)
]
