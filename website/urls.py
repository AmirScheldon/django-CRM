from django.urls import path
from .views import home, logout_user, login_user, register, customer_id, delete_customer, add_customer, update_customer

urlpatterns = [
    path('', home, name= 'home'),
    path('register/', register, name= 'register'),
    path('login/', login_user, name= 'login'),
    path('logout/', logout_user, name= 'logout'),
    path('customer-id/<int:pk>', customer_id, name= 'customer-id'),
    path('customer-id/delete/<int:pk>', delete_customer, name= 'delete-customer'),
    path('customer-id/update/<int:pk>', update_customer, name= 'update-customer'),
    path('add_customer', add_customer, name= 'add_customer'),    
        
]