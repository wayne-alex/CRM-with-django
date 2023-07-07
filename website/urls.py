from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.record_user, name='record'),
    path('delete_user/<int:pk>', views.delete_user, name='delete'),
    path('update_record/<int:pk>', views.update_record, name='update'),
    path('add_record/', views.add_record, name='add'),
]
