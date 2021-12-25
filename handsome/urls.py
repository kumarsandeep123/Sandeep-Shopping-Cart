
from django.urls import path
from .import views

urlpatterns = [
    path('',views.sandeep,name="sandeep"),
    path('about/',views.about,name="about us"),
    path('contact/',views.contact,name="contact"),
    path('search/',views.search,name="search"),
    path('tracker/',views.tracker,name="tracker"),
    path('checkout/', views.checkout, name="checkout"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
