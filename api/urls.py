from django.contrib import admin
from django.urls import path, include

from api.factories.views import GreetingViewFactory
from api.common.views import ViewWrapper

urlpatterns = [
    path('hello', ViewWrapper.as_view(view_factory=GreetingViewFactory)),
]
