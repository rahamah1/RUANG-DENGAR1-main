from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# --- Form Registrasi Pengguna ---
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('nama_lengkap', 'nim', 'prodi', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_lengkap'].label = "Nama"
        self.fields['nim'].label = "NIM"
        self.fields['prodi'].label = "Prodi"
        self.fields['email'].label = "Email Kampus"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Konfirmasi Password"

        self.fields['email'].widget.attrs.update({'placeholder': 'contoh.email@gmail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Ulangi password'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.USER  # Set role otomatis
        if commit:
            user.save()
        return user

# --- Form Registrasi Admin ---
class AdminUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('nama_lengkap', 'username', 'nidn', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nama_lengkap'].label = "Nama"
        self.fields['username'].label = "Username"
        self.fields['nidn'].label = "NIDN"
        self.fields['email'].label = "Email Kampus"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Konfirmasi Password"

        self.fields['email'].widget.attrs.update({'placeholder': 'contoh.email@gmail.com'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Minimal 8 karakter'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = CustomUser.Role.ADMIN  # Set role otomatis
        user.is_staff = True  # Admin harus bisa login ke admin site
        if commit:
            user.save()
        return user

# --- Form Login ---
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label='Email Kampus',
        widget=forms.EmailInput(attrs={'placeholder': 'contoh.email@gmail.com', 'autofocus': True})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Minimal 8 karakter', 'autocomplete': 'current-password'})
    )
    remember_me = forms.BooleanField(
        label='Remember me',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
