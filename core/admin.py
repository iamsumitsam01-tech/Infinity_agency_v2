from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Service, Project, Contact


# =========================
# NORMAL MODELS
# =========================

admin.site.register(Service)
admin.site.register(Project)


# =========================
# CONTACT ADMIN
# =========================

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('name', 'email')


# =========================
# USER ADMIN (GOOGLE LOGIN USERS)
# =========================

admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
    )