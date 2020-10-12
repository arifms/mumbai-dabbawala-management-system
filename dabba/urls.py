from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('canteen/',views.canteen,name='canteen'),
    path('adddabba/',views.adddabba,name="adddabba"),
    path('register/',views.register,name='register'),
    path('forgot/',views.forgot,name="forgot"),
    path('cart/',views.cart,name="cart"),
    path('payments/',views.payments,name="payments"),
    path('dabbawala/',views.dabbawala,name="dabbawala")
]