from django .urls import path 
from . import views

urlpatterns = [
    path('',views.user_login),
    path('logout',views.user_logout),
    path('register',views.register),
    path('vault',views.vault),
    path('add/<id>',views.add),
    




]