from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
#setting the app name
app_name = 'dateverification'

#url patterns
urlpatterns = [
    path('',views.date_check,name='date-check'),
    path('ping/',views.ping,name='ping'),
]
urlpatterns = format_suffix_patterns(urlpatterns)