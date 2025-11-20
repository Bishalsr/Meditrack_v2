from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Public landing page
    path('', views.landing_page, name='landing_page'),

    # Authentication
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='landing_page'), name='logout'),

    # Dashboards
    path('home/', views.home, name='home'),  # staff/admin dashboard
    path('patient-dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', views.doctor_dashboard, name='doctor_dashboard'),


    # Staff management
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('feedback/submit/', views.feedback_submit, name='feedback_submit'),

]

