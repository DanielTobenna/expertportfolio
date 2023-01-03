from django.urls import path

from . import views

urlpatterns=[
	path('', views.home, name='home'),
	path('putri_perbesi/', views.putri_perbesi, name='putri_perbesi' ),
	path('sendMessage/', views.sendMessage, name='sendMessage')
]