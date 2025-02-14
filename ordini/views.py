from django.shortcuts import render,redirect
from django.views.generic  import View,CreateView,ListView
from django.views.generic.edit import UpdateView
from django.db.models import Sum,Avg



from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect
from .form_ordini import FormOrdine
from home.models import Ordine,Fornitori,Azienda,Magazzino,Articoli

# Create your views here.
#class CantiereDetail(DetailView):


class OrdiniList(ListView):
    model=Ordine
    def get(self,request):
        context ={}
        #context['form']= FormOrdine(azienda=request.session['azienda'])
        a = Azienda.objects.get(pk=request.session['azienda'])
        context['ordini'] = a.getOrdini().order_by('id')
        #context['cantieri'] = a.getCantieri()
        return render(request, "ordinilist.html", context)
class OrdiniListDaMagazzino(ListView):
    model=Ordine
    def get(self,request):
        context ={}
        #context['form']= FormOrdine(azienda=request.session['azienda'])
        a = Azienda.objects.get(pk=request.session['azienda'])
        context['ordini'] = a.getOrdini().filter(mestesso=True).order_by('id')
        #context['cantieri'] = a.getCantieri()
        return render(request, "ordinilist_damagazzino.html", context)

class OrdiniListPerMagazzino(ListView):
    model=Ordine
    def get(self,request):
        context ={}
        #context['form']= FormOrdine(azienda=request.session['azienda'])
        a = Azienda.objects.get(pk=request.session['azienda'])
        context['ordini'] = a.getOrdini().filter(magazzino=True).order_by('id')
        #context['cantieri'] = a.getCantieri()
        return render(request, "ordinilist_permagazzino.html", context)
#class OrdiniPerMagazzinoAdd(CreateView):
    
class OrdineAdd(CreateView):
    model=Ordine
    form_class = FormOrdine
    success_url = '/'

    #create_form = Form.create(auto__model=Cantiere)
    #a_table = Table(auto__model=Cantiere)


    def get(self,request,cantiere_id=None):
        if cantiere_id is None:
            context ={}
            context['form']= FormOrdine(azienda=request.session['azienda'])
            a = Azienda.objects.get(pk=request.session['azienda'])
            context['tipologia'] = Ordine().TipologiaFornitore
            #context['ordini'] = a.getOrdini()
            context['cantieri'] = a.getCantieri()
            context['fornitori'] = a.azienda_fornitore.all()
            context['articoli'] = Articoli.objects.values('descrizione').annotate(quantita=Sum('quantita'),prezzo=Avg('prezzo_unitario')).all() #filter(azienda=a)
        else:
            context ={}
            context['form']= FormOrdine(azienda=request.session['azienda'])
            a = Azienda.objects.get(pk=request.session['azienda'])
            context['tipologia'] = Ordine().TipologiaFornitore
            #context['ordini'] = a.getOrdini()
            context['cantieri'] = a.getCantieri().filter(pk=cantiere_id)
            context['fornitori'] = a.azienda_fornitore.all()
            context['articoli'] = Articoli.objects.values('descrizione').annotate(quantita=Sum('quantita'),prezzo=Avg('prezzo_unitario')).all() #.filter(azienda=a)


        return render(request, "ordine_nuovo.html", context)
    


    def post(self,request,cantiere_id=None):
        #id = request.POST.get['cliente']
        #cl =Cliente.objects.get(pk=id) 
        form = FormOrdine(request.POST,azienda=request.session['azienda'])
        form.fields['fornitore'].queryset = Fornitori.objects.filter(azienda=request.session['azienda'])#.values_list('id', 'codcf')

        if form.is_valid():
            # create a new `Band` and save it to the db
            ordine = form.save(commit=False)
        #cl = Cliente.objects.get(pk=cantiere.cliente) 
        #cantiere.cliente = cl #instance.cliente)
            ordine.save()

        # redirect to the detail page of the band we just created
        # we can provide the url pattern arguments as arguments to redirect function
        return HttpResponseRedirect('/ordine/update/'+str(ordine.id))
        #return redirect('pollo')
   


class OrdineUpdate(UpdateView):

    model = Ordine
    template_name = 'ordine.html'
    #form_class = FormCantiere()
    #fields ="__all__" #['nome','descrizione']
    success_url ="/"

 
    def get(self,request,ordine_id):
        context ={}
        ordine = Ordine.objects.get(pk=ordine_id)
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['cantieri'] = az.getCantieri()
        context['fornitori'] = az.azienda_fornitore.all()
        context['ordine'] = ordine
        context['articoli'] = ordine.ordine_articoli.all()
        context['tipologia'] = Ordine.TipologiaFornitore
        context['form']= FormOrdine(instance=ordine,azienda=request.session['azienda'])
        return render(request, "ordine_update.html", context)

    """
    def post(self,request):
        #id = request.POST.get['cliente']
        #cl =Cliente.objects.get(pk=id) 
        form = FormCantiere(request.POST,azienda=request.session['azienda'])
        #if form.is_valid():
            # create a new `Band` and save it to the db
        cantiere = form.save(commit=False)
        cl = Cliente.objects.get(pk=cantiere.cliente) 
        cantiere.cliente = cl #instance.cliente)
        cantiere.save()

        # redirect to the detail page of the band we just created
        # we can provide the url pattern arguments as arguments to redirect function
        return HttpResponseRedirect('/cantiere/update/'+str(cantiere.id))
        #return redirect('pollo')
    
#

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
        if form.is_valid():
            form.save()
        #self.context['detail'] = Cantiere.objects.all()
        return render(request, 'cantiere.html', context)
#
"""
