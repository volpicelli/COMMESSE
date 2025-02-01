# import form class from django
from django import forms
 
# import GeeksModel from models.py
from home.models import Personale
 
# create a ModelForm
class FormPersonale(forms.ModelForm):
    # specify the name of model to use
    
    class Meta:
        model = Personale
        fields = "__all__"
        
    """
    def __init__(self,*args,azienda=None,**kwargs):

        self.azienda = azienda
        #super().__init__(*args, **kwargs)
        super(FormCantiere, self).__init__(*args, **kwargs)
        #if instance is None:
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

            cz = Cliente.objects.filter(azienda_id=self.azienda).values_list('id', 'codcf')
            self.fields['cliente'] = forms.CharField(label="Cliente", required=True,
                                                    widget=forms.Select(choices=cz,
                                                                        attrs={'style': 'width: 300px;'}))
            self.fields['descrizione'] =  forms.CharField(label="Descrizione", required=True,
                                                         widget=forms.Textarea(attrs={'rows': 2}))
        #else:
    
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