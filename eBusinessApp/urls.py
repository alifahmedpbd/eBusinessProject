from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('home/', views.home, name='home'),

    path('signup/', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),


    path('team_view/', views.team_view, name='team_view'),
    path('createTeamMember/', views.createTeamMember, name='createTeamMember'),
    path('updateTeamMember/<str:pk>/', views.updateTeamMember, name="updateTeamMember"),
    path('deleteTeamMember/<str:pk>/', views.deleteTeamMember, name="deleteTeamMember"),


    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('createPortfolio/', views.createPortfolio, name='createPortfolio'),
    path('updatePortfolio/<str:pk>/', views.updatePortfolio, name="updatePortfolio"),
    path('deletePortfolio/<str:pk>/', views.deletePortfolio, name="deletePortfolio"),
    path('portfolio/<int:pk>/', views.portfolioDetails, name='portfolioDetails'),
    path('portfolio/category/<str:category>/', views.portfolioCategory,name="portfolioCategory"),

    
    path('contact/', views.contact_view, name='contact'),

    path('about/', views.about, name='about'),

    path('services/', views.service_view, name='services'),
    path('services/<int:pk>/', views.service_details, name='serviceDetails'),
    path('service/edit/<int:pk>/', views.update_service, name='update_service'),
    path('service/delete/<int:pk>/', views.delete_service, name='delete_service'),

    path('faq/', views.faq, name='faq'),
   
    path('career/', views.career, name='career'),
    path('job-application/<int:id>/', views.job_application, name='job_application'),
    path('create-job/', views.create_job, name='create_job'),
    path('job/edit/<int:pk>/', views.update_job, name='update_job'),
    path('job/delete/<int:pk>/', views.delete_job, name='delete_job'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)