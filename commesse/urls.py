"""
URL configuration for miro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
#from graphene_django.views import GraphQLView

#from drf_yasg.views import get_schema_view
#from drf_yasg import openapi
#from demo.views import SendEmail

"""
schema_view = get_schema_view(
   openapi.Info(
      title="Dummy API",
      default_version='v1',
      description="Dummy description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dummy.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
"""

urlpatterns = [
    #path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('home.urls')),
    path('access/', include('access.urls')),
    path('cantieri/', include('cantieri.urls')),
    path('personale/', include('personale.urls')),
    path('ordini/', include('ordini.urls')),
    path('fatture/', include('fatture.urls')),
    #path('email', SendEmail.as_view()),
    #re_path(r'^playground/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    #re_path(r'^docs/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]
