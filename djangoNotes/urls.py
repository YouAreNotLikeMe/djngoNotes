from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/',include('api.urls')),
    path('', include('pages.urls'))
]
