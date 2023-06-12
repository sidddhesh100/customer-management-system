from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

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
    path('user/', view=views.user_page, name="user_page"),
    path('account/', view=views.accounts_settings, name="account_settings"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name= "accounts/password_reset.html"), name="reset_password"),
    path('reset_password_mail_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name= "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name= "password_reset_complete"),
]
