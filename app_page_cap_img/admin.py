from django.contrib import admin
from .models import PageCapImage, LeadsEmail
from .models import Media, Configuracao

# -------------------------------------------
# Register your models here.
# -------------------------------------------

class ConfigModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', "update", 'timestamp']
    list_display_links = ['update', '__str__']
    list_filter = ["update"]
    search_fields = ['tipo_media','midea_position']
    class Meta:
        model = Configuracao


class MediaModelAdmin(admin.ModelAdmin):
    list_display = ['__str__', "update", 'timestamp']
    list_display_links = ['update', '__str__']
    list_filter = ["update"]
    search_fields = ['image','arquivo_pdf']
    class Meta:
        model = Media


class MaterialModelAdmin(admin.ModelAdmin):
    list_display = ['material',  'user', "update", 'timestamp']
    list_display_links = ['update',]
    list_filter = ["update", 'user', 'material']
    search_fields = [ 'user', 'material','headline']
    list_editable = ['material']
    class Meta:
        model = PageCapImage


class LeadEmailModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'timestamp']
    # list_display_links = ['update']
    list_filter = ["email"]
    search_fields = ['email']
    # list_editable = ['email']
    class Meta:
        model = LeadsEmail


admin.site.register(
    PageCapImage,
    MaterialModelAdmin
)
admin.site.register(
    LeadsEmail,
    LeadEmailModelAdmin
)
admin.site.register(
    Configuracao,
    ConfigModelAdmin
)
admin.site.register(Media, MediaModelAdmin)