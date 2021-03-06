from django.contrib import admin
from django.urls import path, include

from api.factories.views import MessageReceiverViewFactory 
from api.common.views import ViewWrapper

urlpatterns = [
    path('', ViewWrapper.as_view(view_factory=MessageReceiverViewFactory))
]
