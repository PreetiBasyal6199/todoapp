from .views import index,delete_item,edit_item
from django.urls import path
urlpatterns=[
    path('',index),
    path('del/<int:id>',delete_item),
    path('edit/<int:pk>',edit_item)
]