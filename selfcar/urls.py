from django.urls import path

from . import views

app_name = 'selfcar'


urlpatterns = [
    path('', views.selfcar),
    path('selfcar_insert/', views.selfcar_insert),
    path('selfcar_comf/', views.selfcar_comf),
    path('exe_selfcar/', views.exe_selfcar),
    path('exe_search_selfcar/', views.exe_search_selfcar),
    path('exe_delete_selfcar/(?P<selfcarid>\d{1,})/', views.exe_delete_selfcar),
    path('selfcar_reject/', views.selfcar_reject),
    path('selfcar_admin/', views.selfcar_admin),
    path('exe_list_selfcar/', views.exe_list_selfcar),
]