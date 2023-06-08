from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.home, name="home"),
    path('products/', view=views.products, name="products"),
    path('customer/<str:pk>/', view=views.customer, name="customer"),
    path('create_order/<str:pk>/', view=views.create_order, name="create_order"),
    path('update_order/<str:pk>/', view=views.update_order, name= "update_order"),
    path('delete_order/<str:pk>/', view=views.delete_order, name= "delete_order"),
    path('login/', view=views.login_page, name="login_page"),
    path('logout/', view=views.logout_user, name="logout_user"),
    path('register/', view=views.register_page, name="register_page"),
    path('user/', view=views.user_page, name="user_page")
]
