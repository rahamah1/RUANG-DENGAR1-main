from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views
from .views import (
    RoleSelectionView,
    UserRegisterView,
    AdminRegisterView,
    CustomLoginView,
    home_view,
    dashboard_admin_view,
    dashboard_user_view,
    kelola_laporan_view,
    kelola_pengguna_view,
    edit_laporan_view,
    kelola_konten_view,
    # Pastikan Anda mengimpor view untuk notifikasi jika menggunakan Class-Based View
)

urlpatterns = [
    # Halaman login utama
    path('', CustomLoginView.as_view(), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),


    # Registrasi
    path('register/select-role/', RoleSelectionView.as_view(), name='select_role'),
    path('register/user/', UserRegisterView.as_view(), name='register_user'),
    path('register/admin/', AdminRegisterView.as_view(), name='register_admin'),

    # Dashboard
    path('dashboard/admin/', dashboard_admin_view, name='dashboard_admin'),
    path('dashboard/user/', dashboard_user_view, name='dashboard_user'),

    # Detail Artikel User
    path('dashboard/user/artikel/<int:id>/', views.artikel_detail_view, name='artikel-detail'),
    # Buat Laporan User
    path('dashboard/user/buat-laporan/', views.buat_laporan_view, name='buat-laporan'),
    # Riwayat Laporan User
    path('dashboard/user/riwayat-laporan/', views.riwayat_laporan_view, name='riwayat-laporan'),
    # Detail Laporan User
    path("laporan/<int:report_id>/detail/", views.detail_laporan_view, name="detail-laporan"),
    # Booking Konseling User
    path("dashboard/user/buat-booking-konseling/", views.booking_konseling_view, name="booking-konseling"),
    # Status Laporan User
    path("dashboard/user/status-laporan/", views.status_laporan_view, name="status-laporan"),
    # Laporan Terkirim User
    path("dashboard/user/laporan-terkirim/", views.laporan_terkirim_view, name="laporan-terkirim"),

    #Kelola Jadwal Punya Admin
    path('dashboard/kelola-jadwal/', views.kelola_jadwal_view, name='kelola-jadwal'),
    #Lihat Jadwal Punya Admin
    path('dashboard/lihat-jadwal/', views.lihat_jadwal_view, name='lihat-jadwal'), 

    path('dashboard/kelola-laporan/', views.kelola_laporan_view, name='kelola-laporan'),
    # 🎉 Kelola Pengguna Punya Admin
    path('dashboard/kelola-pengguna/', views.kelola_pengguna_view, name='kelola-pengguna'),
    # Edit Laporan (URL BARU)
    path('dashboard/laporan/edit/<int:report_id>/', views.edit_laporan_view, name='edit-laporan'), 
    # 🎉 URL BARU UNTUK KELOLA KONTEN
    path('dashboard/kelola-konten/', views.kelola_konten_view, name='kelola-konten'),
    # --- Penambahan URL Notifikasi ---
    

    
    # Home
    path('home/', home_view, name='home'),
]