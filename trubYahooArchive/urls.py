"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from .importjson import parse_json
from .views import (
    EmailList,
    EmailDetail,
    IndexView,
    SortableEmailList,
    EmailSearchResultsView,
    EmailSearchList)

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('searchresult/', EmailSearchResultsView.as_view(), name='email-search-results'),
    # path('emails/', EmailList.as_view(), name='email-list'),
    path('emailsSort/', SortableEmailList.as_view(), name='sortable-email-list'),
    path('emailsSearch/', EmailSearchList.as_view(), name='email-search-list'),

    path('email/<int:pk>', EmailDetail.as_view(), name='email-detail'),
    path('importjson', parse_json, name='import-json'),
]
