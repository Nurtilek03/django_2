from django.contrib import admin
from app.settings.models import Settings, Info, About, Data ,Creator ,End_Work ,Design ,Development ,Branding , Photography ,Fun_facts 
from app.settings.models import Settings,Custom_CMS ,Custom_CMS2 ,Custom_CMS3 ,Custom_CMS4
# Register your models here.
admin.site.register(Settings)
admin.site.register(Info)
admin.site.register(About)
admin.site.register(Data) 
admin.site.register(Creator) 
admin.site.register(End_Work) 
admin.site.register(Design) 
admin.site.register(Development) 
admin.site.register(Branding) 
admin.site.register(Photography) 
admin.site.register(Fun_facts) 
admin.site.register(Custom_CMS) 
admin.site.register(Custom_CMS2) 
admin.site.register(Custom_CMS3) 
admin.site.register(Custom_CMS4) 