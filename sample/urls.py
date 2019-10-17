from django.urls import include , path
from . import views
urlpatterns=[
    path('docs/',views.Home,name='home'),
    path('api/fetch/all/',views.fetch_all , name='all_items'),
    path('api/fetch/',views.fetch_items,name='specific-item'),
]

