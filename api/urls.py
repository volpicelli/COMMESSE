
from django.urls import path,re_path
from api.view_azienda import *
from api.view_tipologia_lavori import *
from api.view_articoli import *
from api.view_assegnato_cantiere import *
from api.view_cliente import *
from api.view_cantiere import *
from rest_framework.authtoken.views import obtain_auth_token  
from api.views import   ResponsabileCantiere,AddOreLavoro,FattureOrdine,\
                        FattureDetail,FattureList,FornitoriDetail,FornitoriList,\
                        OrdineDetail,OrdineList,PersonaleDetail,PersonaleList,\
                        PersonaleSuCantiere,MagazzinoList,MagazzinoDetail,MagazzinoArticoli,CantieriPersonale,\
                        OrdineGetTipologia,OrdineCreate,OrdineDaMagazzino,GroupMagazzino,LoginView,CustomAuthToken
                
                        #ResponsabileDetail,ResponsabileList,ResponsabileCantiere,\

urlpatterns = [ 
        path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),  # <-- And here

        path('login',LoginView.as_view()),
        path('ordinedamagazzino',OrdineDaMagazzino.as_view()),
        path('ordinecreate',OrdineCreate.as_view()),
        path('azienda/<int:azienda_id>/clienti',ClientiAzienda.as_view()),
        path('azienda/<int:azienda_id>/cantieri',CantieriAzienda.as_view()),
        path('azienda/<int:azienda_id>/personale',PersonaleAzienda.as_view()),
        path('azienda/<int:azienda_id>/personale/cantiere/<int:cantiere_id>',PersonaleAziendaCantiere.as_view()),
        

        path('addorelavoro/cantiere/<int:cantiere_id>/personale/<int:personale_id>/<int:ore>',AddOreLavoro.as_view()),

        path('personale/cantiere/<int:id_cantiere>',PersonaleSuCantiere.as_view()),
        path('responsabile/cantiere/<int:id_cantiere>',ResponsabileCantiere.as_view()),
        path('cantieri/personale/<int:id_personale>',CantieriPersonale.as_view()),
        path('assegnatocantiere/list', Assegnato_CantiereList.as_view()),
        path('assegnatocantiere/create', Assegnato_CantiereList.as_view()),
        path('assegnatocantiere/detail/<int:pk>', Assegnato_CantiereDetail.as_view()),
        path('assegnatocantiere/delete/<int:pk>', Assegnato_CantiereDetail.as_view()),
        path('assegnatocantiere/update/<int:pk>', Assegnato_CantiereDetail.as_view()),
        path('assegnatocantiere/remove/<int:pk>', Remove_Lavoratore_Cantiere.as_view()),


        path('tipologialavori/list', TipologiaLavoriList.as_view()),
        path('tipologialavori/create', TipologiaLavoriList.as_view()),
        path('tipologialavori/detail/<int:pk>', TipologiaLavoriDetail.as_view()),
        path('tipologialavori/delete/<int:pk>', TipologiaLavoriDetail.as_view()),
        path('tipologialavori/update/<int:pk>', TipologiaLavoriDetail.as_view()),

        path('fornitori/list', FornitoriList.as_view()),
        path('fornitori/create', FornitoriList.as_view()),
        path('fornitori/detail/<int:pk>', FornitoriDetail.as_view()),
        path('fornitori/delete/<int:pk>', FornitoriDetail.as_view()),
        path('fornitori/update/<int:pk>', FornitoriDetail.as_view()),

        path('personale/list', PersonaleList.as_view()),
        path('personale/create', PersonaleList.as_view()),
        path('personale/detail/<int:pk>', PersonaleDetail.as_view()),
        path('personale/delete/<int:pk>', PersonaleDetail.as_view()),
        path('personale/update/<int:pk>', PersonaleDetail.as_view()),



        path('groupmagazzino', GroupMagazzino.as_view()),

        path('magazzino/list', MagazzinoList.as_view()),
        path('magazzino/create', MagazzinoList.as_view()),
        path('magazzino/detail/<int:pk>', MagazzinoDetail.as_view()),
        path('magazzino/delete/<int:pk>', MagazzinoDetail.as_view()),
        path('magazzino/update/<int:pk>', MagazzinoDetail.as_view()),
        path('magazzino/articoli', MagazzinoArticoli.as_view()),


        path('cantieri/list', CantiereList.as_view()),
        
        path('cantieri/azienda/<int:azienda_id>', CantieriAzienda.as_view()),
        path('cantiere/create', CantiereList.as_view()),
        path('cantiere/detail/<int:pk>',CantiereDetail.as_view()),
        path('cantiere/delete/<int:pk>', CantiereDetail.as_view()),
        path('cantiere/update/<int:pk>',CantiereDetail.as_view()),
        path('cantiere/<int:cantiere_id>/ordini',OrdiniCantiere.as_view()),



        path('grouparticoli', GroupArticoli.as_view()),

        path('articoli/list', ArticoliList.as_view()),
        path('articoli/create',ArticoliList.as_view()),
        path('articoli/detail/<int:pk>',ArticoliDetail.as_view()),
        path('articoli/delete/<int:pk>', ArticoliDetail.as_view()),
        path('articoli/update/<int:pk>',ArticoliDetail.as_view()),

        path('articoli/ordine/<int:id_ordine>',ArticoliOrdine.as_view()),

        path('azienda/setcurrent/<int:id_azienda>', SetCurrentAzienda.as_view()),
        path('azienda/getcurrent', CurrentAzienda.as_view()),
        path('azienda/list', AziendaList.as_view()),
        path('azienda/create',AziendaList.as_view()),
        path('azienda/detail/<int:pk>',AziendaDetail.as_view()),
        path('azienda/delete/<int:pk>', AziendaDetail.as_view()),
        path('azienda/update/<int:pk>',AziendaDetail.as_view()),

        path('cliente/getpersoc', ClientePersoc.as_view()),
        #path('cliente/listall', ClienteListAll.as_view()),
        path('cliente/list', ClienteListAll.as_view()),

        path('cliente/create',ClienteList.as_view()),
        path('cliente/detail/<int:pk>',ClienteDetail.as_view()),
        path('cliente/delete/<int:pk>', ClienteDetail.as_view()),
        path('cliente/update/<int:pk>',ClienteDetail.as_view()),


        path('fatture/ordine/<int:ordine_id>', FattureOrdine.as_view()),
        path('fatture/list', FattureList.as_view()),
        path('fatture/create',FattureList.as_view()),
        path('fatture/detail/<int:pk>',FattureDetail.as_view()),
        path('fatture/delete/<int:pk>', FattureDetail.as_view()),
        path('fatture/update/<int:pk>',FattureDetail.as_view()),


        path('ordine/getTipologia', OrdineGetTipologia.as_view()),
        path('ordine/list', OrdineList.as_view()),
        path('ordine/create',OrdineList.as_view()),
        path('ordine/detail/<int:pk>',OrdineDetail.as_view()),
        path('ordine/delete/<int:pk>', OrdineDetail.as_view()),
        path('ordine/update/<int:pk>',OrdineDetail.as_view()),
        #path('ordine/<int:ordine_id>/articoli',ArticoliOrdine.as_view()),
        
        path('ordini/cantiere/<int:id_cantiere>',OrdiniCantiere.as_view()),
        path('fatture/cantiere/<int:id_cantiere>',FattureCantiere.as_view()),


        

]
    
