from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name="home"),
    path('product/<str:pk>',views.product, name="product"),
    path('logout/', views.logoutUser, name="logout"),
   
   
    # path('productlist/<str:pk>/', views.productlist, name="productlist"),
    path('products/', views.products, name="products"),
    path('register/', views.register, name="register"),
    path('login/', views.loginr, name='loginr'),
    
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),

    path('userdash/',views.user_dash, name="user_profile"),
    path('update_acc/',views.update_acc, name="update_acc"),
    # path('cat/<slug:slug>/', views.cat, name='cat'),
    path('type/', views.type, name='type'),

    path('category/<slug:slug>/', views.category, name='category'),

    path('brand/<slug:slug>/<str:pk>/', views.brand, name='brand'),
    path('model/<slug:slug>/<str:pk>/', views.model, name='model'),
    path('year/<slug:slug>/<str:pk>/', views.myear, name='myear'),
    
]