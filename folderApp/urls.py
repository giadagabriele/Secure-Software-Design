from django.urls import path

from folderApp.views import ObjectOnDBDetail, ObjectOnDBList

urlpatterns = [
    path('<int:pk>/', ObjectOnDBDetail.as_view()),      #primary key to operate on a object
    path('', ObjectOnDBList.as_view()),         #empty path to list all objects
]