from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('coaches/', views.coaches),
    path('contact/', views.contact),

    path('courses/', views.courses),
    path('free-session/', views.free_session),
    path('para/', views.para),
    path('tournaments/', views.tournaments),
    path('rating-system/', views.rating_system),

    path('files/<str:filename>', views.file_delivery, name='file'),
]
