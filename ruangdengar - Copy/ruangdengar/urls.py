# ruangdengar/urls.py

from django.contrib import admin
from django.urls import path, include  # Pastikan 'include' ada di sini

urlpatterns = [
    path('admin/', admin.site.urls),

    # Baris ini sudah benar, ia mengarahkan URL 'auth/'
    # ke file 'users/urls.py'
    path('', include('users.urls')),
]