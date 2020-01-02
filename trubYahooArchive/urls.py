from django.conf.urls import url

from .views import (
    parse_json,
)

urlpatterns = [
    url(r'^importjson', parse_json),
]

