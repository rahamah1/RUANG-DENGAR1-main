from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import CustomUserCreationForm, AdminUserCreationForm, CustomAuthenticationForm


# 🧩 Halaman Pilih Role
class RoleSelectionView(generic.TemplateView):
    template_name = 'users/role_selection.html'


# 🧩 Registrasi Pengguna
class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Akun Pengguna berhasil dibuat! Silakan login.')
        return super().form_valid(form)


# 🧩 Registrasi Admin
class AdminRegisterView(generic.CreateView):
    form_class = AdminUserCreationForm
    template_name = 'users/register_admin.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Akun Admin berhasil dibuat! Silakan login.')
        return super().form_valid(form)


# 🧩 Login View
class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        user = self.request.user
        # Arahkan sesuai role
        if user.role == CustomUser.Role.ADMIN:
            return reverse_lazy('dashboard_admin')
        else:
            return reverse_lazy('dashboard_user')

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            messages.info(self.request, 'Anda akan logout otomatis saat browser ditutup.')
        else:
            self.request.session.set_expiry(None)
        return super().form_valid(form)


# 🧩 Dashboard Admin
@login_required(login_url='login')
def dashboard_admin_view(request):
    return render(request, 'dashboard.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        # 🎉 Tambahkan active_page: 'dashboard'
        'active_page': 'dashboard',
    })

# 🧩 Halaman Kelola Jadwal Konseling (Admin)
@login_required(login_url='login')
def kelola_jadwal_view(request):
    return render(request, 'dashboard/kelola_jadwal.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'kelola-jadwal',  # supaya menu sidebar aktif
    })

# 🧩 Halaman Lihat Jadwal Konseling (Admin)
@login_required(login_url='login')
def lihat_jadwal_view(request):
    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini.')
        return redirect('dashboard_user')  # redirect ke dashboard user
    return render(request, 'dashboard/lihat_jadwal.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'lihat-jadwal',
    })


# 🧩 Dashboard Pengguna
@login_required(login_url='login')
def dashboard_user_view(request):
    return render(request, 'users/dashboard_user.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
    })


# 🧩 Halaman Home (umum)
@login_required(login_url='login')
def home_view(request):
    # 🎯 Langsung periksa role dan arahkan (redirect) ke dashboard yang benar
    if request.user.role == CustomUser.Role.ADMIN:
        return redirect('dashboard_admin')
    else:
        return redirect('dashboard_user')

@login_required(login_url='login')
def kelola_laporan_view(request):
    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini.')
        return redirect('dashboard_user')
    return render(request, 'dashboard/kelola_laporan.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'kelola-laporan',  # supaya menu sidebar aktif
    })

@login_required(login_url='login')
def kelola_pengguna_view(request):
    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini.')
        return redirect('dashboard_user')
    return render(request, 'dashboard/kelola_pengguna.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'kelola-pengguna',  # supaya menu sidebar aktif
    })


# 🧩 Halaman Edit Laporan (VIEW BARU)
@login_required(login_url='login')
def edit_laporan_view(request, report_id):
    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini.')
        return redirect('dashboard_user')
        
    # TODO: Logika untuk mengambil objek Laporan berdasarkan report_id

    return render(request, 'dashboard/edit_laporan.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'kelola-laporan',
        'report_id': report_id, # untuk ditampilkan di template
    })


# 🧩 Halaman Kelola Konten (VIEW BARU)
@login_required(login_url='login')
def kelola_konten_view(request):
    if request.user.role != CustomUser.Role.ADMIN:
        messages.error(request, 'Anda tidak memiliki akses ke halaman ini.')
        return redirect('dashboard_user')

    # TODO: Logika untuk mengambil dan menampilkan daftar Konten (jika ada)

    return render(request, 'dashboard/kelola_konten.html', {
        'nama_user': request.user.nama_lengkap,
        'email_user': request.user.email,
        'active_page': 'kelola-konten', # supaya menu sidebar aktif
    })