from django.urls import path
from . import views
#from views import index

urlpatterns = [
    path("",views.index),
    #path("<int:id>", views.book_detail, name="book-detail")
    path("<slug:slug>", views.book_detail, name="book-detail")
]