from django.urls import path,include
from . import views
from accounts import views as Accountview

urlpatterns = [
    path('', Accountview.vendorDashboard, name="vendor"),
    path('profile', views.vprofile, name='vprofile'),
]