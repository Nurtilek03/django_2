from django.contrib import admin
from app.settings.models import Settings ,Do ,Ceo,Founder,Designer,Developer,Games,Games2,Games3,Games4,Games5,Contact,Will_talk
from app.settings.models import Settings ,Phone,Email,Address
# Register your models here.
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_filter = ['id', 'title']
    search_fields = ['id', 'title']
admin.site.register(Do)
admin.site.register(Ceo)
admin.site.register(Founder)
admin.site.register(Designer)
admin.site.register(Developer)
admin.site.register(Games)
admin.site.register(Games2)
admin.site.register(Games3)
admin.site.register(Games4)
admin.site.register(Games5)
admin.site.register(Contact)
admin.site.register(Will_talk)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)