# import form class from django
from django import forms
 
# import GeeksModel from models.py
from home.models import Cantiere,Cliente
 
# create a ModelForm
class ModuleSelectorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        self.widget_attrs({'style': 'width:200px;'}, )
        return "%s" % obj.codcf
    
class FormCantiere(forms.ModelForm):
    # specify the name of model to use
    
    class Meta:
        model = Cantiere
        fields = "__all__"
        
    
    def __init__(self,*args,**kwargs):
        self.azienda = kwargs.pop('azienda', None)
        #self.azienda = azienda
        #super().__init__(*args, **kwargs)
        super(FormCantiere, self).__init__(*args, **kwargs)
        #if instance is None:
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        cz = Cliente.objects.filter(azienda=self.azienda)#.values_list('id', 'codcf')
            #self.fields['cliente'] = forms.ModelChoiceField(queryset=cz, empty_label='(select)')
            #self.fields['cliente'] = ModuleSelectorModelChoiceField(queryset=cz,
            #                                                            empty_label='(select module)',
            #                                                            widget=forms.Select(
            #                                                                attrs={'style': 'width:300px'}, ))
        #self.fields['cliente'].queryset = cz

        self.fields['cliente'] = forms.ModelChoiceField(label="Module Name", required=False,queryset=cz,
                                                 widget=forms.Select(choices=cz,
                                                                     attrs={'style': 'max-width: 100%'}))

            #self.fields['cliente'] = forms.ModelChoiceField(queryset=Cliente.objects.filter(azienda_id=self.azienda), empty_label="Scegli cantiere",
            #                          widget=forms.Select(attrs={
            ##                              'class': "form-select text-center fw-bold",
            #                              'style': 'max-width: auto;',
            #                          }))
            
            #self.fields['cliente'] = forms.CharField(label="Cliente", required=True,
            #                                        widget=forms.Select(choices=cz,
            #                                                            attrs={'style': 'width: 300px;'}))
            
        self.fields['descrizione'] =  forms.CharField(label="Descrizione", required=True,
                                                         widget=forms.Textarea(attrs={'style': 'max-width: 100%','rows':2}))
        #else:
    """
    def clean_cliente_id(self):
        cliente_id = self.cleaned_data.get('cliente')
        try:
            self.cliente = Cliente.objects.get(pk=cliente_id)
        except Cliente.DoesNotExist:
            raise forms.ValidationError('Sorry, that course id is not valid.')

        return cliente_id
    
    
    def save(self, commit=True):

        instance = super(FormCantiere, self).save(commit=commit)
        #cl = Cliente.objects.get(pk=1) #instance.cliente)
        #instance.cliente = cl
        
        instance.save()
        return instance
    
    """