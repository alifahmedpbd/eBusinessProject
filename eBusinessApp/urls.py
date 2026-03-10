from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.root_redirect, name='root'),
    path('home/', views.home, name='home'),

    # Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin dashboard
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Team
    path('team_view/', views.team_view, name='team_view'),
    path('createTeamMember/', views.createTeamMember, name='createTeamMember'),
    path('updateTeamMember/<str:pk>/', views.updateTeamMember, name="updateTeamMember"),
    path('deleteTeamMember/<str:pk>/', views.deleteTeamMember, name="deleteTeamMember"),

    # Portfolio
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('createPortfolio/', views.createPortfolio, name='createPortfolio'),
    path('updatePortfolio/<str:pk>/', views.updatePortfolio, name="updatePortfolio"),
    path('deletePortfolio/<str:pk>/', views.deletePortfolio, name="deletePortfolio"),
    path('portfolio/<int:pk>/', views.portfolioDetails, name='portfolioDetails'),
    path('portfolio/category/<str:category>/',
     views.portfolioCategory,
     name="portfolioCategory"),

    # Contact
    path('contact/', views.contact_view, name='contact'),
    path('about/', views.about, name='about')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)