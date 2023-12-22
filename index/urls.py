from django.urls import path
from .views import index_page
urlpatterns=[path('',index_page.as_view(),name='load_index_page')]