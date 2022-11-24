from django.urls import path
from .views import *

urlpatterns = [
    path('outcode/<outcode>/', OutcodeView.as_view(),name='outcode'),
    path('nexus/<outcode>/', NexusView.as_view(),name='nexus'),
]