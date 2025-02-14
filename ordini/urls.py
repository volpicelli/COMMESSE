from django.urls import path
from .views import OrdineAdd,OrdiniList,OrdiniListDaMagazzino,OrdiniListPerMagazzino,OrdineUpdate #,\
                        #OrdiniPerMagazzinoAdd
from home.models import Ordine


urlpatterns = [
        
        path('add',OrdineAdd.as_view()),
        path('add/cantiere/<int:cantiere_id>',OrdineAdd.as_view()),
        path('update/<int:ordine_id>',OrdineUpdate.as_view()),
        path('list', OrdiniList.as_view()),
        path('damagazzino/list', OrdiniListDaMagazzino.as_view()),
        path('permagazzino/list', OrdiniListPerMagazzino.as_view()),
       # path('permagazzino/add', OrdiniPerMagazzinoAdd.as_view()),

        
        

]