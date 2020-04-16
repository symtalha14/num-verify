from django.urls import include , path
from . import views
urlpatterns=[
    path('docs/',views.Home,name='home'),
    path('api/fetch/all/',views.fetch_all , name='all_items'),
    path('api/fetch/',views.fetch_items,name='specific-item'),
    path('api/admin/stats/',views.stats,name='stats'),
    path('api/prefix/fetch/all/',views.get_all_prefix,name='all_prefix'),
    path('api/fetch/countries/', views.fetch_country_names,name="country_names"),
   # path('temp/',views.temp,name='temp'),
]

