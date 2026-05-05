<<<<<<< HEAD
from django.contrib import admin
from .models import Service, Project, Contact

admin.site.register(Service)
admin.site.register(Project)


from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_filter = ('status',)
=======
from django.contrib import admin
from .models import Service, Project, Contact

admin.site.register(Service)
admin.site.register(Project)


from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'status', 'created_at')
    list_filter = ('status',)
>>>>>>> 1b5ce9c (Initial commit)
    search_fields = ('name', 'email')