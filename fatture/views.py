from django.shortcuts import render
from django.views.generic  import View,CreateView,DetailView,ListView
from django.views.generic.edit import UpdateView



from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect
from home.models import Fatture,Azienda
# Create your views here.

class FattureList(ListView):
    model=Fatture

    def get(self,request):
        context ={}
        #context['form']= FormPersonale  #(azienda=request.session['azienda'])
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['fatture'] = az.GetFatture()
        return render(request, "fatture.html", context)
  
class FattureDetail(DetailView):
    pass



class FattureAdd(CreateView):
    model=Fatture
    #form_class = FormFatture
    success_url = '/'
    
    queryset = Fatture.objects.all()
    #template_name='cantiere_nuovo.html'
    #create_form = Form.create(auto__model=Cantiere)
    #a_table = Table(auto__model=Cantiere)


    def get(self,request):
        context ={}
        #context['form']= FormCantiere(azienda=request.session['azienda'])
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['fatture'] = az.GetFatture()
        context['ordini'] = az.getOrdini()
        return render(request, "fattura_nuova.html", context)

    def post(self,request):
        
        #form = FormCantiere(request.POST,azienda=request.session['azienda'])

        #if form.is_valid():
        #    cantiere = form.save(commit=False)
        #    cantiere.save()

        return HttpResponseRedirect('/fatture/update/') #+str(cantiere.id))

