from django.shortcuts import render
from app.settings.models import Settings, Do ,Ceo,Founder,Designer,Developer,Games,Games2,Games3,Games4,Games5,Contact,Will_talk
from app.settings.models import Settings,Phone,Email,Address
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     settings_id = Settings.objects.latest("id")
#     return render(request, 'base/index.html', locals())

class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['settings_id'] = Settings.objects.latest("id")
        context['do_id'] = Do.objects.latest("id")
        context['Ceo_id'] = Ceo.objects.latest("id")
        context['founder_id'] = Founder.objects.latest("id")
        context['designer_id'] = Designer.objects.latest("id")
        context['developer_id'] = Developer.objects.latest("id")
        context['games_id'] = Games.objects.latest("id")
        context['games2_id'] = Games2.objects.latest("id")
        context['games3_id'] = Games3.objects.latest("id")
        context['games4_id'] = Games4.objects.latest("id")
        context['games5_id'] = Games5.objects.latest("id")
        return context
        


class ContactView(TemplateView):
    template_name = 'base/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_id'] = Contact.objects.latest("id")
        context['will_talk_id'] = Will_talk.objects.latest("id")
        context['phone_id'] = Phone.objects.latest("id")
        context['email_id'] = Email.objects.latest("id")
        context['address_id'] = Address.objects.latest("id")
        return context
