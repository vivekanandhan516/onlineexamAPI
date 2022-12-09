from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', include('examapp.urls')),
    path('', include('Candidate.urls')),
]
