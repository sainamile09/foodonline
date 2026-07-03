from django.urls import path
from accounts import views as accountViews
from . import views

urlpatterns=[
    path('',accountViews.vendorDashboard,name = 'vendor'),
    path('profile',views.vProfile,name = 'vProfile'),
]