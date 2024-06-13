from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('contact-agri/', views.contact, name='contact'),
    path('registration-agri/', views.registration_agri, name='registration-agri'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('service-agri/', views.service, name='service'),
    path('testimonail-agri/', views.testimonail, name='testimonail'),
    path('about-agri/', views.about, name='about'),
    path('product/', views.product_agri, name='product_agri'),
    path('cart/', views.cart, name='cart'),
    path('add-cart/<int:pid>/', views.add_cart, name='add_cart'),
    path('plus-cart/<int:cid>/', views.plus_cart, name='plus_cart'),
    path('minus-cart/<int:cid>/', views.minus_cart, name='minus_cart'),
    path('delete-cart/<int:cid>/', views.delete_cart, name='delete_cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add-wishlist/<int:pid>/', views.add_wishlist, name='add_wishlist'),
    path('delete-wishlist/<int:wid>/', views.delete_wishlist, name='delete_wishlist'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmorder/<int:oid>', views.confirmorder, name='confirmorder'),
    path('myorders/', views.myorders, name='myorders'),
    
]
