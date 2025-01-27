from django.shortcuts import render
from app.settings.models import Settings, Info, About, Data,Creator ,End_Work ,Design ,Development ,Branding , Photography ,Fun_facts 
from app.settings.models import Settings, Custom_CMS ,Custom_CMS2 ,Custom_CMS3 ,Custom_CMS4
# Register your models here.

def index(request):
    settings_id = Settings.objects.latest("id")
    info_all = Info.objects.all()
    about = About.objects.latest("id")
    data = Data.objects.latest("id")
    creator = Creator.objects.latest("id")
    end_work = End_Work.objects.latest("id")
    design = Design.objects.latest("id")
    development = Development.objects.latest("id")
    branding = Branding.objects.latest("id")
    photography = Photography.objects.latest("id")
    fun_facts = Fun_facts.objects.latest("id")
    custom_CMS = Custom_CMS.objects.latest("id")
    custom_CMS2 = Custom_CMS2.objects.latest("id")
    custom_CMS3 = Custom_CMS3.objects.latest("id")
    custom_CMS4 = Custom_CMS4.objects.latest("id")
    return render(request, "index.html", locals())