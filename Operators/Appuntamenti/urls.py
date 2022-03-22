from django.urls import path
from .views import Operator
urlpatterns = [
    path('', Operator.as_view(),name="operator"),
]