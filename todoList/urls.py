from .views import index,delete_item,edit_item,add_item
from django.urls import path
urlpatterns=[
    path('',index),
    path('add/',add_item),
    path('del/<int:id>',delete_item),
    path('edit/<int:pk>',edit_item)
]