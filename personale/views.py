from django.shortcuts import render,redirect
from django.views.generic  import View,CreateView,DetailView,ListView
from django.views.generic.edit import UpdateView



from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse,HttpResponseRedirect
from .form_personale import FormPersonale
from home.models import Personale,Azienda,Assegnato_Cantiere,Cantiere

# Create your views here.
#class CantiereDetail(DetailView):
class PersonaleList(ListView):
    model=Personale

    def get(self,request):
        context ={}
        #context['form']= FormPersonale  #(azienda=request.session['azienda'])
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['personale'] = az.getPersonale
        context['cantieri'] = az.getCantieri
        personale = az.getPersonale()
        assegnato_cantiere=[]
        for one in personale:
            assegnato  = one.personale_assegnato.all()
            for a in assegnato:
                assegnato_cantiere.append(a)
        context['assegnato_cantiere'] = assegnato_cantiere
        return render(request, "personale.html", context)
    def post(self,request):
        p_id = request.POST.get('personale')
        c_id = request.POST.get('cantiere')
        responsabile = request.POST.get('responsabile',False)
        if responsabile == 'on':
            responsabile=True
        personale = Personale.objects.get(pk=p_id)
        cantiere = Cantiere.objects.get(pk=c_id)
        ac =Assegnato_Cantiere(personale=personale,cantiere=cantiere,responsabile=responsabile)

        ac.save()
        context ={}
        #context['form']= FormPersonale  #(azienda=request.session['azienda'])
        az = Azienda.objects.get(pk=request.session['azienda'])
        context['personale'] = az.getPersonale
        context['cantieri'] = az.getCantieri
        personale = az.getPersonale()
        assegnato_cantiere=[]
        for one in personale:
            assegnato  = one.personale_assegnato.all()
            for a in assegnato:
                assegnato_cantiere.append(a)
        context['assegnato_cantiere'] = assegnato_cantiere
        return render(request, "personale.html", context)

class PersonaleAdd(CreateView):
    model=Personale
    form_class = FormPersonale
    success_url = '/'

    #create_form = Form.create(auto__model=Cantiere)
    #a_table = Table(auto__model=Cantiere)

    #class Meta:
    #    title = 'An iommi page!'

    def get(self,request):
        context ={}
        context['form']= FormPersonale  #(azienda=request.session['azienda'])
        return render(request, "personale.html", context)
    


class PersonaleDetail(DetailView):
    model = Personale
    #template_name = 'cantiere.html'

    def get(self,request,personale_id):
        personale = Personale.objects.get(pk=personale_id)
        #personaleassegnato = cantiere.cantiere_assegnato.all()



        context ={}
        context['personale']= personale
        #context['personaleassegnato']= personaleassegnato
        
        return render(request, "personale_detail.html", context)

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
