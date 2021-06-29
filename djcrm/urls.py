from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from leads.views import LandingPage
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , LandingPage.as_view()),
    path('leads/' , include('leads.urls' , namespace='leads')) , 
    path('login/'  , LoginView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
