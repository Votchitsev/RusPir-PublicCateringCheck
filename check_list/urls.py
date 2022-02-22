"""check_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from checks.views import start_view, get_objects_view, LocationFormView, LocationListView, delete_location, \
    ObjectFormView, LocationObjectsListView, ControlEventListView, ControlEventFormView, \
    delete_control_event_view, CheckListFormView, delete_check_list_view, delete_object_view, logout_view

location_patterns = [
    path('list/', LocationListView.as_view(), name='location-list'),
    path('create/', LocationFormView.as_view(), name='location-create'),
    path('delete/', delete_location, name='location-delete'),
    path('<int:id>/', LocationObjectsListView.as_view(), name='location')
]

object_patterns = [
    path('list/', get_objects_view, name='object-list'),
    path('create/', ObjectFormView.as_view(), name='object-create'),
    path('delete/', delete_object_view, name='object-delete')
]

control_event_patterns = [
    path('list/', ControlEventListView.as_view(), name='control-event-list'),
    path('create/', ControlEventFormView.as_view(), name='control-event-create'),
    path('delete/', delete_control_event_view, name='control-event-delete'),
    path('<int:control_event_id>/', CheckListFormView.as_view(), name='control-event'),
    path('delete_position/', delete_check_list_view, name='delete-check-list-position')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_view, name='start_page'),
    path('location/', include(location_patterns)),
    path('object/', include(object_patterns)),
    path('control_event/', include(control_event_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name='logout'),
]
