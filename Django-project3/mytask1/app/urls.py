from django.urls import path
from . views import *

urlpatterns=[
    path("",index),
    path("Registration/", create_user),
    path("data/", table),
    path("delete/<int:pk>/",delete_user, name='delete'),
    path("update/<int:uid>/",update_user,name="update"),
    path("update_user/",update_data)
]