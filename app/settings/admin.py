from django.contrib import admin
from app.settings.models import Settings, Info, About, Data
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
admin.site.register(About)
admin.site.register(Data) 