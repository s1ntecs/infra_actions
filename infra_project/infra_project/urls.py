from django.contrib import admin
from django.urls import include, path

# from django.urls import include
# from django.contrib import admin

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
