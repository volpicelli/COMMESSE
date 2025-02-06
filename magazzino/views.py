from django.shortcuts import render
from django.views.generic  import View,CreateView,DetailView,ListView
from django.db.models import Sum,Avg
from home.models import Magazzino,Azienda
# Create your views here.



class MagazzinoList(ListView):
    model=Magazzino
    def get(self,request):
        context ={}
        #context['form']= FormOrdine(azienda=request.session['azienda'])
        a = Azienda.objects.get(pk=request.session['azienda'])
        ma = Magazzino.objects.values('descrizione').annotate(quantita=Sum('quantita'),prezzo=Avg('prezzo_unitario')).filter(azienda=a)

        context['magazzino'] = ma # Magazzino.objects.filter(azienda=a)
        #context['cantieri'] = a.getCantieri()
        return render(request, "magazzinolist.html", context)
