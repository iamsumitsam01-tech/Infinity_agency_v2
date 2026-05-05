<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout,name='checkout'),

    path('crm/', views.crm, name='crm'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('update-status/<int:id>/<str:status>/', views.update_status, name='update_status'),
    path('export/', views.export_contacts, name='export_contacts'),

    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),   # ✅ ADD THIS
    path('success/', views.success,name='success')
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('service/', views.service, name='service'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout,name='checkout'),

    path('crm/', views.crm, name='crm'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('update-status/<int:id>/<str:status>/', views.update_status, name='update_status'),
    path('export/', views.export_contacts, name='export_contacts'),

    path('login/', views.admin_login, name='login'),
    path('logout/', views.admin_logout, name='logout'),   # ✅ ADD THIS
    path('success/', views.success,name='success')
>>>>>>> 1b5ce9c (Initial commit)
]