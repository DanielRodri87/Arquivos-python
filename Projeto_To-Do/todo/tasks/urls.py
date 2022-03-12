from django.urls import path 
from . import views
urlpatterns = [
    path('helloword/', views.helloworld),
]

# desinstalar django: pip uninstall django