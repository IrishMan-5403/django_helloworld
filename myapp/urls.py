from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.status, name='status'),
    path('status_html/',views.status_html_view , name='status_html'),
]



