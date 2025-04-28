from django.contrib import admin
from django.urls import path
from weather import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('weather/', views.weather, name='weather'),  # Handles form submission
    path('weather/display/', views.weather_display, name='weather_display'),  # Handles displaying result
]
