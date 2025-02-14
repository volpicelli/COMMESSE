from django.shortcuts import render,redirect
from django.views.generic  import View,CreateView,DetailView,ListView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ObjectDoesNotExist

from django.db.models import Sum

from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect
from .form_cantiere import FormCantiere
from home.models import Cantiere,Cliente,Azienda

# Create your views here.
#class CantiereDetail(DetailView):

class GetCantieri(View):
    def get(self,request):
        #az = Azienda.objects.get(current=True)
        az = Azienda.objects.get(id=request.session['azienda'])

        fatture = az.GetFatture()
        clienti=Cliente.objects.filter(azienda=az)
        tutticantieri_id = []
        for one in clienti:
            try:
                cantiere = Cantiere.objects.filter(cliente=one)
                for o in cantiere:
                    tutticantieri_id.append(o.id)
            except ObjectDoesNotExist:
                pass
        #c = Cantiere.objects.all()
        tutticantieri = Cantiere.objects.filter(id__in=tutticantieri_id).order_by('-status','-data_inizio_lavori')
        context={"cantiere":tutticantieri,'azienda': request.session['azienda'],'fatture':fatture}
        template = loader.get_template('cantieri.html')
        return HttpResponse(template.render(context, request))

class CantiereAdd(CreateView):
    model=Cantiere
    form_class = FormCantiere
    success_url = '/'
    #template_name='cantiere_nuovo.html'
    #create_form = Form.create(auto__model=Cantiere)
    #a_table = Table(auto__model=Cantiere)


    def get(self,request):
        context ={}
        context['form']= FormCantiere(azienda=request.session['azienda'])
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['clienti'] = az.azienda_cliente.all()
        return render(request, "cantiere_nuovo.html", context)

    def post(self,request):
        
        form = FormCantiere(request.POST,azienda=request.session['azienda'])

        if form.is_valid():
            cantiere = form.save(commit=False)
            cantiere.save()

        return HttpResponseRedirect('/cantiere/update/'+str(cantiere.id))
    
#
class CantiereDetail(DetailView):
    model = Cantiere
    template_name = 'cantiere.html'

    def get(self,request,cantiere_id):
        cantiere = Cantiere.objects.get(pk=cantiere_id)
        ordini = cantiere.GetOrdini()
        fatture = cantiere.GetFatture()
        personaleassegnato = cantiere.cantiere_assegnato.all()
        totale=0
        for one in personaleassegnato:
            tot = float(one.ore_lavorate * one.personale.wage_lordo)
            totale+=tot



        context ={}
        context['fatture']= fatture
        context['cantiere']= cantiere
        context['ordini']= ordini
        totale_ordini = ordini.aggregate(Sum('importo'))
        if totale_ordini['importo__sum'] is None:
            totale_ordini['importo__sum']=0.0
        context['totale_ordini'] = totale_ordini['importo__sum']
        context['personaleassegnato']= personaleassegnato
        context['totalepersonale']= totale
        
        context['totalecantiere']= totale + totale_ordini['importo__sum']


        
        return render(request, "cantiere_detail.html", context)
"""
class FattureCantiere(ListView):
    model = Fatture
    template_name = 'cantiere.html'

    def get(self,request,cantiere_id):
        cantiere = Cantiere.objects.get(pk=cantiere_id)
        ordini = cantiere.GetOrdini()
        fatture = cantiere.GetFatture()
        personaleassegnato = cantiere.cantiere_assegnato.all()



        context ={}
        context['fatture']= fatture
        context['cantiere']= cantiere
        context['ordini']= ordini
        context['personaleassegnato']= personaleassegnato
        
        return render(request, "cantiere_detail.html", context)

"""


class CantiereUpdate(UpdateView):
    model = Cantiere
    template_name = 'cantiere.html'
    #form_class = FormCantiere()
    #fields ="__all__" #['nome','descrizione']
    success_url ="/"

 
    def get(self,request,pk):
        context ={}
        cant = Cantiere.objects.get(pk=pk)
        context['form']= FormCantiere(instance=cant,azienda=request.session['azienda'])
        return render(request, "cantiere.html", context)


    def post(self,request,pk):
        cant = Cantiere.objects.get(pk=pk)
        form = FormCantiere(request.POST,instance=cant)#,azienda=request.session['azienda'])
        

        context={}
        context['form'] = form
        form.fields['cliente'].queryset = Cliente.objects.filter(azienda=request.session['azienda'])#.values_list('id', 'codcf')

        if form.is_valid():
            cantiere = form.save(commit=False)
            cantiere.save()
        #self.context['detail'] = Cantiere.objects.all()
        return render(request, 'cantiere.html', context)
#

class CantieriOrdini(View):

    def get(sef,request,cantiere_id):
        context ={}
        cantiere = Cantiere.objects.get(pk=cantiere_id)
        ordini = cantiere.GetOrdini()
        context['ordini'] = ordini
        return render(request, 'cantiereordini.html', context)

class CantieriFatture(View):

    def get(sef,request,cantiere_id):
        context ={}
        cantiere = Cantiere.objects.get(pk=cantiere_id)
        fatture = cantiere.GetFatture()
        context['fatture'] = fatture
        return render(request, 'cantierefatture.html', context)
